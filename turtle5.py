import turtle

turtle.shape('turtle')
n=1
while n<=100:
    turtle.forward(n)
    turtle.left(1)
    n+=0.01
input()
turtle._root.mainloop()