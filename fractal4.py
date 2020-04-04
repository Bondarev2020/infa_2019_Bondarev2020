import turtle

turtle.shape('turtle')
turtle.penup()
turtle.goto(-200, 0)
turtle.pendown()


def levi (l, n):
    if n == 0:
        turtle.forward(l)

        return
    l //= 1.7
    turtle.left(45)
    levi(l, n - 1)
    turtle.right(90)
    levi(l, n - 1)
    turtle.left(45)
levi (5000, 10)
turtle.mainloop()










            




