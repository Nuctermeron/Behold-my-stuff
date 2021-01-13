from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

"""Functions"""


def add_fun():
    web = website_entry.get().title()
    email = mail_entry.get()
    password = password_entry.get()
    new_data = {
        web: {
            "email": email,
            "password": password
        }
    }
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo("Please fill all fields")
    else:
        try:
            with open("passwords.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open("passwords.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("passwords.json", "w") as file:
                json.dump(data, file, indent=4)

            website_entry.delete(0, END)
            password_entry.delete(0, END)


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for n in range(random.randint(0, 10))]
    password_symbols = [random.choice(numbers) for n in range(random.randint(2, 4))]
    password_numbers = [random.choice(symbols) for n in range(random.randint(2, 4))]

    passwordL = password_letters + password_symbols + password_numbers
    random.shuffle(passwordL)

    password = "".join(passwordL)

    password_entry.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="Added", message="Password copied to clipboard")


def find_password():
    website = website_entry.get().title()
    try:
        with open("passwords.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file in folder")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,
                                message=f"Data for this website already exists.\nEmail: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


"""Window setup"""
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20, bg="white")

"""Canvas setup"""
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0, )
logo = PhotoImage(file="logo.gif")
canvas.create_image(100, 100, image=logo, anchor=CENTER)
canvas.grid(column=1, row=0)

"""Widgets setup"""
website_label = Label(text="Website:", bg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=30)
website_entry.grid(column=1, row=1, sticky="w")
website_entry.focus()

mail_label = Label(text="Email/Username:", bg="white")
mail_label.grid(column=0, row=2)

mail_entry = Entry(width=52)
mail_entry.grid(column=1, row=2, columnspan=2, sticky="w")
mail_entry.insert(0, "your_email@gmail.com")

password_label = Label(text="Password:", bg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="w")

password_generate_button = Button(text="Generate Password", command=generate_password)
password_generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=add_fun)
add_button.grid(column=1, row=4, columnspan=2)

search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
