import turtle


timmy = turtle.Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")

timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)
timmy.forward(100)
timmy.left(120)

my_screen = turtle.Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
