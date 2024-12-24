import P903_Calculator_Proj_mine as mine


def add(n1, n2):
    return n1 + n2


def substract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}


def calculator():
    print(mine.logo)
    n1 = float(input("What's the first number?: "))
    should_accumulate = True
    while (should_accumulate):
        operation_symbol = input("+\n-\n*\n/\nPick an operation: ")
        n2 = float(input("What's the next number?: "))

        result = operations[operation_symbol](n1, n2)
        print(f"{n1} {operation_symbol} {n2} = {result}")
        futhur = input(f"Type 'y' to continue calculating with {
                       result}, or type 'n' to start a new calculation: ").lower()

        if (futhur == "y"):
            n1 = result

        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()
