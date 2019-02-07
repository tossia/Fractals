from tkinter import *
import math


def dragon(canv, x1, y1, x2, y2, n):
  if n:
    dx = (x2 - x1) / 4
    dy = (y2 - y1) / 4
    x3 = x1 + dx + dy
    y3 = y1 + dy - dx
    x4 = x2 - dx - dy
    y4 = y2 - dy + dx
    dragon(canv, x1, y1, x3, y3, n-1)
    dragon(canv, x3, y3, x4, y4, n-1)
    dragon(canv, x4, y4, x2, y2, n-1)
  else:
    canv.create_line(x1, y1, x2, y2, width=0.3, fill='blue')


root = Tk()
root.title("Dragon Koch plot")
root.geometry('1000x600')

canv = Canvas(root, width=1000, height=600, bg='white')

N = 12
dragon(canv, 100, 300, 900, 300, N)

canv.pack()
root.mainloop()
