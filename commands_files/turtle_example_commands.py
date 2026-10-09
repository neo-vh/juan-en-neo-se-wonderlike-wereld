import turtle

def draw_square(size):

    if not type(size) == int:
        size = int(size)

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

def draw_triangle(size):

    if not type(size) == int:
        size = int(size)

    for _ in range(3):
        turtle.forward(size)
        turtle.right(-120)
