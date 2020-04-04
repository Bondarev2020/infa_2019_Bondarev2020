import turtle
import math

def nugolnik(x):
    for i in range(x):
        sin=math.pi/x
        shag=10*x*2*math.sin(sin)
        s=180*(x-2)
        turtle.left(180-s/x)
        turtle.forward(shag)

def otstup(t):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.shape('turtle')

b=3
while b<=20:
    s=180*(b-2)
    turtle.left((s/b)/2)
    nugolnik(b)
    turtle.right((s/b)/2)
    otstup(b)  
    b+=1

turtle._root.mainloop()