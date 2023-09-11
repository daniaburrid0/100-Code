import random
import string
import tkinter as tk
from tkinter import messagebox


class PasswordManager:
    def __init__(self, db_file: str):
        self.db_file = db_file
        self.create_table()

    def create_table(self):
        with open(self.db_file, mode="a"):
            pass

    def add_password(self, website: str, email: str, password: str):
        with open(self.db_file, mode="a") as file:
            file.write(f"{website} | {email} | {password}\n")


class PasswordManagerWindow(tk.Tk):
    def __init__(self, password_manager: PasswordManager):
        super().__init__()
        self.password_manager = password_manager
        self.title("Password Manager")
        self.config(padx=20, pady=20)

        # Logo
        canvas = tk.Canvas(width=300, height=300)
        logo_img = tk.PhotoImage(file="logo.png")
        canvas.create_image(150, 150, image=logo_img)
        canvas.grid(row=0, column=1)

        # Website label and entry
        website_label = tk.Label(text="Website:")
        website_label.grid(row=1, column=0)
        self.website_entry = tk.Entry(width=65)
        self.website_entry.grid(
            row=1, column=1, columnspan=2, sticky="EW", padx=10, pady=5
        )
        self.website_entry.focus()

        # Email/Username label and entry
        email_label = tk.Label(text="Email/Username:")
        email_label.grid(row=2, column=0)
        self.email_entry = tk.Entry(width=65)
        self.email_entry.grid(
            row=2, column=1, columnspan=2, sticky="EW", padx=10, pady=5
        )

        # Password label and entry
        password_label = tk.Label(text="Password:")
        password_label.grid(row=3, column=0)
        self.password_entry = tk.Entry(width=42)
        self.password_entry.grid(row=3, column=1, sticky="EW", padx=10, pady=5)

        # Generate Password button
        generate_password_button = tk.Button(
            text="Generate Password", width=18, command=self.generate_password
        )
        generate_password_button.grid(
            row=3, column=2, sticky="EW", padx=10, pady=5
        )

        # Add button
        add_button = tk.Button(
            text="Add", width=36, command=self.save_password
        )
        add_button.grid(
            row=4, column=1, columnspan=2, sticky="EW", padx=10, pady=5
        )

    def generate_password(self):
        password = "".join(
            random.choice(string.ascii_letters) for _ in range(8)
        )
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        self.clipboard_clear()
        self.clipboard_append(password)

    def save_password(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if not website or not password:
            messagebox.showinfo(
                title="Oops", message="Please fill in all required fields."
            )
            return
        self.password_manager.add_password(website, email, password)
        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo(
            title="Success", message="Password saved successfully."
        )


if __name__ == "__main__":
    password_manager = PasswordManager("data.txt")
    window = PasswordManagerWindow(password_manager)
    window.mainloop()