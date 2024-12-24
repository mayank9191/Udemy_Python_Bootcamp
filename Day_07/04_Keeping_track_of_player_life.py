import random

states = ['''+---+
|   |
    | 
    |
    |
    |
=========''', '''+---+
|   |
O   |
    |
    |
    |
=========''', '''+---+
|   |
O   |
|   |
    |
    |
=========''', ''' +---+
 |   |
 O   |
/|   |
     |
     |
=========''', ''' +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', ''' +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''']

word_list = ["aardvark", "baboon", "camel"]

# TODO-1: Create a variable called "Lives" to keep track of the player lifes
# Set "Lives" to equal 6

chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while (not game_over):
    guess = input("Guess a letter: ").lower()

    display = ""

    for word in chosen_word:
        if (guess == word):
            display += guess
            correct_letters.append(guess)

        elif (word in correct_letters):
            display += word

        else:
            display += "_"

    print(display)

# TODO-2: If guess is not a letter in the chosen_word, then lower a life by 1
# If lives goes down to 0 then the game should stop and it shows you lose!

    if (guess not in chosen_word):
        lives -= 1
        if (lives == 0):
            print("You lose!")
            break
        print(states[6 - lives])

    else:
        print(states[6-lives])

    print(lives)

    if ("_" not in display):
        game_over = True
        print("You win!")
