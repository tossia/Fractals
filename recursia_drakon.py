import turtle
from math import sqrt
win = turtle.Screen()
turtle.speed('fastest')


def dragon_courve(n, l):
    right_move(n, l)


def right_move(n, l):
#    n -= 1
    l = sqrt((l ** 2) / 2)
    if n > 0:
        turtle.right(45)
        right_move(n - 1, l)
        turtle.left(90)
        left_move(n - 1, l)
        turtle.right(45)
    else:
        turtle.right(45)
        turtle.forward(l)
        turtle.left(90)
        turtle.forward(l)
        turtle.right(45)


def left_move(n, l):
#    n -= 1
    l = sqrt((l ** 2) / 2)

    if n > 0:
        turtle.left(45)
        right_move(n - 1, l)
        turtle.right(90)
        left_move(n - 1, l)
        turtle.left(45)
    else:
        turtle.left(45)
        turtle.forward(l)
        turtle.right(90)
        turtle.forward(l)
        turtle.left(45)


dragon_courve(5, 100)

win.mainloop()
