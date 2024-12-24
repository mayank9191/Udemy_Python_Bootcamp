import turtle as t
import random

screen = t.Screen()
screen.setup(600, 600)
screen.tracer(0)


class Food:
    def __init__(self):
        self = t.Turtle("circle")
        self.color("blue")
        self.penup()
        self.goto(random.randint(-300, 300), random.randint(-300, 300))
        screen.update()


# while (True):
#     food = Food()
# screen.exitonclick()
