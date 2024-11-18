import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip  # For clipboard integration

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        master.title("Advanced Password Generator")

        # Options for password complexity
        self.length_label = tk.Label(master, text="Password Length:")
        self.length_label.pack()

        self.length_entry = tk.Entry(master)
        self.length_entry.pack()

        self.include_uppercase = tk.BooleanVar(value=True)
        self.uppercase_check = tk.Checkbutton(master, text="Include Uppercase Letters", variable=self.include_uppercase)
        self.uppercase_check.pack()

        self.include_numbers = tk.BooleanVar(value=True)
        self.numbers_check = tk.Checkbutton(master, text="Include Numbers", variable=self.include_numbers)
        self.numbers_check.pack()

        self.include_symbols = tk.BooleanVar(value=True)
        self.symbols_check = tk.Checkbutton(master, text="Include Symbols", variable=self.include_symbols)
        self.symbols_check.pack()

        self.exclude_chars_label = tk.Label(master, text="Exclude Characters (optional):")
        self.exclude_chars_label.pack()

        self.exclude_chars_entry = tk.Entry(master)
        self.exclude_chars_entry.pack()

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack()

        self.password_label = tk.Label(master, text="Generated Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master)
        self.password_entry.pack()

        self.copy_button = tk.Button(master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.pack()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                raise ValueError("Password length must be at least 1.")

            character_set = string.ascii_lowercase
            if self.include_uppercase.get():
                character_set += string.ascii_uppercase
            if self.include_numbers.get():
                character_set += string.digits
            if self.include_symbols.get():
                character_set += string.punctuation

            exclude_chars = self.exclude_chars_entry.get()
            character_set = ''.join(c for c in character_set if c not in exclude_chars)

            if not character_set:
                raise ValueError("No characters available for password generation.")

            password = ''.join(random.choice(character_set) for _ in range(length))
            self.password_entry.delete(0, tk.END)
            self.password_entry.insert(0, password)
        except ValueError as ve:
            messagebox.showerror("Input Error", str(ve))

    def copy_to_clipboard(self):
        password = self.password_entry.get()
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied", "Password copied to clipboard!")

if __name__ == "__main__":
    root = tk.Tk()
    password_generator = PasswordGenerator(root)
    root.mainloop()

# for runnign this programme use this command in your terminal :- python password_generator.py