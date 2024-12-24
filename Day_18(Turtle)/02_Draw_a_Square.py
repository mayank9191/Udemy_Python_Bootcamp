from turtle import Turtle, Screen

kubri = Turtle()

kubri.shape("turtle")
kubri.color("red")

for i in range(4):
    kubri.forward(100)
    kubri.right(90)


screen = Screen()
screen.exitonclick()
