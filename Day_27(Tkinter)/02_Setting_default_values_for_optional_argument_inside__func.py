import tkinter


window = tkinter.Tk()
window.title("My GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))

# It like when a function is made it have some default argument which is optional to give its value in keyword argument

my_label.pack(side="left")


window.mainloop()
