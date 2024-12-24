# import tkinter
from tkinter import *


def button_clicked():
    # my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())
    # my_label.pack()
    my_label.grid(column=0, row=0)


window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=100, pady=200)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New_text"
my_label.config(text="New_text")
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Buttonh

button = Button(text="Click Me", command=button_clicked)
# button.pack()
# button.place(x=1, y=1)
button.grid(column=1, row=1)

# New Button

new_button = Button(text="Click pls", command=button_clicked)
new_button.grid(column=2, row=0)
# Entry

input = Entry(width=10)
# input.pack()
# input.place(x=3, y=5)
input.grid(column=3, row=2)

window.mainloop()
