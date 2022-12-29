import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage


def new_item():
    item = my_entry.get()
    if item != "":
        lb.insert(END, item)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("Warning", "Please enter an item.")


def delete_item():
    lb.delete(ANCHOR)

# shopping list (sl)
sl = Tk()


# Location middle of screen
w = 600
h = 600
ws = sl.winfo_screenwidth()
hs = sl.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
sl.geometry('%dx%d+%d+%d' % (w, h, x, y))

# sl.title("Shopping list")
titleImg = PhotoImage(file="TitleShopping.png")
title = Label(sl, image=titleImg, bg='#FFFCAE')
title.pack(side="top", fill="both", expand=True)

sl.config(bg='#FFFCAE')
sl.resizable(width=True, height=True)

# Main list
frame = Frame(sl)
frame.pack(pady=20)

lb = Listbox(
    frame,
    width=25,
    height=10,
    font=('Chalkboard', 18),
    bd=0,
    fg='#000000',
    highlightthickness=0,
    selectbackground='#FFFFFF',
    activestyle="dotbox",
)


shopping = ""
for item in shopping:
    lb.insert(END, item)


lb.pack(side=LEFT, fill=BOTH)


# Scrollbar
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    sl,
    font=('chalkboard', 24)
)

my_entry.pack(pady=20)

# Buttons
button_frame = Frame(sl)
button_frame.pack(pady=20)

add_item_btn = Button(
    button_frame,
    text='Add Item',
    font='arial 14',
    bg='#ffffff',
    padx=10,
    pady=10,
    command=new_item
)
add_item_btn.pack(fill=BOTH, expand=True, side=LEFT)

delitem_btn = Button(
    button_frame,
    text='Delete item',
    font='arial 14',
    bg='#ffffff',
    padx=10,
    pady=10,
    command=delete_item
)
delitem_btn.pack(fill=BOTH, expand=True, side=LEFT)


sl.mainloop()
