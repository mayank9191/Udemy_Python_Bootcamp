import turtle as t
import pandas

n = 0

screen = t.Screen()
screen.setup(725, 491)
screen.bgpic(r"Day_25\blank_states_img.gif")


data = pandas.read_csv("Day_25/50_states.csv")
dict_data = data.to_dict()

pen = t.Turtle()
pen.hideturtle()
pen.penup()

all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    guess = screen.textinput(title=f"{n}/50 States Correct",
                             prompt="What's another state name?").title()
    if (guess == "Exit"):
        not_guessed = [i for i in all_states if i not in guessed_states]
        print(not_guessed)
        states_to_learn = pandas.DataFrame(not_guessed)
        states_to_learn.to_csv("Day_25/states_to_learn.csv")
        break

    for i in range(0, 50):
        if (dict_data["state"][i] == guess):
            n += 1
            guessed_states.append(guess)
            pen.goto(dict_data["x"][i], dict_data["y"][i])
            pen.write(f"{dict_data["state"][i]}")

screen.exitonclick()
