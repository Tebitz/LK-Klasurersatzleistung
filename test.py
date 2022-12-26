
from tkinter import *
# Erzeugung des Fensters

tkFenster = Tk()
tkFenster.title('Test')
tkFenster.geometry('550x300')

canvas = Canvas(master=tkFenster, background="gray")
canvas.place(width=450, height=250)

canvas.create_text(225, 50, font=("Arial", 62), text="Informatik") 

test = Text(master=canvas, background="black")
"""
import tkinter as tk

root = tk.Tk()
T = tk.Text(root, height=3, width=3, bg="red", font=("Helvetica", 72))
T.pack()
T.insert(tk.END, "        5")
tk.mainloop()
"""


# Aktivierung des Fensters
tkFenster.mainloop()