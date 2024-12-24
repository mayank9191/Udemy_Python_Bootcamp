import turtle as t
import random
import time
from paddle import Paddle
from score_board import Score
from ball import Ball

screen = t.Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.mode("standard")
screen.tracer(0)

count = 0


line = t.Turtle()
line.speed(0)
line.goto(0, -300)
line.setheading(90)
line.color("white")
line.pensize(5)
line.hideturtle()

for i in range(20):
    line.fd(15)
    line.penup()
    line.fd(15)
    line.pendown()

left_player = Paddle((-350, 0))
right_player = Paddle((350, 0))

score = Score()
ball = Ball()


while (True):
    screen.update()
    time.sleep(0.05)

    right_screen_heading = random.randint(-75, -55)
    left_screen_heading = random.randint(235, 260)

    if (ball.xcor() < -390 or ball.xcor() > 390):
        score.final()
        break

    elif (left_player.distance(ball) < 35 and ball.xcor() < -330):
        ball.bounce()
        score.left_score_add()

    elif (right_player.distance(ball) < 35 and ball.xcor() > 330):
        ball.bounce()
        score.right_score_add()

    elif (ball.ycor() < -270 or ball.ycor() > 270):
        ball.bounce1()

    ball.move()

    screen.listen()
    screen.onkeypress(left_player.go_up, "w")
    screen.onkeypress(left_player.go_dw, "s")
    screen.onkeypress(right_player.go_up, "Up")
    screen.onkeypress(right_player.go_dw, "Down")


screen.exitonclick()
