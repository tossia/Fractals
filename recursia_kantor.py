"""Pseudocode
Function (left_point, right_point) 
Draw a line from left to right point -                      Нарисовать линию от левой до правой точки
Move to next level -                                        Переместиться на следующий уровень
Calculate the difference between right and left points      Рассчитать разницу между правой и левой точками
Draw a line fron left point till 1/3 of full length -       Нарисовать линию от левой точки до 1/3 от общей длины основной линии
Call the function (left point, left point + 1/3 full length Вызвать функцию (левая точка, левая точка + 1/3 общей длины)
Draw a line from left point + 2/3 full length               Нарисовать линию от левой точки + 2/3 от общей длины
Call the function (left point + 2/3 full length, right point)Вызвать фукцию (левая точка + 2/3 от общей длины, правая точка)
"""

import turtle
# turtle.speed('fastest') - an option to move the turtle as crasy turtle
win = turtle.Screen()

l = 500
n = 5
x = 0
y = 0


def kantor(l, n, x, y):
    if n == 0:
        turtle.forward(l)
        return
    else:
        turtle.forward(l)
        turtle.penup()
        y -= 20
        turtle.goto(x, y)
        turtle.pendown()
        l //= 3
        kantor(l, n - 1, x, y)
        turtle.penup()
        x += (l * 2)
        turtle.goto(x, y)
        turtle.pendown()
        kantor(l, n - 1, x, y)


kantor(l, n, x, y)

turtle.penup()
turtle.goto(0, 0)
win.mainloop()
