import turtle

turtle.speed('fastest')
koch_flake = "FRFRF"
iterations = 5

for i in range(iterations):
    koch_flake = koch_flake.replace("F", "FLFRFLF")

turtle.down()

for move in koch_flake:
    if move == "F":
        turtle.forward(100.0 / (3 ** (iterations - 1)))
    elif move == "L":
        turtle.left(60)
    elif move == "R":
        turtle.right(120)
