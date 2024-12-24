import random

# generates a random integer between given range a <= N <= b
# random_integer = random.randint(1, 100)
# print(random_integer)

# generates a random floating number 0.0 <= X < 1.0
# random_float_0_to_1 = random.random()*10
# print(random_float_0_to_1)

random_heads_tails = random.randint(0, 1)

if (random_heads_tails == 1):
    print("Heads")

else:
    print("Tails")
