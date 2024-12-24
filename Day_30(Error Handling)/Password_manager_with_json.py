from tkinter import *
from tkinter import messagebox
from charater import alphabets, symbols, numbers
import random
import json


def generate_pass():
    pass_alph = [random.choice(alphabets)for i in range(random.randint(8, 10))]

    pass_num = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    pass_sym = [random.choice(symbols) for _ in range(random.randint(2, 4))]

    password_list = pass_alph + pass_num + pass_sym

    random.shuffle(password_list)
    random_string = "".join(password_list)
    password_entry.insert(0, string=random_string)
    window.clipboard_append(random_string)


def add():
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    if (website == "" and password == ""):
        messagebox.showinfo(title="Oops",
                            message="Please don't leave website name and password fields empty !")
        return

    elif (website == ""):
        messagebox.showinfo(
            title="Oops", message="Please don't leave website field empty !")
        return

    elif (password == ""):
        messagebox.showinfo(title="Oops",
                            message="Please don't leave password field empty !")
        return

    else:
        new_data = {
            website: {
                "email": email,
                "password": password
            }
        }

        file_add(new_data)
        website_entry.delete(0, END)
        password_entry.delete(0, END)


def file_add(new_data):
    try:
        with open("Day_30/Password.json", "r") as f:

            # Reading old data
            data = json.load(f)

    except FileNotFoundError:

        with open("Day_30/Password.json", "w") as f:
            json.dump(new_data, f, indent=4)

    else:
        # Updating old data with new data
        data.update(new_data)

    with open("Day_30/Password.json", "w") as f:

        # Saving updated data
        json.dump(data, f, indent=4)


def search():
    website = website_entry.get().title()
    try:
        with open("Day_30/Password.json", "r") as f:
            data = json.load(f)
        email_data = data[website]["email"]
        password_data = data[website]["password"]

    except FileNotFoundError:
        messagebox.showinfo(
            title="Oops", message=f"No Data File Found.")

    except KeyError:
        messagebox.showinfo(
            title="Oops", message=f"No Details For {website} Exist !")

    else:
        messagebox.showinfo(title=website, message=f'''Email:  {
            email_data}\nPassword:  {password_data}''')


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Canvas
canvas = Canvas(width=200, height=200)
my_pass_pic = PhotoImage(file="Day_29/logo.png")
canvas.create_image(100, 100, image=my_pass_pic)
canvas.grid(column=1, row=0)

# Label

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username/Phone No:")
email_label.grid(column=0, row=2)

password = Label(text="Password:")
password.grid(column=0, row=3)

# Entry

website_entry = Entry(width=32)
website_entry.grid(column=1, row=1, columnspan=2, pady=3, padx=10, sticky=(W))
website_entry.focus()

email_entry = Entry(width=55)
email_entry.grid(column=1, row=2, columnspan=2, pady=3, padx=10, sticky=(W))
email_entry.insert(0, string="mayankkulahara@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(column=1, row=3, padx=10, sticky=(W))


# Button

generate_button = Button(text="Generate Password",
                         command=generate_pass, width=15)
generate_button.grid(column=2, row=3, pady=3, sticky=(W))

add_button = Button(text="Add", command=add, width=36)
add_button.grid(column=1, row=4, columnspan=2, pady=3, padx=10, sticky=(W, E))

search = Button(text="Search", command=search, width=15)
search.grid(column=2, row=1, pady=3, sticky=(W))
window.mainloop()
