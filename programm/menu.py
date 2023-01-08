from game import game
from functions import *
from tkinter import *


def mainmenu():
    canvas = Canvas(master=menu, background=textdatei("primary_color", "null"))
    canvas.place(width=width, height=height)

    button_play = Button(master=menu, text="Play", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=play)
    button_play.place(x=(width/2)-100, y=(height/2)-75, width=200, height=50)

    button_settings = Button(master=menu, text="SETTINGS", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=settings)
    button_settings.place(x=(width/2)-100, y=(height/2), width=200, height=50)

    button_quit = Button(master=menu, text="QUIT", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=quit)
    button_quit.place(x=(width/2)-100, y=(height/2)+75, width=200, height=50)

def play(): #weiterleitung zum Spiel(schließt menufenster)
    menu.destroy()
    game()

def settings():
    def gameplay():
        number_of_bots = Label(mitte, text="Anzahl der Bots: " + str(textdatei("number_of_bots", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        number_of_bots.grid(row=1, column=0, padx=10, pady=(width/100), sticky="nesw")

        nob_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))-1), gameplay()])
        nob_decr.grid(row=1, column=1, padx=width/16, pady=(width/100), sticky="w")
        if textdatei("number_of_bots", "null") == "1":
            nob_decr.config(state="disabled")

        nob_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))+1), gameplay()])
        nob_incr.grid(row=1, column=1, padx=width/16, pady=(width/100), sticky="e")
        if cards_check("number_of_bots") == "False" or textdatei("number_of_bots", "null") == "3":
            nob_incr.config(state="disabled")
        
        
        number_of_cards = Label(mitte, text="Karten zu Beginn: " + str(textdatei("number_of_cards", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        number_of_cards.grid(row=2, column=0, padx=10, pady=(width/100), sticky="nesw")

        noc_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_cards", int(textdatei("number_of_cards", "null"))-1), gameplay()])
        noc_decr.grid(row=2, column=1, padx=width/16, pady=(width/100), sticky="w")
        if textdatei("number_of_cards", "null") == "1":
            noc_decr.config(state="disabled")

        noc_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_cards", int(textdatei("number_of_cards", "null"))+1), gameplay()])
        noc_incr.grid(row=2, column=1, padx=width/16, pady=(width/100), sticky="e")
        if cards_check("number_of_cards") == "False" or textdatei("number_of_cards", "null") == "12":
            noc_incr.config(state="disabled")


        colors = Label(mitte, text="Anzahl der Farben:  " + str(textdatei("colors", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        colors.grid(row=3, column=0, padx=10, pady=(width/100), sticky="nesw")

        clr_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("colors", int(textdatei("colors", "null"))-1), gameplay()])
        clr_decr.grid(row=3, column=1, padx=width/16, pady=(width/100), sticky="w")
        if cards_check("colors") == "False" or textdatei("colors", "null") == "3":
            clr_decr.config(state="disabled")

        clr_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("colors", int(textdatei("colors", "null"))+1), gameplay()])
        clr_incr.grid(row=3, column=1, padx=width/16, pady=(width/100), sticky="e")
        if textdatei("colors", "null") == "5":
            clr_incr.config(state="disabled")
        
        #specialcards = Label(mitte, text="Sonderkarten", fg=textdatei("font_color_1", "null"), background=textdatei("color_3", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        #specialcards.grid(row=3, column=0, padx=10, pady=10, sticky="nesw")
        #spcards = StringVar(value=textdatei("special_cards", "null"))
        #print(spcards)
        #specialcards_checkbutton = Checkbutton(mitte, anchor="center", width=2, offvalue="False", onvalue="True", variable=spcards, command=lambda: [textdatei("special_cards", spcards), settings()])
        #specialcards_checkbutton.grid(row=3, column=1, padx=10, pady=10, sticky="nesw")

    def keybinds():
        def save():
            textdatei("kb_take", kb_take_set.get())
            textdatei("kb_back_to_menu", kb_back_to_menu_set.get())
            textdatei("kb_place_card_1", kb_place_card_1_set.get())
            textdatei("kb_place_card_2", kb_place_card_2_set.get())
            textdatei("kb_place_card_3", kb_place_card_3_set.get())
            textdatei("kb_place_card_4", kb_place_card_4_set.get())
            textdatei("kb_place_card_5", kb_place_card_5_set.get())
            textdatei("kb_place_card_6", kb_place_card_6_set.get())

        kb_take = Label(mitte, text="Nachziehen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_take.grid(row=1, column=2, padx=10, pady=(width/100), sticky="nesw")
        kb_take_set = Entry(mitte, width=1, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_take_set.grid(row=1, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_take_set.insert(0, textdatei("kb_take", "null"))

        kb_back_to_menu = Label(mitte, text="Spiel abbrechen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_back_to_menu.grid(row=2, column=2, padx=10, pady=(width/100), sticky="nesw")
        kb_back_to_menu_set = Entry(mitte, width=1, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_back_to_menu_set.grid(row=2, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_back_to_menu_set.insert(0, textdatei("kb_back_to_menu", "null"))

        for i in range(1,7):
            m_label = Label(mitte, text=f"Karte {i} legen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
            m_label.grid(row=i+2, column=2, padx=10, pady=(width/100), sticky="nesw")
            
        kb_place_card_1_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_1_set.grid(row=3, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_1_set.insert(0, textdatei("kb_place_card_1", "null"))

        kb_place_card_2_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_2_set.grid(row=4, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_2_set.insert(0, textdatei("kb_place_card_2", "null"))

        kb_place_card_3_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_3_set.grid(row=5, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_3_set.insert(0, textdatei("kb_place_card_3", "null"))

        kb_place_card_4_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_4_set.grid(row=6, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_4_set.insert(0, textdatei("kb_place_card_4", "null"))   

        kb_place_card_5_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_5_set.grid(row=7, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_5_set.insert(0, textdatei("kb_place_card_5", "null"))

        kb_place_card_6_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_6_set.grid(row=8, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_6_set.insert(0, textdatei("kb_place_card_6", "null"))
        
        kb_save = Button(mitte, text="Save", fg=textdatei("font_color_1", "null"), bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")), command=save)
        kb_save.grid(row=10, column=2, columnspan=2, padx=width/10, pady=(width/100), sticky="ew")


    def customization():
        primary_color = Label(mitte, text="Primärfarbe:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        primary_color.grid(row=1, column=4, padx=10, pady=(width/100), sticky="nesw")

        primary_color_grey = Button(mitte, width=2, bg="grey", command=lambda: [textdatei("primary_color", "grey"), settings()])
        primary_color_grey.grid(row=1, column=5, padx=0, pady=(width/100), sticky="w")

        primary_color_darkgreen = Button(mitte, width=2, bg="darkgreen", command=lambda: [textdatei("primary_color", "darkgreen"), settings()])
        primary_color_darkgreen.grid(row=1, column=5, padx=30, pady=(width/100), sticky="w")

        primary_color_darkblue = Button(mitte, width=2, bg="darkblue", command=lambda: [textdatei("primary_color", "darkblue"), settings()])
        primary_color_darkblue.grid(row=1, column=5, padx=60, pady=(width/100), sticky="w")

        primary_color_purple = Button(mitte, width=2, bg="purple", command=lambda: [textdatei("primary_color", "purple"), settings()])
        primary_color_purple.grid(row=1, column=5, padx=30, pady=(width/100), sticky="e")

        primary_color_orange = Button(mitte, width=2, bg="orange", command=lambda: [textdatei("primary_color", "orange"), settings()])
        primary_color_orange.grid(row=1, column=5, padx=0, pady=(width/100), sticky="e")

        
        secondary_color = Label(mitte, text="Sekundärfarbe:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        secondary_color.grid(row=2, column=4, padx=10, pady=(width/100), sticky="nesw")

        secondary_color_grey = Button(mitte, width=2, bg="grey", command=lambda: [textdatei("secondary_color", "grey"), settings()])
        secondary_color_grey.grid(row=2, column=5, padx=0, pady=(width/100), sticky="w")

        secondary_color_darkgreen = Button(mitte, width=2, bg="darkgreen", command=lambda: [textdatei("secondary_color", "darkgreen"), settings()])
        secondary_color_darkgreen.grid(row=2, column=5, padx=30, pady=(width/100), sticky="w")

        secondary_color_white = Button(mitte, width=2, bg="white", command=lambda: [textdatei("secondary_color", "white"), settings()])
        secondary_color_white.grid(row=2, column=5, padx=60, pady=(width/100), sticky="w")
    
        secondary_color_blue = Button(mitte, width=2, bg="blue", command=lambda: [textdatei("secondary_color", "blue"), settings()])
        secondary_color_blue.grid(row=2, column=5, padx=30, pady=(width/100), sticky="e")

        secondary_color_yellow = Button(mitte, width=2, bg="yellow", command=lambda: [textdatei("secondary_color", "yellow"), settings()])
        secondary_color_yellow.grid(row=2, column=5, padx=0, pady=(width/100), sticky="e")

    menu.title("Settings")

    canvas = Canvas(menu, background=textdatei("secondary_color", "null"))
    canvas.place(width=width, height=height)

    mitte = Canvas(menu, background="grey") #textdatei("primary_color", "null"))
    mitte.place(x=0, y=height/8, width=width, height=height-(height/4))
    
    title = Label(menu, text="SETTINGS", fg=textdatei("font_color_1", "null"), background=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_title", "null")))
    title.place(x=width/9, y=height/16)

    mitte.create_line((width/3), 0, (width/3), (height-(height/4)), width=10, activefill=textdatei("font_color_1", "null"))
    mitte.create_line((2*(width/3)), 0, (2*(width/3)), (height-(height/4)), width=10, activefill=textdatei("font_color_1", "null"))

    for i in range(9):
        if i < 5:
            mitte.columnconfigure(i, minsize=width/6)#weight=width)
        mitte.rowconfigure(i, minsize=(height-height/4)/10)
    
    subtitle_frame = Frame(mitte, height=30, bg=textdatei("primary_color", "null"))
    subtitle_frame.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nesw")

    subtitle_gameplay = Label(mitte, text="GAMEPLAY", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_gameplay.place(x=25, y=10, width=(width/3)-50)
    subtitle_keybinds = Label(mitte, text="KEYBINDS", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_keybinds.place(x=(width/3)+25, y=10, width=(width/3)-50)
    subtitle_customization = Label(mitte, text="CUSTOMIZATION", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_customization.place(x=(2*(width/3))+25, y=10, width=(width/3)-50)

    back = Button(canvas, text="ZURÜCK", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")), command=mainmenu)
    back.place(x=width/9, y=height-(height/12))


    gameplay()
    keybinds()
    customization()


def close(): #um das bearbeiten angenehmer zu gestalten
    menu.destroy()



menu = Tk()
menu.title("Letzte Karte")
menu.attributes("-fullscreen", True)

width = menu.winfo_screenwidth()
height = menu.winfo_screenheight()

canvas = Canvas()

#menu.after(5000, close)
mainmenu()


menu.mainloop()


