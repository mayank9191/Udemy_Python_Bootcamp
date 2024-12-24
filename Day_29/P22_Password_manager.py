from tkinter import *
from tkinter import messagebox
from charater import alphabets, symbols, numbers
import random


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
        is_ok = messagebox.askokcancel(title=website, message=f'''These are the details entered: \nEmail: {
            email}\nPassword: {password}\nIs it ok to save?''')

        if (is_ok):
            file_add(website, email, password)
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def file_add(website, email, password):
    with open("Day_29/Password.txt", "a") as f:
        f.write(f"{website} | {email} | {password}" + "\n")


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

website_entry = Entry(width=50)
website_entry.grid(column=1, row=1, columnspan=2, pady=3, padx=10, sticky=(W))
website_entry.focus()

email_entry = Entry(width=50)
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


window.mainloop()
