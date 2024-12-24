import turtle as t
from snake import Snake
from food import Food
from scoreboard import Score_board
import time


def game_over():
    text = t.Turtle()
    text.hideturtle()
    text.color("white")
    text.penup()
    text.write("Game Over.", False,
               "center", ("Courier", 24, "normal"))


screen = t.Screen()
screen.title("Snake Game")
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

# All the essential classes used
snake = Snake()
food = Food()
score_board = Score_board()

game_is_on = True
while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()     # Move the snake

# Detect food colision

    if (food.distance(snake.turtle[0]) < 15):
        food.refresh()
        score_board.increase_score()
        snake.add()

 # Detect wall colision

    if ((snake.turtle[0].xcor() > 296 or snake.turtle[0].ycor() > 296) or (snake.turtle[0].xcor() < -296 or snake.turtle[0].ycor() < -296)):
        game_over()
        game_is_on = False

 # Detect body collision

    for i in snake.turtle[1:]:
        if (snake.turtle[0].distance(i) < 15):
            game_over()
            game_is_on = False

 # Take input from user

    screen.listen()
    screen.onkeypress(snake.move_up, "Up")
    screen.onkeypress(snake.move_down, "Down")
    screen.onkeypress(snake.move_left, "Left")
    screen.onkeypress(snake.move_right, "Right")


screen.exitonclick()
