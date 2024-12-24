import random

logo = '''
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|    
'''


def check(a):
    if (a == 0):
        print(f"You've run out of guesses number was {random_no}, you lose.")
        return True
    return False


print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random_no = random.randint(1, 100)

if (level == "easy"):
    attempts = 10
    print("You have 10 attempts remaining to guess the number.")

else:
    attempts = 5
    print("You have 5 attempts remaining to guess the number.")

while attempts > 0:
    guess = int(input("Make a guess: "))
    attempts -= 1
    if (guess < random_no):
        if (check(attempts)):
            break
        print(f'''Too low.\nGuess again\nYou have {
              attempts} attempts remaining to guess the number.''')
    elif (guess > random_no):
        if (check(attempts)):
            break
        print(f'''Too high.\nGuess again\nYou have {
              attempts} attempts remaining to guess the number.''')
    else:
        print(f"You got it! The answer was {random_no}.")
        break
