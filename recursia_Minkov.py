import turtle
# turtle.speed('fastest')
turtle.left(180)
turtle.penup()
turtle.forward(200)
turtle.right(180)
turtle.pendown()
win = turtle.Screen()

def minkovsky(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 8
    minkovsky(l, n - 1)
    turtle.left(90)
    minkovsky(l, n - 1)
    turtle.right(90)
    minkovsky(l, n - 1)
    turtle.right(90)
    minkovsky(l, n - 1)
    minkovsky(l, n - 1)
    turtle.left(90)
    minkovsky(l, n - 1)
    turtle.left(90)
    minkovsky(l, n - 1)
    turtle.right(90)
    minkovsky(l, n - 1)


minkovsky(2000, 3)
win.mainloop()
