import tkinter as tk
from tkinter import messagebox
import os

def register_user():
    username = username_entry.get()
    password = password_entry.get()

    if not username or not password:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    try:
        with open("users.txt", "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = []

    existing_users = {line.split(":")[0]: line.split(":")[1].strip() for line in lines}

    if username in existing_users:
        messagebox.showerror("Ошибка", "Пользователь с таким именем уже существует.")
        return

    try:
        with open("users.txt", "a") as f:
            f.write(f"{username}:{password}\n")
        messagebox.showinfo("Успех", "Пользователь успешно зарегистрирован!")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    except OSError as e:
        messagebox.showerror("Ошибка", f"Ошибка записи в файл: {e}")


root = tk.Tk()
root.title("Регистрация пользователя")

username_label = tk.Label(root, text="Имя пользователя:")
username_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

password_label = tk.Label(root, text="Пароль:")
password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5, pady=5)

register_button = tk.Button(root, text="Зарегистрироваться", command=register_user)
register_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()