alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i",    "j",     "k",
         "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print('''
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88
            88             88
           ""             88
                          88
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8
8b         88 88       d8 88       88 8PP""""""" 88
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88
              88
              88  ''')


def cpher(alpha, choice, message, shift_no):
    result = ""
    shift_no %= len(alpha)
    if (choice == "decode"):
        shift_no *= -1
    for i in message:
        if (i in alpha):
            n = alpha.index(i)
            find = n + shift_no
            result += alpha[find]

        else:
            result += i

    print(f"Here's the {choice}d result: {result}")


while (True):
    choice = input(
        "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    message = input("Type your message: \n").lower()

    shift_no = int(input("Type the shift number: \n"))

    cpher(alpha, choice, message, shift_no)

    again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if (again == "no"):
        print("GoodBye!")
        break
