import turtle as t


class Paddle(t.Turtle):

    def __init__(self, coor):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(coor)

    def go_up(self):
        new = self.ycor() + 20
        self.goto(self.xcor(), new)

    def go_dw(self):
        new = self.ycor() - 20
        self.goto(self.xcor(), new)
