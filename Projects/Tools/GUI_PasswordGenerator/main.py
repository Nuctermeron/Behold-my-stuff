from tkinter import *
from tkinter import messagebox
import random
import pyperclip

"""Functions"""


def add_fun():
    web = website_entry.get()
    email = mail_entry.get()
    password = password_entry.get()
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo("Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=web, message=f"Should be saved?")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(f"{web} | {email} | {password}\n")
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

website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky="w")
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

window.mainloop()
