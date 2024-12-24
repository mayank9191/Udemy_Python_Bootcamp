import turtle as t


class ScoreBoard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.update()

    def update(self):
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left",
                   font=("Courier", 24, "normal"))

    def score_add(self):
        self.level += 1
        self.clear()
        self.update()

    def final(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=("Courier", 20, "normal"))
