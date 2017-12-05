import sys
from tkinter import *

def make_cmd(yama):
    buff = StringVar()
    buff.set(yama)
    label = Label(root, textvariable = buff)
    label.pack()

root = Tk()
button = Button(root, text = "Python/Tkinter", command= make_cmd("yama"))
button.pack()

root.mainloop()
