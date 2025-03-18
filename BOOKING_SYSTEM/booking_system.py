from tkinter import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import messagebox
import time


# calling my tkinter attributes
root = Tk()
root.title("STORE BOOKING SYSTEM")
root.geometry("1270x668+0+0")
root.resizable(False, False)
root.config(bg="white")

# creating my icon
image_col = Image.open("C:\\Users\\USER\\Downloads\\download.jpeg")
data = ImageTk.PhotoImage(image=image_col)
root.iconphoto(TRUE, data)


# creating my label widget
my_label = Label(root, text="STORE BOOKING SYSTEM", font=("agency fb", 40, "bold"),bg="indigo",fg="white")
my_label.place(x=0,y=0, relwidth=1)

# creating my log out button
logout_butoon = Button(root,text="Logout",font=("agency fb",20,"bold"),fg="indigo")
logout_butoon.place(x=1110,y=10)


#date and time format
# i define my time
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    sub_title.config(current_time)
    sub_title.after(1000, update_clock)
    update_clock

#  creating my sub-title headings
sub_title = Label(root, text=f"Welcome\t\t Time{update_clock} ",font=("agency fb",15, "bold"),bg="grey", fg="white")
sub_title.place(x=0,y=70,relwidth=1)
# left frame
left_frame = Frame(root, bg="light grey")
left_frame.place(x=0, y=100, width=200, height=545)

# creating my customer UI frame image
left_frame_image = PhotoImage(file="C:\\Users\\USER\\Downloads\\download (6).png")
left_frame_icon = Label(left_frame, image=left_frame_image).pack()

menu = Label(left_frame, text="CUSTOMER'S UI", font=("agency fb", 25), bg="green", fg="white")
menu.pack(fill=X)

slot_button = Button(left_frame, text="BOOK AN ITEM", font=("agency fb", 20, "bold"),bg="light blue",fg="black")
slot_button.pack(fill=X)

items_button = Button(left_frame,text="RESERVED ITEMS",font=("agency fb",20,"bold"),bg="light blue",fg="black")
items_button.pack(fill=X)

notification_button = Button(left_frame,text="NOTIFICATIONS",font=("agency fb", 20, "bold"), bg="light blue",fg="black")
notification_button.pack(fill=X)

customer_exit_button = Button(left_frame,text="EXIT",font=("agency fb",20,"bold"),bg="light blue",fg="black",command=root.destroy)
customer_exit_button.pack(fill=X)


#  i created my admin UI
right_frame = Frame(root,bg="light grey")
right_frame.place(x=1070,y=102,width=200,height=555,)

# creating my admin UI frame image
right_frame_image = PhotoImage(file="C:\\Users\\USER\\Downloads\\images (4).png")
right_frame_icon = Label(right_frame, image=right_frame_image).pack()

Admin = Label(right_frame, text="ADMIN UI", font=("agency fb", 20), bg="red", fg="white")
Admin.pack(fill=X)

bookings_button = Button(right_frame,text="BOOKINGS",font=("agency fb",20,"bold"),bg="light blue",fg="black")
bookings_button.pack(fill=X)

stock_button = Button(right_frame,text="UPDATE STOCK",font=("agency fb",20,"bold"),bg="light blue",fg="black")
stock_button.pack(fill=X)

stock_status_button = Button(right_frame,text="STOCK STATUS",font=("agency fb",20,"bold"),bg="light blue",fg="black")
stock_status_button.pack(fill=X)

admin_exit_button = Button(right_frame,text="EXIT",font=("agency fb",20,"bold"),bg="light blue",fg="black", command=root.destroy)
admin_exit_button.pack(fill=X)

    
# i created our password interface
password_label = Label(root,text="ENTER PASSWORD",font=("agency fb ",20),bg="blue",fg="white",)
password_label.place(x=420,y=150,width=400)



# Sample user data
users = {
    "Admin": "password1",
    "Customer": "password2"
}

def authenticate():
    username = entry_username.get()
    password = entry_password.get()


    if username in users and users[username] == password:
        messagebox.showinfo("Login Success", "Welcome, " + username + "!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        
        if messagebox.showinfo:
            username in users and users[username].delete(0,END)
            
        

# Create and placed the username label and entry
label_username = tk.Label(root, text="Username",font=("agency fb",10,"bold"),bg="#cccccc")
label_username.place(x=579,y=200,width=100)
entry_username = tk.Entry(root,font=("agency fb",17,"bold"))
entry_username.place(x=510,y=230,width=200)

# Create and place the password label and entry
label_password = tk.Label(root, text="Password",font=("agency fb",10,"bold"),bg="#cccccc")
label_password.place(x=579,y=260,width=100)
entry_password = tk.Entry(root, show="*",font=("agency fb",17,"bold"))
entry_password.place(x=510,y=290,width=200)

# Create and place the login button
button_login = tk.Button(root, text="Login",bg="#cccccc",font=("agency fb",15,"bold"), command=authenticate)
button_login.place(x=595,y=330,width=70)


root.mainloop()