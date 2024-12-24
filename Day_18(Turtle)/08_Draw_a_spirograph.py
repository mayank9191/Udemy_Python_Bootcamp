import turtle as t
import random

kubri = t.Turtle()
kubri.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def draw_spirograph(size):
    for i in range(int(360 / size)):
        # kubri.forward(0.1)
        # kubri.left(4)
        kubri.color(random_color())
        kubri.circle(100)
        kubri.setheading(kubri.heading() + size)


draw_spirograph(10)
screen = t.Screen()
screen.exitonclick()
