import turtle

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def Koch_Line(l, n):

    if n == 0:

        turtle.forward(l)
        return
    turtle.speed('fastest')
    l //= 3
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)
    turtle.right(120)
    Koch_Line(l, n - 1)
    turtle.left(60)
    Koch_Line(l, n - 1)
turtle.color("yellow")
turtle.fillcolor("blue")
turtle.begin_fill()
for i in range(3):
    Koch_Line(400, 3)
    turtle.right(120)
turtle.end_fill()






            




