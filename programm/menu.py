from game import game
from functions import textdatei
from tkinter import *


def mainmenu():
    global width, height, canvas
    #canvas.delete("all")
    
    canvas = Canvas(master=menu, background=textdatei("primary_color", "null"))
    canvas.place(width=width, height=height)

    button_play = Button(master=menu, text="Play", bg=textdatei("secondary_color", "null"), command=play)
    button_play.place(x=(width/2)-100, y=(height/2)-75, width=200, height=50)

    button_settings = Button(master=menu, text="SETTINGS", bg=textdatei("secondary_color", "null"), command=settings)
    button_settings.place(x=(width/2)-100, y=(height/2), width=200, height=50)

    button_quit = Button(master=menu, text="QUIT", bg=textdatei("secondary_color", "null"), command=quit)
    button_quit.place(x=(width/2)-100, y=(height/2)+75, width=200, height=50)

def play(): #weiterleitung zum Spiel(schließt menufenster)
    menu.destroy()
    game()

def settings():
    global width, height
    #canvas.delete("all")

    menu.title("Settings")

    canvas = Canvas(master=menu, background=textdatei("secondary_color", "null"))
    canvas.place(width=width, height=height)

    mitte = Canvas(master=menu, background=textdatei("primary_color", "null"))
    mitte.place(x=0, y=height/8, width=width, height=height-(height/4))

    mitte.create_line(width/3, 0, width/3, height-(height/4), width=10, activefill=textdatei("font_color_1", "null"))
    mitte.create_line(2*(width/3), 0, 2*(width/3), height-(height/4), width=10, activefill=textdatei("font_color_1", "null"))

    title = Label(master=menu, text="SETTINGS", fg=textdatei("font_color_1", "null"), background=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_title", "null")))
    title.place(x=width/9, y=height/16)

    filler1 = Label(master=mitte, fg=textdatei("font_color_1", "null"), background=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"),textdatei("font_size_subtitle", "null")))
    filler1.grid(row=0, column=0, padx=width/6, pady=10, sticky="nesw")
    filler2 = Label(master=mitte, fg=textdatei("font_color_1", "null"), background=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"),textdatei("font_size_subtitle", "null")))
    filler2.grid(row=0, column=1, padx=width/6, pady=10, sticky="nesw")

    subtitle_gameplay = Label(master=mitte, text="GAMEPLAY", fg=textdatei("font_color_1", "null"), background=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"),textdatei("font_size_subtitle", "null")))
    subtitle_gameplay.grid(row=0, column=0, padx=width/12, pady=10, sticky="nesw")
    subtitle_keybinds = Label(master=mitte, text="KEYBINDS", fg=textdatei("font_color_1", "null"), background=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"),textdatei("font_size_subtitle", "null")))
    subtitle_keybinds.grid(row=0, column=1, padx=width/12, pady=10, sticky="nesw")
    subtitle_customization = Label(master=mitte, text="CUSTOMIZATION", fg=textdatei("font_color_1", "null"), background=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"),textdatei("font_size_subtitle", "null")))
    subtitle_customization.grid(row=0, column=2, padx=width/12, pady=10, sticky="nesw")
    


#def quit(): #Beendet das Spiel
    #menu.destroy()
    #quit()


def close(): #um das bearbeiten angenehmer zu gestalten
    menu.destroy()



menu = Tk()
menu.title("Menu")
menu.attributes("-fullscreen", True)

width = menu.winfo_screenwidth()
height = menu.winfo_screenheight()

canvas = Canvas()

menu.after(5000, close)
mainmenu()


menu.mainloop()

