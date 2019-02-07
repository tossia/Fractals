"""Pseudocode
Function (left_point, right_point) 
    Нарисовать линию от левой до правой точки
    Переместиться на следующий уровень
    Рассчитать разницу между правой и левой точками
    Нарисовать линию от левой точки до 1/3 от общей длины основной линии
    Вызвать функцию (левая точка, левая точка + 1/3 общей длины)
    Нарисовать линию от левой точки + 2/3 от общей длины
    Вызвать фукцию (левая точка + 2/3 от общей длины, правая точка)
"""

import turtle
# turtle.speed('fastest')
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
