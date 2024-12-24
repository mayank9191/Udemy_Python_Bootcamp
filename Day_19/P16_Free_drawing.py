import turtle as t

kubri = t.Turtle()
screen = t.Screen()


def forward():
    kubri.forward(10)


def backward():
    kubri.back(10)


def counter_clockwise():
    new_heading = kubri.heading() + 10
    kubri.setheading(new_heading)


def clockwise():
    new_heading = kubri.heading() - 10
    kubri.setheading(new_heading)


def clear():
    kubri.clear()
    kubri.penup()
    kubri.home()
    kubri.pendown()


screen.listen()

screen.onkeypress(forward, "w")
screen.onkeypress(backward, "s")
screen.onkeypress(counter_clockwise, "a")
screen.onkeypress(clockwise, "d")
screen.onkeypress(clear, "c")


screen.exitonclick()
