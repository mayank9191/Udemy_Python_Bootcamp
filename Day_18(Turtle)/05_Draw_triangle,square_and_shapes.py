import turtle as t
import random

kubri = t.Turtle()
kubri.pensize(10)
kubri.speed(0)

# dict = {"triangle": 3, "square": 4, "pentagon": 5, "hexagon": 6,
#         "heptagon": 7, "octagon": 8, "nonagon": 9, "decagon": 10}

# choice = input("Enter the shape which want to get: ").lower()
# n = dict[choice]

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

for i in range(3, 10):
    kubri.color(random.choice(colours))
    for j in range(i):
        kubri.fd(100)
        # kubri.left(180 - ((i-2)*180)/i)
        kubri.left(360/i)


screen = t.Screen()
screen.exitonclick()
