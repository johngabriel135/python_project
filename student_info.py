from tkinter import *
import tkinter as tk
from tkinter import messagebox
import sys
from tkinter.font import Font
from PIL import ImageTk, Image

root = tk.Tk()
root.title("STUDENT INFORMATION FORM")
image_type = Image.open("C:\\Users\\USER\\Downloads\\F.U.T logo.jpeg")
image_data = ImageTk.PhotoImage(image=image_type)
root.iconphoto(True, image_data)
root.geometry("300x300")
root.config(bg="white")
root.resizable(False, False)

my_font =  (
    "arial",
    12,
    "bold"
)

def form():
    name = enter_name.get()
    age = enter_age.get()
    gender = enter_gender.get()
    course = enter_course.get()



    if name and age and gender and course:
        messagebox.showinfo("Successful", f"Welcome, {name}! ☺")
    else:
        messagebox.showwarning("blank fields detected", "Please fill out all fields.")

def reset_key():
    name = enter_name.get()
    age = enter_age.get()
    gender = enter_gender.get()
    course = enter_course.get()
    enter_name.delete(0, END)
    enter_age.delete(0, END)
    enter_gender.delete(0, END)
    enter_course.delete(0, END)

    if name and age and gender and course:
        messagebox.showinfo(f"Information cleared", "bye! 👋")
        
def Exit_key():
    sys.exit(0)

label = Label(root, text="Name :").grid(row=0, column=0, padx=10, pady=5)
enter_name = Entry(root)
enter_name.grid(row=0, column=1, padx=10, pady=5)

label = Label(root, text="Age :").grid(row=1, column=0, padx=10, pady=5)
enter_age = Entry(root)
enter_age.grid(row=1, column=1, padx=10, pady=5)

label = Label(root, text="Gender :").grid(row=2, column=0, padx=10, pady=5)
enter_gender = Entry(root)
enter_gender.grid(row=2, column=1, padx=10, pady=5)

label = Label(root, text="Course :").grid(row=3, column=0, padx=10, pady=5)
enter_course = Entry(root)
enter_course.grid(row=3, column=1, padx=10, pady=5)

form_button = Button(root, text="Submit", command=form)
form_button.grid(row=4, column=0, pady=15, padx=10)
form_button.config(bg="blue", font=my_font, fg='white')
reset_button = Button(root, text="Reset", command=reset_key)
reset_button.grid(row=4, column=1, pady=15)
reset_button.config(bg="brown", fg="white")

button_exit = Button(root, text="Exit", padx=15, command=Exit_key)
button_exit.grid(row=4, column=2)
button_exit.config(bg="black", fg="white")

root.mainloop()