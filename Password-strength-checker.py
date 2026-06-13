import tkinter as tk
from tkinter import ttk
import re


def check_strength():
    password = password_entry.get()
    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?:{}|<>]", password):
        score += 1
    if score <= 2:
        result_label.config(text="Weak Password❌❌", fg="#8B0000")
        progress["value"] = 33

    elif score <= 4:
        result_label.config(text="Medium Password⚠️", fg="#FF7F50")
        progress["value"] = 66

    else:
        result_label.config(text="Strong Password✅", fg="#00cc66")
        progress["value"] = 100

# Main Window
root = tk.Tk()
root.title("Cyber Security Password Checker")
root.geometry("500x350")
root.configure(bg="#1e1e2f")

# Heading
title = tk.Label(
    root,
    text="🔏Password Strength Checker",
    font=("Aerial", 18, "bold"),
    bg="#1e1e2f",
    fg="#00d4ff"
)
title.pack(pady=20)

# Password Entry
password_entry = tk.Entry(
    root,
    show="*",
    width=30,
    font=("Aerial", 14)
)
password_entry.pack(pady=10)

# Check Button
check_btn = tk.Button(
    root,
    text="Check Strength",
    command=check_strength,
    bg="#00d4ff",
    fg="black",
    font=("Arial", 12, "bold"),
    relief="raised"
)
check_btn.pack(pady=10)

# Progress bar
progress = ttk.Progressbar(
    root,
    orient="horizontal",
    length=300,
    mode="determinate"
)
progress.pack(pady=15)

# Result Label
result_label = tk.Label(
    root,
    text="Enter a password",
    font=("Arial", 14, "bold"),
    bg="#1e1e2f",
    fg="white"
)
result_label.pack(pady=10)

# Footer
footer = tk.Label(
    root,
    text="Python Cyber Security Project",
    bg="#1e1e2f",
    fg="#888888",
    font=("Arial", 10)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
