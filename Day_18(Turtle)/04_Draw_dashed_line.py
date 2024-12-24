import turtle as t

kubri = t.Turtle()

kubri.shape("turtle")
kubri.color("red")


def dash():
    for i in range(10):
        kubri.forward(5)
        kubri.penup()
        kubri.forward(5)
        kubri.pendown()


dash()

screen = t.Screen()
screen.exitonclick()
