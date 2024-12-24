MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18
        },
        "cost": 1.5
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24
        },
        "cost": 3.0
    }
}

resources = {
    "water": 250,
    "milk": 150,
    "coffee": 24,
    "money": 0
}


def check_ingredient(ingredient_item):
    """Returns True when order can be made, False if ingredients are insufficient."""
    can_make = False
    for item in ingredient_item:
        if (ingredient_item[item] > resources[item]):
            print(f"Sorry there is not enough {item}")
            can_make = True
    return can_make


def take_money():
    """Returns the total calculated from coins inserted."""
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickels?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01

    return total


def check_money_sufficient(m, c):
    """Returns True when the payment is accepted, or False if mone is insufficient."""
    if (m < c):
        print(f"Sorry! ${m:.2f} is not enough money. Money refunded")
        return False

    elif (m > c):
        print(f"Here is ${round(m - c, 2)} in change")
        return True


while (True):
    choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()

    if (choice == "off"):
        print("The coffee maker isn't operational at the moment.")
        break

    if (choice == "report"):
        print(f'''Water: {resources["water"]}ml\nMilk: {
              resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}''')
        continue
    if (choice in MENU):
        drink = MENU[choice]
        if (check_ingredient(drink["ingredients"])):
            continue

        else:
            print("Please insert coins.")
            money = take_money()
            if (check_money_sufficient(money, drink["cost"])):
                resources["water"] -= drink["ingredients"]["water"]
                if "milk" in drink["ingredients"]:
                    resources["milk"] -= drink["ingredients"].get(
                        "milk")
                resources["coffee"] -= drink["ingredients"]["coffee"]
                resources["money"] += drink["cost"]
                print(f"Here is your {choice} ☕ Enjoy😊!")
    else:
        print("Unfortunately, we don’t serve that. Please select a different drink.")
