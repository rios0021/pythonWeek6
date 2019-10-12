# Function to clear the screen of the gxfhat
def clearScreen():
    from gfxhat import lcd
    lcd.clear()
    lcd.show()

# Function to show a random color on each of the Leds of the gfx hat
def randomLedColor():
    from gfxhat import backlight
    from random import randint
    for x in range(6):
        backlight.set_pixel(x ,randint(0,255),randint(0,255),randint(0,255))
    backlight.show()

# Function to display text in the gfx hat at given coordinates
def displayText(text,x,y):
    from gfxhat import lcd,  fonts, backlight
    from PIL import Image, ImageFont, ImageDraw
    lcd.clear()
    width, height = lcd.dimensions()
    image = Image.new('P', (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(fonts.BitbuntuFull , 10)
    w, h = font.getsize(text)
    draw.text((x,y), text, 1, font)
    for x1 in range(x,x+w):
        for y1 in range(y,y+h):
            pixel = image.getpixel((x1, y1))
            lcd.set_pixel(x1, y1, pixel)
    lcd.show() 

# Function to Draw a pixel to the right of the given gfxhat coordenates, and return the new x coordenate
def drawPixelRight(x,y):
    from gfxhat import lcd
    x += 1
    if (x > 127):
        x = 0
    lcd.set_pixel(x,y,1)
    lcd.show()
    return x

# Function to Draw a pixel to the left of the given gfxhat coordenates, and return the new x coordenate
def drawPixelLeft(x,y):
    from gfxhat import lcd
    x -= 1
    if (x < 0):
        x = 127
    lcd.set_pixel(x,y,1)
    lcd.show()
    return x

# Function to Draw a pixel up of the given gfxhat coordenates, and return the new y coordenate
def drawPixelUp(x,y):
    from gfxhat import lcd
    y -= 1
    if (y < 0):
        y = 63
    lcd.set_pixel(x,y,1)
    lcd.show()
    return y

# Function to Draw a pixel down of the given gfxhat coordenates, and return the new y coordenate
def drawPixelDown(x,y):
    from gfxhat import lcd
    y += 1
    if (y > 63):
        y = 0
    lcd.set_pixel(x,y,1)
    lcd.show()
    return y

# Etch a sketch function,use arrows to draw in the gfxhat exit pressing 'q'
def etchSketch():
    import click
    from gfxhat import lcd, backlight
    from random import randint
    import os
    from rios0021Library import clearBacklight
    print("Etch a Sketch running, use arrow keys to draw, 's' to restart or 'q' to exit...")
    exit = False
    x = 64
    y = 32
    clearScreen()
    displayText("Etch a Sketch", 40, 54)
    while(exit != True):
        keyPressed = click.getchar()
        if(keyPressed == '\x1b[A'):
            y = drawPixelUp(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[B'):
            y = drawPixelDown(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[C'):
            x = drawPixelRight(x,y)
            randomLedColor()
        elif(keyPressed == '\x1b[D'):
            x = drawPixelLeft(x,y)
            randomLedColor()
        elif(keyPressed == 'q' or keyPressed == 'Q'):
            exit = True
            clearScreen()
            clearBacklight()
        elif(keyPressed == 's' or keyPressed == 'S'):
            clearScreen()
            displayText("Etch a Sketch", 40, 54)
        os.system("cls||clear")
        print("Etch a Sketch running, use arrow keys to draw, 's' to restart or 'q' to exit...")