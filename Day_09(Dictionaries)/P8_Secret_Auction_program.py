import os

logo = '''

                         -----------
                         \         /
                          )-------(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |-------| '-'`'----------'` '-'
                          )"""""""(
                         /---------\\
                        .-----------.
                       /-------------\\
'''

print(logo)
bid_dict = {}
while (True):
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))

    bid_dict[name] = bid

    futher = input(
        "Are there any other bidders? Type 'yes or 'no'.\n ").lower()

    if (futher == "yes"):

        os.system("cls")
        continue

    else:
        name = ""
        count = 0
        for key, value in bid_dict.items():
            if (count < value):
                count = value
                name = key

        print(f"The winner is {name} with a bid of ${count}")

        break
