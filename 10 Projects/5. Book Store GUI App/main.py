""""
    A program that stores this book information:
        1. Title
        2. Author
        3. Year
        4. ISBN

    A user can:
        1. view all the records
        2. search an entry
        3. add entry
        4. update entry
        5. delete
        6. close
"""

from tkinter import *

window = Tk()

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

btn_width = 10
view_all_btn = Button(window, text="View all", width=btn_width)
view_all_btn.grid(row=2, column=3)

search_entry_btn = Button(window, text="Search entry", width=btn_width)
search_entry_btn.grid(row=3, column=3)

add_entry_btn = Button(window, text="Add entry", width=btn_width)
add_entry_btn.grid(row=4, column=3)

update_btn = Button(window, text="Update", width=btn_width)
update_btn.grid(row=5, column=3)

delete_btn = Button(window, text="Delete", width=btn_width)
delete_btn.grid(row=6, column=3)

close_btn = Button(window, text="Close", width=btn_width)
close_btn.grid(row=7, column=3)

window.mainloop()
