import turtle as t


class Score(t.Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.update()

    def update(self):
        self.goto(-100, 200)
        self.write(f"{self.left_score}",
                   align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(f"{self.right_score}",
                   align="center", font=("Courier", 80, "normal"))

    def left_score_add(self):
        self.clear()
        self.left_score += 1
        self.update()

    def right_score_add(self):
        self.clear()
        self.right_score += 1
        self.update()

    def final(self):
        self.goto(0, 0)
        self.write("Game   Over!", False, "center", ("arial", 20, "normal"))
