import turtle
from math import sqrt
turtle.speed('fastest')
win = turtle.Screen()

def courbe_levi(l, n):
    if n == 0:
        turtle.forward(l)
    else:
        l = sqrt((l ** 2) / 2)
        turtle.left(45)
        courbe_levi(l, n - 1)
        turtle.right(90)
        courbe_levi(l, n - 1)
        turtle.left(45)

l = 300
n = 4
courbe_levi(l, n)
win.mainloop()
