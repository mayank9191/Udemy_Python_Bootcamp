import turtle as t
import random

screen = t.Screen()
screen.setup(width=500, height=400)


user_bet = screen.textinput(title="Make your Bet",
                            prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)


colors = ["purple", "blue", "green", "yellow", "orange", "red"]
y_position = [67, 40.4, 13.8, -12.8, -39.4, -67]

turtle_name = ["kubri", "tim", "rony", "rook", "wrath", "sam"]
for i in range(6):
    turtle_name[i] = t.Turtle()
    turtle_name[i].penup()
    turtle_name[i].shape("turtle")
    turtle_name[i].color(colors[i])
    turtle_name[i].goto(-230, y_position[i])
    turtle_name[i].speed(0)

line = t.Turtle()
line.hideturtle()
line.color("red")
line.penup()
line.goto(237, 100)
line.pendown()
line.pensize(5)
line.setheading(270)
line.fd(200)
is_on = True
while (is_on):
    for i in range(6):
        turtle_name[i].fd(random.randint(0, 10))
        if (turtle_name[i].xcor() > 220):
            is_on = False
            print(f"{colors[i]} turtle wins the game!")
            if (colors[i] == user_bet):
                print(f"You've won! The {colors[i]} turtle is the winner!")
            else:
                print(f"You've lost! The {colors[i]} turtle is the winner!")
            break

screen.exitonclick()
