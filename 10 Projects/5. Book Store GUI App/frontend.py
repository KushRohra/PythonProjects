from tkinter import *

from backend import delete, insert, search, update, view

window = Tk()

window.wm_title("Book Store")


def clear_entry_fields():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def get_selected_row(event):
    global selected_tuple
    if len(list1.curselection()) == 0:
        return
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    clear_entry_fields()
    e1.insert(END, selected_tuple[1])
    e2.insert(END, selected_tuple[2])
    e3.insert(END, selected_tuple[3])
    e4.insert(END, selected_tuple[4])


def view_command():
    clear_entry_fields()
    list1.delete(0, END)
    for row in view():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)
    clear_entry_fields()


def add_command():
    insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))
    clear_entry_fields()


def delete_command():
    delete(selected_tuple[0])
    view_command()


def update_command():
    update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    clear_entry_fields()
    view_command()


l1 = Label(window, text="Title")
l1.grid(row=0, column=0)
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)
author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)
year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)
isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1 = Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>', get_selected_row)

btn_width = 10
view_all_btn = Button(window, text="View all", width=btn_width, command=view_command)
view_all_btn.grid(row=2, column=3)

search_entry_btn = Button(window, text="Search entry", width=btn_width, command=search_command)
search_entry_btn.grid(row=3, column=3)

add_entry_btn = Button(window, text="Add entry", width=btn_width, command=add_command)
add_entry_btn.grid(row=4, column=3)

update_btn = Button(window, text="Update", width=btn_width, command=update_command)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text="Delete", width=btn_width, command=delete_command)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=btn_width, command=window.destroy)
close_btn.grid(row=7, column=3)

window.mainloop()
