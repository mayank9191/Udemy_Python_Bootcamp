import turtle as t


class Player(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(0, -280)
        self.setheading(90)

    def up(self):
        self.fd(10)
