import pandas

data = pandas.read_csv("Day_26/nato_phonetic_alphabet.csv")

nato_dict = {value.alpha: value.nato for (key, value) in data.iterrows()}

input_word = input("Enter a word: ").lower()
message = [nato_dict[i] for i in list(input_word) if (i != " ")]

print(message)
