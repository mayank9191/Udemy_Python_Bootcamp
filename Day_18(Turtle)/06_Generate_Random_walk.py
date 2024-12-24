import turtle as t
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed",
           "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

kubri = t.Turtle()
kubri.shape("circle")
kubri.pensize(10)
kubri.speed(0)

while (True):
    kubri.color(random.choice(colours))
    kubri.forward(30)
    # angle = random.randint(1, 5) * 90
    angle = random.choice([0, 90, 180,  270])

    kubri.setheading(angle)
