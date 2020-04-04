from graph import *
def update():
    moveObjectBy(obj, 5, 0)
    if xCoord(obj) >= 380:
        close()
def update1():
    moveObjectBy(obj, 0, 5)
    if xCoord(obj) >= 380:
        close()  
def keyPressed(event):
    if event.keycode == VK_ESCAPE:
        close()
    if event.keycode == VK_XBUTTON1:
        close()
windowSize(500, 500)
canvasSize(500, 500)
brushColor("blue")
rectangle(0, 0, 400, 400)
x=100
y=100
penColor("yellow")
brushColor("green")
obj = rectangle(x, y, x+20, y+20)
onTimer(update, 50) 
onKey (keyPressed)
run()






