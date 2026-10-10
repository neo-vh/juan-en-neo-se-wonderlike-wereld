import turtle, time

# Currently only works once for each draw (might only be for square), these are test commands and will be removed


def _open_screen():
    screen = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True
    return screen

def draw_square(size):

    if not type(size) == int:
        size = int(size)

    screen = _open_screen()

    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)

    time.sleep(3)
    screen.bye()

def draw_triangle(size):

    if not type(size) == int:
        size = int(size)

    screen = _open_screen()

    for _ in range(3):
        turtle.forward(size)
        turtle.right(-120)

    time.sleep(3)
    screen.bye()
    #retard     

    # neo n bitch 
