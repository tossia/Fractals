import turtle
turtle.speed('fastest')
turtle.left(180)
turtle.penup()
turtle.forward(300)
turtle.right(180)
turtle.pendown()
win = turtle.Screen()

def koch(l, n):
    if n == 0:
        turtle.forward(l)
        return
    l //= 3
    koch(l, n - 1)
    turtle.left(60)
    koch(l, n - 1)
    turtle.right(120)
    koch(l, n - 1)
    turtle.left(60)
    koch(l, n - 1)
        

def floc_koch(l, n):
    for i in range(6):
        koch(l, n)
        turtle.right(60)

floc_koch(100, 3)
win.mainloop()