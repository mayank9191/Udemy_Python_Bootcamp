print("Welcome to Python Deliveries!")

size = input("What size pizza do you want? S, M, L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if (size == "S"):
    bill += 15
    if (pepperoni == "Y"):
        bill += 2

    if (extra_cheese == "Y"):
        bill += 1

    print(f"You have to pay ${bill}")

elif (size == "M"):
    bill += 20
    if (pepperoni == "Y"):
        bill += 3

    if (extra_cheese == "Y"):
        bill += 1

    print(f"You have to pay ${bill}")

else:
    bill += 25
    if (pepperoni == "Y"):
        bill += 3

    if (extra_cheese == "Y"):
        bill += 1

    print(f"You have to pay ${bill}")
