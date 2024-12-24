
logo = ''''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / /__\ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||___|    |___|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|


'''
print(logo)


def calc(first_number, symbol, next_number):
    if (symbol == "+"):
        answer = first_number + next_number
    elif (symbol == "-"):
        answer = first_number - next_number

    elif (symbol == "*"):
        answer = first_number * next_number
    else:
        answer = first_number / next_number

    print(f"{first_number} {symbol} {next_number} = {answer}")
    return answer


while (True):
    first_number = float(input("What's the first number?: "))

    while (True):
        symbol = input("+\n-\n*\n/\nPick an operation: ")

        next_number = float(input("What's the next number?: "))

        first_number = calc(first_number, symbol, next_number)

        futhur = input(
            f"Type 'y' to continue calculating with {first_number}, or type 'n' to start a new calculation: ").lower()

        if (futhur == "y"):
            continue

        else:
            break
