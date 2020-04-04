import turtle

def nugolnik(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.left(ugol)
def nugolnik1(x, shag, ugol):
    for i in range(x):
        turtle.forward(shag)
        turtle.left(ugol)

turtle.shape('turtle')
i=1
turtle.left(90)
while i<=3:
    nugolnik(18, 10, 10)
    nugolnik1(18, 1, 10)
    i+=1

input()
turtle._root.mainloop()