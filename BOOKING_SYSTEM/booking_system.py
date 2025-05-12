import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk
from time import strftime

# Sample user data with roles
users = {
    "Admin": {"password": "password1", "role": "admin"},
    "Customer": {"password": "password2", "role": "customer"},
}


# --------- LOGIN WINDOW -------------
def login_window():
    login = Tk()
    login.title("Login")
    login.geometry("400x300")
    login.resizable(False, False)
    login.configure(bg="white")

    tk.Label(
        login,
        text="Store Booking Login",
        font=("agency fb", 20, "bold"),
        bg="white",
        fg="black",
    ).pack(pady=10)

    tk.Label(login, text="Username:", font=("agency fb", 12), bg="white").pack(pady=5)
    entry_username = tk.Entry(login, font=("agency fb", 12))
    entry_username.pack()

    tk.Label(login, text="Password:", font=("agency fb", 12), bg="white").pack(pady=5)
    entry_password = tk.Entry(login, show="*", font=("agency fb", 12))
    entry_password.pack()

    def authenticate():
        username = entry_username.get()
        password = entry_password.get()
        if username in users and users[username]["password"] == password:
            login.destroy()
            open_dashboard(username, users[username]["role"])
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    tk.Button(
        login,
        text="Login",
        font=("agency fb", 14),
        command=authenticate,
        width=16,
        bg="indigo",
        fg="white",
    ).pack(pady=20)

    login.mainloop()


# --------- DASHBOARD WINDOW -------------
def open_dashboard(username, role):
    root = Tk()
    root.title("STORE BOOKING SYSTEM")
    root.geometry("1270x668+0+0")
    root.resizable(False, False)
    root.config(bg="white")

    Label(
        root,
        text="STORE BOOKING SYSTEM",
        font=("agency fb", 40, "bold"),
        bg="indigo",
        fg="white",
    ).place(x=0, y=0, relwidth=1)

    Button(
        root,
        text="Logout",
        font=("agency fb", 20, "bold"),
        fg="indigo",
        command=root.destroy,
    ).place(x=1110, y=6)

    # Clock
    def update_clock():
        current_time = strftime("%H:%M:%S %p")
        clock_label.config(text=current_time)
        clock_label.after(1000, update_clock)

    clock_label = tk.Label(
        root, font=("calibri", 35, "bold"), background="purple", foreground="white"
    )
    clock_label.pack(anchor="nw", padx=20, pady=2)
    update_clock()

    Label(
        root,
        text=f"Welcome, {username.upper()} ({role.upper()})",
        font=("agency fb", 15, "bold"),
        bg="grey",
        fg="white",
    ).place(x=0, y=70, relwidth=1)

    if role == "customer":
        # Customer Panel
        left_frame = Frame(root, bg="light grey")
        left_frame.place(x=0, y=100, width=200, height=545)

        Label(
            left_frame,
            text="CUSTOMER UI",
            font=("agency fb", 25),
            bg="green",
            fg="white",
        ).pack(fill=X)

        Button(
            left_frame,
            text="BOOK AN ITEM",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            left_frame,
            text="RESERVED ITEMS",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            left_frame,
            text="NOTIFICATIONS",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            left_frame,
            text="EXIT",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
            command=root.destroy,
        ).pack(fill=X)

    elif role == "admin":
        # Admin Panel
        right_frame = Frame(root, bg="light grey")
        right_frame.place(x=1070, y=102, width=200, height=555)

        Label(
            right_frame, text="ADMIN UI", font=("agency fb", 20), bg="red", fg="white"
        ).pack(fill=X)

        Button(
            right_frame,
            text="BOOKINGS",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            right_frame,
            text="UPDATE STOCK",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            right_frame,
            text="STOCK STATUS",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
        ).pack(fill=X)
        Button(
            right_frame,
            text="EXIT",
            font=("agency fb", 20, "bold"),
            bg="light blue",
            fg="black",
            command=root.destroy,
        ).pack(fill=X)

    root.mainloop()


# ---------- START THE APP ----------
login_window()
