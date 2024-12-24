import turtle as t
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.distance = 20

    def create_cars(self):
        random_chance = random.randint(1, 5)
        if (random_chance == 1):
            new_car = t.Turtle("square")
            new_car.shapesize(1, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(300, random.randint(-250, 250))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.distance)

    def check_collide(self, x):
        for car in self.all_cars:
            if (car.distance(x) < 20):
                return 1
