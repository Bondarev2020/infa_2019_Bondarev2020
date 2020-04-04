import turtle
import math

def nugolnik(x, shag):
    for i in range(x):
        sin=math.pi/x
        shag=10*x*2*math.sin(sin)
        s=180*(x-2)
        turtle.left(180-s/x)
        turtle.forward(shag)

nugolnik(x, shag)