from game import game
from functions import textdatei, integrity_check
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

    mitte = Canvas(master=menu, background= "grey") #textdatei("primary_color", "null"))
    mitte.place(x=0, y=height/8, width=width, height=height-(height/4))

    mitte.create_line(width/3, 0, width/3, height-(height/4), width=10, activefill=textdatei("font_color_1", "null"))
    mitte.create_line(2*(width/3), 0, 2*(width/3), height-(height/4), width=10, activefill=textdatei("font_color_1", "null"))

    title = Label(master=menu, text="SETTINGS", fg=textdatei("font_color_1", "null"), background=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_title", "null")))
    title.place(x=width/9, y=height/16)

    for i in range(5):
        mitte.columnconfigure(i, minsize=width/6)
    
    subtitle_frame = Frame(mitte, bg=textdatei("color_3", "null"))
    subtitle_frame.grid(row=0, column=0, columnspan=6, sticky="nesw")
    subtitle_gameplay = Label(subtitle_frame, text="GAMEPLAY", fg=textdatei("font_color_1", "null"), bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_gameplay.place(x=0, y=0, width=width/3, height=20)
    subtitle_keybinds = Label(subtitle_frame, text="KEYBINDS", fg=textdatei("font_color_1", "null"), bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_keybinds.place(x=width/3, y=0, width=width/3)
    subtitle_customization = Label(subtitle_frame, text="CUSTOMIZATION", fg=textdatei("font_color_1", "null"), bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_customization.place(x=2*(width/3), y=0, width=width/3)#grid(row=0, column=2, columnspan=1, padx=0, pady=0, sticky="nesw")

    """
    test = Canvas(mitte, background=textdatei("color_3", "null"))
    test.grid(row=5, column=0)
    test1 = Canvas(mitte, background="black")
    test1.grid(row=5, column=1)
    test2 = Canvas(mitte, background=textdatei("color_3", "null"))
    test2.grid(row=5, column=2)
    test3 = Canvas(mitte, background="black")
    test3.grid(row=5, column=3)
    test4 = Canvas(mitte, background=textdatei("color_3", "null"))
    test4.grid(row=5, column=4)
    test5 = Canvas(mitte, background="black")
    test5.grid(row=5, column=5)"""

    number_of_bots = Label(mitte, text="Anzahl der Bots: " + str(textdatei("number_of_bots", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
    number_of_bots.grid(row=1, column=0, padx=10, pady=10, sticky="nesw")
    nob_decr = Button(mitte, text="-", width=2, bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))-1), settings()])
    nob_decr.grid(row=1, column=1, padx=(width/12)-20, pady=10, sticky="w")
    if int(textdatei("number_of_bots", "null")) == 1:
        nob_decr.config(state="disabled")
    nob_incr = Button(mitte, text="+", width=2, bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))+1), settings()])
    nob_incr.grid(row=1, column=1, padx=(width/12)+20, pady=10, sticky="e")
    if int(textdatei("number_of_bots", "null")) == 3:
        nob_incr.config(state="disabled")
    
    number_of_cards = Label(mitte, text="Karten zu Beginn: " + str(textdatei("number_of_cards", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
    number_of_cards.grid(row=2, column=0, padx=10, pady=10, sticky="nesw")
    noc_decr = Button(mitte, text="-", width=2, bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_cards", int(textdatei("number_of_cards", "null"))-1), settings()])
    noc_decr.grid(row=2, column=1, padx=(width/12)-20, pady=10, sticky="w")
    if int(textdatei("number_of_cards", "null")) == 1: #Eingabefeld zwischen - und +, sync?
        noc_decr.config(state="disabled")
    noc_incr = Button(mitte, text="+", width=2, bg=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [integrity_check("number_of_cards", int(textdatei("number_of_cards", "null"))+1, 1), settings()])
    noc_incr.grid(row=2, column=1, padx=(width/12)+20, pady=10, sticky="e")
    if integrity_check("number_of_cards", int(textdatei("number_of_cards", "null"))+1, 0) == "False":
        noc_incr.config(state="disabled")

    #specialcards = Label(mitte, text="Sonderkarten", fg=textdatei("font_color_1", "null"), background=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
    #specialcards.grid(row=3, column=0, padx=10, pady=10, sticky="nesw")
    #spcards = StringVar(value=textdatei("special_cards", "null"))
    #print(spcards)
    #specialcards_checkbutton = Checkbutton(mitte, anchor="center", width=2, offvalue="False", onvalue="True", variable=spcards, command=lambda: [textdatei("special_cards", spcards), settings()])
    #specialcards_checkbutton.grid(row=3, column=1, padx=10, pady=10, sticky="nesw")
    
    





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


