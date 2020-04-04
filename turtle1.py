import turtle

def nugolnik(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.left(ugol)

turtle.shape('turtle')
nugolnik(3, 200, 90)


input()
turtle._root.mainloop()