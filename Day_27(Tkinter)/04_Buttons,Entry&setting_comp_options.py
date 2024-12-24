# import tkinter
from tkinter import *

window = Tk()

window.title("My First GUI Program")
window.minsize(width=500, height=500)

# Label

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label["text"] = "New_text"
my_label.config(text="New_text")
my_label.pack()


# Button


def button_clicked():
    # my_label["text"] = "Button got clicked"
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())
    my_label.pack()


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()

window.mainloop()
