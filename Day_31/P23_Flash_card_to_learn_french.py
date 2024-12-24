from tkinter import *
import pandas
import random
import time

BACKGROUND_COLOR = "#B1DDC6"

current_card = {}
# Data from French_words

try:
    data = pandas.read_csv("Day_31/data/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("Day_31/data/french_words.csv")
    french_dict = original_data.to_dict(orient="records")

else:
    french_dict = data.to_dict(orient="records")


def change():
    canvas.itemconfig(canvas_image, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def next_card():
    global current_card, flip_timmer
    window.after_cancel(flip_timmer)
    current_card = random.choice(french_dict)
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")

    flip_timmer = window.after(3000, change)


def is_known():
    french_dict.remove(current_card)
    word = pandas.DataFrame(french_dict)
    word.to_csv("Day_31/data/words_to_learn.csv", index=False)
    next_card()


#                                   UI Design
window = Tk()
window.title("Flashy")
window.configure(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timmer = window.after(3000, change)


# Canvas

card_front_img = PhotoImage(file="Day_31/images/card_front.png")
card_back_img = PhotoImage(file="Day_31/images/card_back.png")

canvas = Canvas(width=800, height=526,
                bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(
    400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(
    400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

# Button

right_img = PhotoImage(file="Day_31/images/right.png")
right_button = Button(
    image=right_img, command=is_known, highlightthickness=0)
right_button.grid(column=1, row=1)

cross_img = PhotoImage(file="Day_31/images/wrong.png")
cross_button = Button(
    image=cross_img, command=next_card, highlightthickness=0)
cross_button.grid(column=0, row=1)

next_card()
window.mainloop()
