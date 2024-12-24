import turtle as t
import time
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.turtle = []
        for i in STARTING_POSITION:
            kubri = t.Turtle("square")
            kubri.penup()
            kubri.goto(i)
            kubri.color("white")
            kubri.speed(0)
            self.turtle.append(kubri)

    def move(self):
        for i in range(len(self.turtle)-1, 0, -1):
            self.turtle[i].goto(self.turtle[i-1].position())
        self.turtle[0].fd(20)

    def move_up(self):
        if (self.turtle[0].heading() != 270):
            self.turtle[0].setheading(90)

    def move_down(self):
        if (self.turtle[0].heading() != 90):
            self.turtle[0].setheading(270)

    def move_left(self):
        if (self.turtle[0].heading() != 0):
            self.turtle[0].setheading(180)

    def move_right(self):
        if (self.turtle[0].heading() != 180):
            self.turtle[0].setheading(0)
