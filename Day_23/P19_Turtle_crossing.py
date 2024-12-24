import turtle as t
import random
import time
from player import Player
from car import CarManager
from score_board import ScoreBoard

screen = t.Screen()
screen.setup(600, 600)
screen.tracer(0)


def dine():
    r = random.randint(-300, 300)
    e = t.Turtle("square")
    e.penup()
    e.goto(300, r)
    e.setheading(180)
    e.fd(30)


tur = Player()
car = CarManager()
score = ScoreBoard()

while (True):
    time.sleep(0.1)
    screen.update()

    car.create_cars()

    car.move_cars()

    if (tur.ycor() > 280):
        score.score_add()
        car.distance += 10
        tur.goto(0, -280)

    elif (car.check_collide(tur) == 1):
        score.final()
        break
    screen.listen()
    screen.onkeypress(tur.up, "Up")


screen.exitonclick()
