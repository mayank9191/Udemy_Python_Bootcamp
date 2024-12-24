def greet_with(name, location):
    print(f"Hello {name} sir")
    print(f"What is it like in {location}")


# positional argument
greet_with("Mayank", "Delhi")
# order will change in argument with change in input argument order
greet_with("Delhi", "Mayank")


# keyword argument
greet_with(name="Mayank", location="Delhi")
greet_with(location="Delhi", name="Mayank")
