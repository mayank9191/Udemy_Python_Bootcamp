import turtle as t


class Score_board(t.Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.write(f"SCORE: {self.count}", False,
                   "center", ("Courier", 24, "normal"))

    def increase_score(self):
        self.count += 1
        self.clear()
        self.refresh()
