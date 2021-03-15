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

from frontend import frontend
from tkinter import *


def main():
    window = Tk()

    frontend(window)

    window.mainloop()


if __name__ == "__main__":
    main()