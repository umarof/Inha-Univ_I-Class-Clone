from tkinter import *

from tkinter import ttk

import login_ops as log
import forum_qa as forum

window = Tk()

window.title("Welcome to SWP8 Inha website")
window.geometry('1280x720')
window.resizable(False, False)


def start():

    log.widgets(window)


start()


window.mainloop()