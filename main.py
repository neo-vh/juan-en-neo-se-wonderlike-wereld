import turtle


t = turtle.Turtle()
screen = turtle.Screen()

def make_shape():
    t.color("black")

    for i in range(100):
        t.forward(100 + 1)
        t.left(50 + 1)

make_shape() 