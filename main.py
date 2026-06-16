import tkinter as tk
from tkinter import ttk, messagebox

BG_COLOR = "#eaf6ff"
CARD_COLOR = "#ffffff"
HEADING_COLOR = "#1b4965"
BTN_COLOR = "#5fa8d3"
BTN_HOVER = "#1b4965"
TEXT_COLOR = "#1b4965"

window = tk.Tk()
window.title("Login & Signup System")
window.geometry("420x460")
window.config(bg=BG_COLOR)

style = ttk.Style()
style.theme_use("clam")
style.configure("Blue.TButton",
                background=BTN_COLOR,
                foreground="white",
                font=("Arial", 12, "bold"),
                padding=10,
                borderwidth=0)
style.map("Blue.TButton", background=[("active", BTN_HOVER)])

card = tk.Frame(window, bg=CARD_COLOR, padx=30, pady=30,
                 highlightbackground=BTN_COLOR, highlightthickness=2)
card.place(relx=0.5, rely=0.5, anchor="center")

heading = tk.Label(card, text="Welcome", font=("Arial", 24, "bold"), bg=CARD_COLOR, fg=HEADING_COLOR)
heading.grid(row=0, column=0, columnspan=2, pady=(0, 20))

tk.Label(card, text="Username", font=("Arial", 12), bg=CARD_COLOR, fg=TEXT_COLOR).grid(row=1, column=0, columnspan=2, sticky="w")
username_entry = tk.Entry(card, font=("Arial", 12), width=30, relief="solid", bd=1)
username_entry.grid(row=2, column=0, columnspan=2, pady=(2, 15))

tk.Label(card, text="Password", font=("Arial", 12), bg=CARD_COLOR, fg=TEXT_COLOR).grid(row=3, column=0, columnspan=2, sticky="w")
password_entry = tk.Entry(card, font=("Arial", 12), width=30, show="*", relief="solid", bd=1)
password_entry.grid(row=4, column=0, columnspan=2, pady=(2, 20))


def signup():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill both fields")
        return

    file = open("users.txt", "a")
    file.write(username + "," + password + "\n")
    file.close()

    messagebox.showinfo("Success", "Signup Successful!")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill both fields")
        return

    found = False

    try:
        file = open("users.txt", "r")
        users = file.readlines()
        file.close()

        for line in users:
            data = line.strip().split(",")
            if username == data[0] and password == data[1]:
                found = True
                break

        if found:
            messagebox.showinfo("Success", "Login Successful!")
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

    except:
        messagebox.showerror("Error", "No users found. Please signup first")


signup_btn = ttk.Button(card, text="Signup", style="Blue.TButton", command=signup)
signup_btn.grid(row=5, column=0, padx=8, pady=5, sticky="ew")

login_btn = ttk.Button(card, text="Login", style="Blue.TButton", command=login)
login_btn.grid(row=5, column=1, padx=8, pady=5, sticky="ew")

window.mainloop()