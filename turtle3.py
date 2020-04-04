import turtle

def nugolnik(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.left(ugol)

def otstup():
    turtle.penup()
    turtle.left(180)
    turtle.forward(a/2)
    turtle.left(90)
    turtle.forward(a/2)
    turtle.left(90)
    turtle.pendown()

turtle.shape('turtle')
c=10
b=1
a=36
while b<=c:
    nugolnik(4, a*b, 90)
    otstup()
    b+=1
input()
turtle._root.mainloop()