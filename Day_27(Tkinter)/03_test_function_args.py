# Unlimited Positional Arguments
# here *args can take any number of positional argument as tuple

def add(*args):
    sum = 0
    for n in args:
        sum += n

    print(f"Sum: {sum}")


add(3, 3, 3, 35, 5, 67, 8)

# Unlimited Keyword argument
# here **kwargs can take any number of keyword arguments as dictionaries


def calculate(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)


calculate(2, add=3, multiply=4)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        # self.model = kw["model"]
        # get is used to fetch dict value if not there return none
        self.model = kw.get("model")
        self.colour = kw.get("colour")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="GT-R")

print(my_car.make)
print(my_car.model)
print(my_car.colour)
