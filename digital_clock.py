import tkinter as tk
import time

def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")

# Create and configure the clock label
clock_label = tk.Label(root, font=("Helvetica", 48), bg="black", fg="white")
clock_label.pack(anchor='center')

# Start the clock
update_clock()