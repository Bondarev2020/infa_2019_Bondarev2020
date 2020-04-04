import turtle
import math

def nugolnik(x):
    for i in range(x):
        sin=math.pi/x
        shag=1*x*2*math.sin(sin)
        s=180*(x-2)
        turtle.left(180-s/x)
        turtle.forward(shag)

def nugolnik1(x):
    for i in range(x):
        sin=math.pi/x
        shag=1*x*2*math.sin(sin)
        s=180*(x-2)
        turtle.right(180-s/x)
        turtle.forward(shag)


def otstup(t):
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()

turtle.shape('turtle')

b=30
turtle.left(90)
while b<=31:
    turtle.begin_fill()
    turtle.color("blue")
    nugolnik(b)
    turtle.end_fill()
    nugolnik1(b)
    b+=1

turtle._root.mainloop()