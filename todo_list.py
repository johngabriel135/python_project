#create a simple to-do list app that allows users to view, add delete and manage task.
#this project is perferct for learning tkinter widgets like, buttons, entry fields and listboxes.

from tkinter import *
from tkinter.font import Font
from PIL import Image, ImageTk
from tkinter import filedialog
import pickle

root = Tk()
image_col = Image.open("C:\\Users\\USER\\Downloads\\calculator icon.jpg")
data = ImageTk.PhotoImage(image=image_col)
root.iconphoto(TRUE, data)
root.title("TO-DO LIST")
root.geometry("500x400")
root.resizable(False, False)
# i created my font
my_font = Font(
    family= "Agency FB",
    size= 30,
    weight= "bold")

# i created my frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# i created my listbox
my_list = Listbox(my_frame, font=my_font, width=25, height=5, bg="white", bd= 0, highlightthickness=0, selectbackground="#a6a6a6", activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# i creates my list
my_schedule = ["1. Pray",
               "2. Brush your teeth",
               "3. Eat breakfast",
               "4. Go to school",
               "5. Learn python",
               "6. Eat lunch",
               "7. Go home",
               "8. Take a nap"]

# i added my list to my listbox
for item in my_schedule:
    my_list.insert(END, item)

# i created my scroollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# i added my scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# i created entry field to add items to the list
my_entry = Entry(root, font=("helvetical", 24), width= 24)
my_entry.pack(pady=10)

# i created my button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

def Delete_task():
    my_list.delete(ANCHOR)

def Add_task():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def Cross_off_task():
    my_list.itemconfig(
        my_list.curselection(),
        fg="light grey")
    my_list.select_clear(0, END)

def Uncross_task():
    my_list.itemconfig(
        my_list.curselection(),
        fg="black")
    my_list.select_clear(0, END)


def save_data():
    file_name = filedialog.asksaveasfilename(
    initialdir="C:/GUIFOLDER/PROJECT/first_project data",
        title="save file",
       filetypes= (("Dat Files", "*.txt"),
                   ("All Files", "*.*")))

    if file_name:
        if file_name.endswith(".txt"):
            pass
    else:
        file_name = f"{file_name}.txt"
# delete crossed item before saving
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "light grey":
            my_list.delete(my_list.index(count))
    else:
            count += 1

# grab all the things from the list
my_things = my_list.get(0,END)

# open the data
output_file = open("file_name","wb")
# add things to the file
pickle.dump(my_things, output_file)

def open_data():
    file_name = filedialog.askopenfilename(initialdir="C:/GUIFOLDER/PROJECT/first_project data",
        title="open file",
       filetypes= (("Dat Files", "*.txt"),
                   ("All Files", "*.*")))
    if file_name:
        # delete currently opened file
        my_list.delete(0, END)

        # open the file
        input_file = open(file_name, "rb")

        # load the data from the file

        my_things = pickle(input_file)

        # output things to the screen
        for item in my_things:
            my_list.insert(END, item)

def clear_data():
    my_list.get(0, END)
    my_list.delete(0, END)

# i created my menu
my_menu = Menu(root)
root.config(menu=my_menu)

# i added items to my menu
data_menu = Menu(my_menu, tearoff=FALSE)
my_menu.add_cascade(label="Data", menu=data_menu)

# i added my drop down items
data_menu.add_command(label="save data",  command=save_data)
data_menu.add_separator()
data_menu.add_command(label="open data", command=open_data)
data_menu.add_separator()
data_menu.add_command(label="clear data", command=clear_data)


# i added my buttons
delete_button = Button(button_frame, text="Delete task", command=Delete_task)
add_button = Button(button_frame, text="Add task", command=Add_task)
cross_off_button = Button(button_frame, text="Cross off task", command=Cross_off_task)
uncross_button = Button(button_frame, text="Uncross task", command=Uncross_task)

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)


root.mainloop()