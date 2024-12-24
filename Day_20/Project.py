import turtle as t
from snake import Snake
from food import Food
import time

screen = t.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.move_left, "Left")
    screen.onkeypress(snake.move_right, "Right")

screen.exitonclick()
