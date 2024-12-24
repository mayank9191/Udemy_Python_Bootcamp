import turtle as t
import random

kubri = t.Turtle()
kubri.shape("circle")
kubri.pensize(10)
kubri.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


while (True):
    kubri.color(random_color())
    kubri.forward(30)
    # angle = random.randint(1, 5) * 90
    angle = random.choice([0, 90, 180,  270])
    kubri.setheading(angle)
