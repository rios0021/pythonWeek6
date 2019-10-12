# Function that displays an object represented as a tuple or a list on the gfxhat at position x,y
# Input: obj(tuple/list), x(int), y(int)
# Output: none
def displayObject(obj,x,y):
    from gfxhat import lcd
    # While loop to translate any entered number into a existing space in the gfxhat display
    while(x < 0 or y < 0 or x > 127 or y > 63):
        if(x < 0):
            x = 128+x
        if(y < 0):
            y = 64+y
        if(x > 127):
            x = x-128
        if(y > 63):
            y = y-63
    navX = x
    navY = y
    for aux in obj:
        for aux2 in aux:
            if(aux2 == 1):
                lcd.set_pixel(navX,navY,1)
                lcd.show()
            navX += 1
            if(navX > 127):
                navX = 0
        navY += 1
        if(navY > 63):
            navY = 0
        navX = x

f1 =  [
[1,1,1,1,1,1,1,1],
[1,1,1,1,1,1,1,1],
[0,1,1,1,1,1,1,0],
[1,0,1,1,1,1,0,1],
[1,0,0,1,1,0,0,1],
[1,0,0,1,1,0,0,1],
[0,0,0,1,1,0,0,0],
[0,0,0,0,0,0,0,0]
]

pm = [[0,0,0,1,1,1,1,1,0,0,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[1,1,1,1,1,1,1,1,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,0,0,0,0,0],
[1,1,1,1,1,1,1,0,0,0,0],
[1,1,1,1,1,1,1,1,0,0,0],
[0,1,1,1,1,1,1,1,1,1,0],
[0,0,1,1,1,1,1,1,1,0,0],
[0,0,0,1,1,1,1,1,0,0,0]
]
obj = 0
print("Welcome to the object drawing program")
while(obj !=  "1" and obj != "2"):
    obj = input("Select 1 for the ship or 2 for pacman: ")
    if (obj !=  "1" and obj != "2"):
        print("Please enter a valid option!")
x = int(input("Please enter x coordinate of the gfxhat to start drawing: "))
y = int(input("Please enter y coordinate of the gfxhat to start drawing: "))
if (obj== "1"):
    displayObject(f1,x,y)
else:
    displayObject(pm,x,y)

