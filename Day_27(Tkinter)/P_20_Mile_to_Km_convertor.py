from tkinter import *


window = Tk()
window.title("Mile to Km Convertor")
window.minsize(width=250, height=100)
window.config(padx=40, pady=20)

# Entry

input = Entry(width=10)
input.grid(column=4, row=0)

# Label

label1 = Label(text="Miles")
label1.grid(column=5, row=0)

label2 = Label(text="is equal to")
label2.grid(column=3, row=1)

label3 = Label(text="")
label3.grid(column=4, row=1)

label4 = Label(text="Km")
label4.grid(column=5, row=1)
# Button


def calculate():
    answer = round(float(input.get()) * 1.609, 2)
    label3.config(text=f"{answer}")
    label3.grid(column=4, row=1)


button = Button(text="Calculate", command=calculate)
button.grid(column=4, row=3)


window.mainloop()
