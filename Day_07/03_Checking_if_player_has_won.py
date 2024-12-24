import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = "_" * len(chosen_word)
print(placeholder)

# TODO-1: Use a while loop to let the user guess again.


game_over = False
correct_letters = []

while (not game_over):
    guess = input("Guess a letter: ").lower()

    display = ""

# TODO-2: Change the for loop so that you keep the previous correct letter in display

    for word in chosen_word:
        if (guess == word):
            display += guess
            correct_letters.append(guess)

        elif (word in correct_letters):
            display += word

        else:
            display += "_"

    print(display)

    if ("_" not in display):
        game_over = True

        print("You win!")
