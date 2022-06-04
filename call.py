# page = 0
# memory = {}

# def call(command, page, memory):
#     if command == "black":
#         try:
#             f = open("page/" + str(page) + ".txt", "xt")
#             memory[page] = page
#             return memory
#         except:
#             x = 0
#             page += 1
#             while x == 0:
#                 try:
#                     f = open("page/" + str(page) + ".txt", "xt")
#                     memory[page] = page
#                     return memory
#                 except:
#                     page += 1

from tkinter import *
from tkinter import ttk

alt = False

def call(command):
    try:
        if alt == False:
            if command == "black":
                alt = True
            if command == "white":
                root = Tk()
                frm = ttk.Frame(root, padding=10)
                frm.grid()
                ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
                ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
                root.mainloop()
        if alt == False:
            if command == "black":
                alt = False
    except:
        alt = False