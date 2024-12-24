print("Hello World")  # built-in functions in python

num_char = len("hello")
print(num_char)


# self made function
def is_prime(n):
    count = 0

    if n <= 1:
        print(f"{n} is not a prime number.")
        return

    for i in range(1, n+1):
        if (n % i == 0):
            count += 1

    if (count > 2):
        print(f"{n} is not a prime number.")

    else:
        print(f"{n} is a prime number.")


n = int(input("Enter your Number: "))
is_prime(n)  # calling a function


# All the parts are done as a challenge in reeborg game by python implementing while loop and functions
