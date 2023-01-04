from game import game
from functions import *
from tkinter import *


def mainmenu():
    global width, height, canvas
    #canvas.delete("all")
    
    canvas = Canvas(master=menu, background=auslesen("primary_color"))
    canvas.place(width=width, height=height)

    button_play = Button(master=menu, text="Play", bg=auslesen("secondary_color"), command=play)
    button_play.place(x=(width/2)-100, y=(height/2)-75, width=200, height=50)

    button_settings = Button(master=menu, text="SETTINGS", bg=auslesen("secondary_color"), command=settings)
    button_settings.place(x=(width/2)-100, y=(height/2), width=200, height=50)

    button_quit = Button(master=menu, text="QUIT", bg=auslesen("secondary_color"), command=quit)
    button_quit.place(x=(width/2)-100, y=(height/2)+75, width=200, height=50)

def play(): #weiterleitung zum Spiel(schließt menufenster)
    menu.destroy()
    game()

def settings(): #Weiterleitung zu Settings
    global width, height, canvas
    #canvas.delete("all")

    menu.title("Settings")

    canvas = Canvas(master=menu, background=auslesen("secondary_color"))
    canvas.place(width=width, height=height)

    mitte = Canvas(master=menu, background=auslesen("primary_color"))
    mitte.place(x=0, y=height/8, width=width, height=height-(height/4))

    #title = Label(master=)

def quit(): #Beendet das Spiel
    menu.destroy()
    quit()

def close(): #um das bearbeiten angenehmer zu gestalten
    menu.destroy()

#def clear():
        

global menu

menu = Tk()
menu.title("Menu")
menu.attributes("-fullscreen", True)

width = menu.winfo_screenwidth()
height = menu.winfo_screenheight()

canvas = Canvas()

menu.after(5000, close)
mainmenu()


menu.mainloop()


