import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/
                   ''')
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

word_list = ["Elegant",
             "Whisper",
             "Harmony",
             "Journey",
             "Twilight",
             "Mystery",
             "Courage",
             "Passion",
             "Victory",
             "Destiny"]


chosen_word = random.choice(word_list)
print(chosen_word)

lives = 6

placeholder = "_" * len(chosen_word)
print(placeholder)

game_over = False
correct_letters = []

while (not game_over):

    print(
        f"****************************{lives}/6 LIVES LEFT****************************")

    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display = ""

    for word in chosen_word:
        if (guess == word):
            display += guess
            correct_letters.append(guess)

        elif (word in correct_letters):
            display += word

        else:
            display += "_"

    print("Word to guess: " + display)

    if (guess not in chosen_word):
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if (lives == 0):
            print(f"****************************Its was {
                  chosen_word}!YOU LOSE!****************************")
            break
        print(states[6 - lives])

    else:
        print(states[6-lives])

    print(lives)

    if ("_" not in display):
        game_over = True
        print(
            "****************************YOU WIN!****************************")
