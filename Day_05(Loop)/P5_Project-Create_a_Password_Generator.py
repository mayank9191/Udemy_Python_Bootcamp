import random
from charater import alphabets, symbols, numbers


print("Welcome to the PyPassword Generator!")

a = int(input("How many alphabets would you like?\n"))

b = int(input("How many symbols would you like?\n"))

c = int(input("How many numbers would you like?\n"))


password = []

for i in range(a):
    password.append(random.choice(alphabets))

for i in range(b):
    password.append(random.choice(symbols))

for i in range(c):
    password.append(random.choice(numbers))

print(password)
random.shuffle(password)
print(password)

final = "".join(password)

print(f"Your password is: {final}")
