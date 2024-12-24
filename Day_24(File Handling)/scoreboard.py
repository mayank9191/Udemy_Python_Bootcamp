import turtle as t


class Score_board(t.Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        # Saving high score in separate file
        with open("Day_24\high_score.txt", "r") as f:
            self.high_score = int(f.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"SCORE: {self.count} High Score: {self.high_score}", False,
                   "center", ("Courier", 24, "normal"))

    def increase_score(self):
        self.count += 1
        self.refresh()

    def reset(self):
        if (self.count > self.high_score):
            self.high_score = self.count
            with open("Day_24\high_score.txt", "w") as f:
                f.write(str(self.count))
        self.count = 0
        self.refresh()
