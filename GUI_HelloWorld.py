import sys
from tkinter import *

#define function of label in GUI.
def make_cmd(val_str):
    buff = StringVar()
    buff.set(val_str)
    label = Label(root, textvariable = buff)
    label.pack()

root = Tk()
button = Button(root, text = "Python/Tkinter", command= make_cmd("Hello_wrold!"))
button.pack()

root.mainloop()
