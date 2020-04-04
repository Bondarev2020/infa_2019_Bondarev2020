import turtle

def nugolnik(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.left(ugol)
def nugolnik1(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.right(ugol)

turtle.shape('turtle')
i=1
while i<=3:
    nugolnik(36, 10, 10)
    nugolnik1(36, 10, 10)
    turtle.left(60)
    i+=1

input()
turtle._root.mainloop()