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
    l //= 8
    Koch_Line(l, n - 1)
    turtle.left(90)
    Koch_Line(l, n - 1)
    turtle.right(90)
    Koch_Line(l, n - 1)
    turtle.right(90)
    Koch_Line(l, n - 1)
    Koch_Line(l, n - 1)
    turtle.left(90)
    Koch_Line(l, n - 1)
    turtle.left(90)
    Koch_Line(l, n - 1)
    turtle.right(90)
    Koch_Line(l, n - 1)

Koch_Line(10000, 3)
turtle.mainloop()










            




