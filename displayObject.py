# Function that displays an object represented as a tuple or a list on the gfxhat at position x,y
# Input: obj(tuple/list), x(int), y(int)
# Output: none
def displayObject(obj,x,y):
    from gfxhat import lcd
    if(x < 0):
        x = 128+x
    if(y < 0):
        y = 64+y
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

displayObject(pm, 64,-4)