import requests
from tkinter import *

n = 0

rightanswer = []

parameters = {
    "amount": 10,
    "type": "boolean"
}


def get_question():
    response = requests.get(
        url="https://opentdb.com/api.php", params=parameters)

    response.raise_for_status()
    data = response.json()
    print(data)
    # with open("Day_34/Question.json", "w") as f:
    #     f.write(data)


def check(result):
    # if (rightanswer[0] == result):
    #     canvas.configure(bg="green")
    #     global n
    #     n += 1
    #     Label.configure(score_label, text=f"Score: {n}")

    # else:
    #     canvas.configure(bg="red")

    canvas.itemconfigure(question_text, text=get_question())
    canvas.configure(bg="white")


window = Tk()
window.title("Quizzler")
window.configure(padx=50, pady=50, bg="#2F4F4F")


# Label

score_label = Label(text=f"Score: {n}", font=(
    "ariel", 15, "normal"), fg="white", bg="#2F4F4F", highlightthickness=0)
score_label.grid(column=1, row=0)

# Canvas
canvas = Canvas(height=300, width=350, bg="white")
question_text = canvas.create_text(
    150, 130, text=get_question(), fill="#2F4F4F", font=("ariel", 20, "italic"), width=300)
canvas.grid(column=0, row=1, columnspan=2, pady=50)


# Button

right_img = PhotoImage(file="Day_34(Incomplete)/images/true.png")
true_button = Button(image=right_img, command=lambda: check("True"))
true_button.grid(column=0, row=2, pady=20)

wrong_img = PhotoImage(file="Day_34(Incomplete)/images/false.png")
false_button = Button(image=wrong_img, command=lambda: check("False"))
false_button.grid(column=1, row=2, pady=20)


window.mainloop()
