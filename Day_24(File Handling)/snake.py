import turtle as t
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtle = []
        for i in STARTING_POSITION:
            self.kubri = t.Turtle("square")
            self.kubri.penup()
            self.kubri.goto(i)
            self.kubri.color("lime green")
            self.kubri.speed(0)
            self.turtle.append(self.kubri)

    def add(self):
        kubri = t.Turtle("square")
        kubri.penup()
        kubri.goto(self.turtle[-1].pos())
        kubri.color("lime green")
        kubri.speed(0)
        self.turtle.append(kubri)

    def move(self):
        for i in range(len(self.turtle)-1, 0, -1):
            self.turtle[i].goto(self.turtle[i-1].position())
        self.turtle[0].fd(MOVE_DISTANCE)

    def move_up(self):
        if (self.turtle[0].heading() != DOWN):
            self.turtle[0].setheading(90)

    def move_down(self):
        if (self.turtle[0].heading() != UP):
            self.turtle[0].setheading(270)

    def move_left(self):
        if (self.turtle[0].heading() != RIGHT):
            self.turtle[0].setheading(180)

    def move_right(self):
        if (self.turtle[0].heading() != LEFT):
            self.turtle[0].setheading(0)

    def reset(self):
        for seg in self.turtle:
            seg.goto(1000, 1000)
        self.turtle.clear()
        self.turtle = []
        for i in STARTING_POSITION:
            self.kubri = t.Turtle("square")
            self.kubri.penup()
            self.kubri.goto(i)
            self.kubri.color("lime green")
            self.kubri.speed(0)
            self.turtle.append(self.kubri)
