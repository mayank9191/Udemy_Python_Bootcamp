import pandas

data = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")

nato_dict = {value.alpha: value.nato for (key, value) in data.iterrows()}


def generate_phonetic():
    input_word = input("Enter a word: ").lower()

    try:
        message = [nato_dict[i] for i in list(input_word) if (i != " ")]

    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()

    else:
        print(message)
