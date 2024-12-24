import turtle as t
import random

# used colorgram module to extract image color into a tuple of rgb as a list

color_list = [(254, 253, 249), (248, 254, 252), (254, 249, 253), (247, 28, 152), (236, 137, 31), (93, 192, 243), (248, 238, 57), (240, 247, 251), (3, 38, 77), (123, 7, 183), (8, 127, 47), (77, 188, 174), (159, 203, 34), (196, 36, 181),
              (69, 181, 165), (212, 126, 190), (5, 119, 42), (237, 160, 212), (79, 95, 115), (160, 209, 195), (180, 110, 58), (150, 203, 227), (45, 63, 87), (115, 125, 151), (179, 190, 215), (237, 177, 156), (164, 217, 36), (79, 144, 166), (168, 119, 89)]

screen = t.Screen()
kubri = t.Turtle()
t.colormode(255)
kubri.speed(0)
kubri.penup()
kubri.hideturtle()
kubri.speed(0)


def draw():
    for i in range(13):
        kubri.dot(20, random.choice(color_list))
        kubri.forward(50)


kubri.setheading(220)

for i in range(8):
    kubri.forward(50)

kubri.left(140)
for i in range(14):
    draw()
    kubri.left(176.6)
    kubri.penup()
    kubri.fd(651)
    kubri.left(183.4)


screen.exitonclick()
