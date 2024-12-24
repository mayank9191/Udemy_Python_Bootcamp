import turtle as t

kubri = t.Turtle()
screen = t.Screen()


def f():
    kubri.forward(5)


screen.listen()

# Here we are passing a function into another function by its name only here f -> lower order function and onkeypress() is High order function

screen.onkeypress(f, "Up")


screen.exitonclick()
