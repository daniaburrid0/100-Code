# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import string

def generate_password():
    password_entry.delete(0, END)
    password = ""
    for _ in range(0, 8):
        password += random.choice(string.ascii_letters)
    password_entry.insert(0, password)
    # add to clipboard
    windows.clipboard_clear()
    windows.clipboard_append(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
from tkinter import messagebox
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if password == "" or website == "":
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    with open("data.txt", mode="a") as file:
        file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)
        messagebox.showinfo(title="Success", message="Password saved successfully.")

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import *

# Window
windows = Tk()
windows.title("Password Manager")
windows.config(padx=20, pady=20)

# Logo
canvas = Canvas(width=300, height=300)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(150, 150, image=logo_img)
canvas.grid(row=0, column=1)

# Website label and entry
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=65)
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW", padx=10, pady=5)
website_entry.focus()

# Email/Username label and entry
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
email_entry = Entry(width=65)
email_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=10, pady=5)

# Password label and entry
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry = Entry(width=42)
password_entry.grid(row=3, column=1, sticky="EW", padx=10, pady=5)

# Generate Password button
generate_password_button = Button(text="Generate Password", width=18, command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW", padx=10, pady=5)

# Add button
add_button = Button(text="Add", width=36, command=save_password)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", padx=10, pady=5)

windows.mainloop()
