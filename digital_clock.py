import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x200")
root.resizable(False,False)

def update_clock():
    current_time = time.strftime("%H:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)


clock_label = tk.Label(root, font=("Helvetica", 30), bg="black", fg="red")
clock_label.pack(anchor="center")

update_clock()

root.mainloop()