import turtle as t
import random


class Ball(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, -270)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move = -self.y_move
        self.x_move = -self.x_move

    def bounce1(self):
        self.y_move = -self.y_move
        self.x_move = self.x_move
