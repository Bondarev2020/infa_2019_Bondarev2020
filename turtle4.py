import turtle

turtle.shape('turtle')
n=12
for i in range(n):
    turtle.forward(100)
    turtle.left(180)
    turtle.stamp()
    turtle.forward(100)
    turtle.left(180)
    turtle.left(360/n)

input()
turtle._root.mainloop()