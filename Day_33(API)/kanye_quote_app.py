import requests
from tkinter import *


def change_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()
    quote = response.json()["quote"]
    canvas.itemconfigure(quote_text, text=quote)

# UI


window = Tk()
window.title("Kanye Says...")
window.configure(padx=50, pady=50)

# Canvas

background_image = PhotoImage(file="Day_33(API)/background.png")
canvas = Canvas(width=300, height=414)
canvas.create_image(150, 207, image=background_image)
quote_text = canvas.create_text(
    150, 207, text="Kanye Quote Goes HERE", font=("ariel", 20, "bold"), width=250, fill="white")
canvas.grid(column=0, row=0)

# Button

kanye_img = PhotoImage(file="Day_33(API)/kanye.png")
kanye_button = Button(
    image=kanye_img, command=change_quote)
kanye_button.grid(column=0, row=1)
window.mainloop()
