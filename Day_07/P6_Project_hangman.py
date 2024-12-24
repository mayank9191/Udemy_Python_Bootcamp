import random
random_words = ["Elegant",
                "Whisper",
                "Harmony",
                "Journey",
                "Twilight",
                "Mystery",
                "Courage",
                "Passion",
                "Victory",
                "Destiny"]

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


word = random.choice(random_words).lower()
l = len(word)
dash = "_" * l

n = 6
w = 0
while (n > 0):
    print(f"Word to guess: {dash}")
    let = input("Guess a leter:")

    if (let in word):
        dash = list(dash)
        q = word.find(let)
        dash[q] = let
        dash = "".join(dash)
        print(dash)
        print(states[w])
        print(
            f"****************************{n}/6 LIVES LEFT****************************")

    else:
        n -= 1
        print(f"You guessed {let}, that's not in the word. You lose a life.")
        w += 1
        if (n == 0):
            print("***********************IT WAS faking! YOU LOSE**********************")
            break
        print(states[w])
        print(
            f"****************************{n}/6 LIVES LEFT****************************")
    if (dash == word):
        print(f"You Guessed right: {dash}")
        break
