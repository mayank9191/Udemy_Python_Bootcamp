import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "display" with the same number of blanks as the choosen_word


placeholder = "_" * len(chosen_word)
print(placeholder)

guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in unmatched positions

display = ""
for word in chosen_word:
    if (guess == word):
        display += guess

    else:
        display += "_"

print(display)
