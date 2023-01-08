# "Letzte Karte"-Menu von Amos
from game import game, back_to_menu
from functions import textdatei, cards_check
from tkinter import *

#Erstellt Tkinter-Fenster
def tk_menu():
    global width, height, menu

    menu = Tk()
    menu.title("Letzte Karte") #menu-Titel wird gesetzt/geändert
    menu.attributes("-fullscreen", True) #menufenster wird im Vollbild erstellt

    #width und height sind die Werte an denen sich der gesamte Aufbau orientiert.
    width = menu.winfo_screenwidth()
    height = menu.winfo_screenheight()

    canvas = Canvas()
    #Failsafe für den Fall dass das Programm in einer Schleife steckt, oder sonst irgendwie buggt.
    menu.bind('<KeyPress-End>', quit)

    #menu.after(5000, close) #macht das bearbeiten um einiges angehnemer.
    mainmenu()  #ruft Startseite auf
    menu.mainloop()

#Startseite
def mainmenu():
    #Canvas wird für Startseite Kofiguriert
    canvas = Canvas(master=menu, background=textdatei("primary_color", "null"))
    canvas.place(width=width, height=height)

    #Titel
    title = Label(menu, text="Letzte Karte", fg=textdatei("font_color_1", "null"), background=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), 40))
    title.place(x=width/4, y=height/16, width=width/2)

    #Regeln
    rules = Label(canvas, text="Wie Funktioniert Letzte Karte?", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    rules.place(x=width/4, y=(height/6), width=width/2)

    #Label für Spielregeln
    rules_text = Label(canvas, text="""Die Regeln sind Simple af.
    Dein Ziel ist es als erster alle deine Karten los zu werden.
    Jede Runde kannst du eine passende Karte aus deiner Hand ablegen.
    Eine ist passend, wenn sie die gleiche Farbe oder die gleiche Zahl
    wie die oberste Karte auf dem Ablagestapel hat. Wenn du keine passende 
    Karte hast, musst du solange vom Ablagestapel ziehen, bist du eine
    passesnde Karte gezogen hast. Wenn du gelegt hast sind reiherum alle 
    Bots an der Reihe.
    In den Setting kannst du Aspekte des Spiels anpassen.""", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
    rules_text.place(x=(width/4), y=height/5, width=(width/2))

    #Button zum starten des Spiels
    button_play = Button(master=menu, text="Play", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=play)
    button_play.place(x=(width/2)-100, y=(height/2)-75, width=200, height=50)
    #Button zur weiterleitung zu den Einstellungen
    button_settings = Button(master=menu, text="SETTINGS", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=settings)
    button_settings.place(x=(width/2)-100, y=(height/2), width=200, height=50)
    #Button zum beenden des Spiels
    button_quit = Button(master=menu, text="QUIT", bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=quit)
    button_quit.place(x=(width/2)-100, y=(height/2)+75, width=200, height=50)

def play(): #weiterleitung zum Spiel(schließt menufenster)
    global menu
    menu.destroy()
    game()
    #menu.after(5000, quit)
    #fragt so lange back_to_menu-Funktion ab, bis diese False ausgibt.
    while back_to_menu() == True:
        pass
    #sobald dass der Fall ist (das Spiel wurde geschlossen), wird die Startseite aufgerufen
    tk_menu()
            
#Einstellungen
def settings():
    def gameplay(): #Konfiguriert den Abschnitt Gameplay in den Einstellungen.
        #Erstellt ein Label zum anzeigen der aktuellen Anzahl an Bots, welche aus der txt ausgelesen wird.
        number_of_bots = Label(mitte, text="Anzahl der Bots: " + str(textdatei("number_of_bots", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        number_of_bots.grid(row=1, column=0, padx=10, pady=(width/100), sticky="nesw")

        #trägt die aktuelle Anzahl an Bots -1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        nob_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))-1), gameplay()])
        nob_decr.grid(row=1, column=1, padx=width/16, pady=(width/100), sticky="w")
        #Prüft die aktuelle Anzahl der Bots und deaktiviert den Button, wenn diese nicht weiter verringert werden darf.
        if textdatei("number_of_bots", "null") == "1":
            nob_decr.config(state="disabled")
        
        #trägt die aktuelle Anzahl an Bots +1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        nob_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_bots", int(textdatei("number_of_bots", "null"))+1), gameplay()])
        nob_incr.grid(row=1, column=1, padx=width/16, pady=(width/100), sticky="e")
        #Prüft in cards_check-Funktion ob die Verteilung der Karten aufgeht wenn der Button betätigt wird (die Anzahl der Bots erhöht wird), sowie die aktuelle Anzahl der Bots und deaktiviert den button entsprechend.
        if cards_check("number_of_bots") == "False" or textdatei("number_of_bots", "null") == "3":
            nob_incr.config(state="disabled")
        

        #Erstellt ein Label zum anzeigen der aktuellen Anzahl an Karten die Spieler und Bots zu beginn auf der Hand haben, welche aus der txt ausgelesen wird.
        number_of_cards = Label(mitte, text="Karten zu Beginn: " + str(textdatei("number_of_cards", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        number_of_cards.grid(row=2, column=0, padx=10, pady=(width/100), sticky="nesw")

        #trägt die aktuelle Anzahl an Karten -1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        noc_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_cards", int(textdatei("number_of_cards", "null"))-1), gameplay()])
        noc_decr.grid(row=2, column=1, padx=width/16, pady=(width/100), sticky="w")

        #Prüft die aktuelle Anzahl der Karten und deaktiviert den Button, wenn diese nicht weiter verringert werden darf.
        if textdatei("number_of_cards", "null") == "1":
            noc_decr.config(state="disabled")

        #trägt die aktuelle Anzahl an Karten +1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        noc_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("number_of_cards", int(textdatei("number_of_cards", "null"))+1), gameplay()])
        noc_incr.grid(row=2, column=1, padx=width/16, pady=(width/100), sticky="e")

        #Prüft in cards_check-Funktion ob die Verteilung der Karten aufgeht wenn der Button betätigt wird (die Anzahl der Karten erhöht wird), sowie die aktuelle Anzahl der Karten und deaktiviert den button entsprechend.
        if cards_check("number_of_cards") == "False" or textdatei("number_of_cards", "null") == "12":
            noc_incr.config(state="disabled")


        #Erstellt ein Label zum anzeigen der aktuellen Anzahl an Farben mit denen gespielt wird, welche aus der txt ausgelesen wird.
        colors = Label(mitte, text="Anzahl der Farben:  " + str(textdatei("colors", "null")), fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        colors.grid(row=3, column=0, padx=10, pady=(width/100), sticky="nesw")

        #trägt die aktuelle Anzahl an Farben -1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        clr_decr = Button(mitte, text="-", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("colors", int(textdatei("colors", "null"))-1), gameplay()])
        clr_decr.grid(row=3, column=1, padx=width/16, pady=(width/100), sticky="w")

        #Prüft in Funktion ob die Verteilung der Karten aufgeht wenn der Button betätigt wird (die Anzahl der Farben und damit die anzahl der Karten im Spiel verringert wird), sowie die aktuelle Anzahl der Farben und deaktiviert den button entsprechend.
        if cards_check("colors") == "False" or textdatei("colors", "null") == "3":
            clr_decr.config(state="disabled")

        #trägt die aktuelle Anzahl an Farben +1 in die txt ein und ruft die Funktion gameplay zum aktalisieren der Label und Buttons auf.
        clr_incr = Button(mitte, text="+", width=2, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")), command=lambda: [textdatei("colors", int(textdatei("colors", "null"))+1), gameplay()])
        clr_incr.grid(row=3, column=1, padx=width/16, pady=(width/100), sticky="e")

        #Prüft die aktuelle Anzahl der Karten und deaktiviert den Button, wenn diese nicht weiter erhöht werden darf.
        if textdatei("colors", "null") == "5":
            clr_incr.config(state="disabled")
        
    
    def keybinds(): #Konfiguriert den Abschnitt Keybinds in den Einstellungen.
        #trägt den in die Entry-Felder eingetragenen inhalt in die txt um ihn zu speichen.
        def save(): 
            textdatei("kb_take", kb_take_set.get())
            textdatei("kb_back_to_menu", kb_back_to_menu_set.get())
            textdatei("kb_place_card_1", kb_place_card_1_set.get())
            textdatei("kb_place_card_2", kb_place_card_2_set.get())
            textdatei("kb_place_card_3", kb_place_card_3_set.get())
            textdatei("kb_place_card_4", kb_place_card_4_set.get())
            textdatei("kb_place_card_5", kb_place_card_5_set.get())
            textdatei("kb_place_card_6", kb_place_card_6_set.get())

        #Erstellt ein Label.
        kb_take = Label(mitte, text="Nachziehen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_take.grid(row=1, column=2, padx=10, pady=(width/100), sticky="nesw")
        #Erstellt ein Eingabefeld in dem man den in der txt gespeicherten Keybind ändern kann.
        kb_take_set = Entry(mitte, width=1, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_take_set.grid(row=1, column=3, padx=10, pady=(width/100), sticky="nesw")
        #tragt den in der txt gespeicherten Wert in das Eingabefeld ein.
        kb_take_set.insert(0, textdatei("kb_take", "null"))

        #Erstellt noch ein Label.
        kb_back_to_menu = Label(mitte, text="Spiel abbrechen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_back_to_menu.grid(row=2, column=2, padx=10, pady=(width/100), sticky="nesw")
        #Erstellt ein Eingabefeld in dem man den in der txt gespeicherten Keybind ändern kann.
        kb_back_to_menu_set = Entry(mitte, width=1, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_back_to_menu_set.grid(row=2, column=3, padx=10, pady=(width/100), sticky="nesw")
        #tragt den in der txt gespeicherten Wert in das Eingabefeld ein.
        kb_back_to_menu_set.insert(0, textdatei("kb_back_to_menu", "null"))

        #Erstellt 6 weitere Label für die Keybinds zum legen der Karten 1-6 in aufeinander folgenden grid-Zellen.
        for i in range(1,7):
            m_label = Label(mitte, text=f"Karte {i} legen:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
            m_label.grid(row=i+2, column=2, padx=10, pady=(width/100), sticky="nesw")
        
        #Erstellt ein Eingabefeld und trägt einen Wert in dieses ein.
        kb_place_card_1_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_1_set.grid(row=3, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_1_set.insert(0, textdatei("kb_place_card_1", "null"))

        #Erstellt noch ein Eingabefeld und trägt einen Wert in dieses ein.
        kb_place_card_2_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_2_set.grid(row=4, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_2_set.insert(0, textdatei("kb_place_card_2", "null"))

        #Erstellt ein weiteres Eingabefeld und ... .
        kb_place_card_3_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_3_set.grid(row=5, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_3_set.insert(0, textdatei("kb_place_card_3", "null"))

        #Erstellt noch eins.
        kb_place_card_4_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_4_set.grid(row=6, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_4_set.insert(0, textdatei("kb_place_card_4", "null"))   

        #Und noch eins.
        kb_place_card_5_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_5_set.grid(row=7, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_5_set.insert(0, textdatei("kb_place_card_5", "null"))

        #Und noch eins.
        kb_place_card_6_set = Entry(mitte, bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        kb_place_card_6_set.grid(row=8, column=3, padx=10, pady=(width/100), sticky="nesw")
        kb_place_card_6_set.insert(0, textdatei("kb_place_card_6", "null"))
        
        #Erstellt einen Button der die save- und die keybinds-Funktion aufruft.
        kb_save = Button(mitte, text="Save", fg=textdatei("font_color_1", "null"), bg=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")), command=lambda: [save(), keybinds()])
        kb_save.grid(row=10, column=2, columnspan=2, padx=width/10, pady=(width/100), sticky="ew")


    def customization(): #Konfiguriert den Abschnitt Customization.
        #Erstellt ein Label
        primary_color = Label(mitte, text="Primärfarbe:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        primary_color.grid(row=1, column=4, padx=10, pady=(width/100), sticky="nesw")

        #Erstellt 5 Buttons die bei Betätigung je eine farbe als Primärfarbe in die txt eintragen und anschließend mit dem Funktionsaufruf settings das Fenster neu laden.
        #1
        primary_color_grey = Button(mitte, width=2, bg="grey", command=lambda: [textdatei("primary_color", "grey"), settings()])
        primary_color_grey.grid(row=1, column=5, padx=0, pady=(width/100), sticky="w")
        #2
        primary_color_darkgreen = Button(mitte, width=2, bg="darkgreen", command=lambda: [textdatei("primary_color", "darkgreen"), settings()])
        primary_color_darkgreen.grid(row=1, column=5, padx=30, pady=(width/100), sticky="w")
        #3
        primary_color_darkblue = Button(mitte, width=2, bg="darkblue", command=lambda: [textdatei("primary_color", "darkblue"), settings()])
        primary_color_darkblue.grid(row=1, column=5, padx=60, pady=(width/100), sticky="w")
        #4
        primary_color_purple = Button(mitte, width=2, bg="purple", command=lambda: [textdatei("primary_color", "purple"), settings()])
        primary_color_purple.grid(row=1, column=5, padx=30, pady=(width/100), sticky="e")
        #5
        primary_color_orange = Button(mitte, width=2, bg="orange", command=lambda: [textdatei("primary_color", "orange"), settings()])
        primary_color_orange.grid(row=1, column=5, padx=0, pady=(width/100), sticky="e")

        #Und das selbe nochmal für die Sekundärfarbe
        secondary_color = Label(mitte, text="Sekundärfarbe:", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_text", "null")))
        secondary_color.grid(row=2, column=4, padx=10, pady=(width/100), sticky="nesw")
        #1
        secondary_color_grey = Button(mitte, width=2, bg="grey", command=lambda: [textdatei("secondary_color", "grey"), settings()])
        secondary_color_grey.grid(row=2, column=5, padx=0, pady=(width/100), sticky="w")
        #2
        secondary_color_darkgreen = Button(mitte, width=2, bg="darkgreen", command=lambda: [textdatei("secondary_color", "darkgreen"), settings()])
        secondary_color_darkgreen.grid(row=2, column=5, padx=30, pady=(width/100), sticky="w")
        #3
        secondary_color_white = Button(mitte, width=2, bg="white", command=lambda: [textdatei("secondary_color", "white"), settings()])
        secondary_color_white.grid(row=2, column=5, padx=60, pady=(width/100), sticky="w")
        #4
        secondary_color_blue = Button(mitte, width=2, bg="blue", command=lambda: [textdatei("secondary_color", "blue"), settings()])
        secondary_color_blue.grid(row=2, column=5, padx=30, pady=(width/100), sticky="e")
        #5
        secondary_color_yellow = Button(mitte, width=2, bg="yellow", command=lambda: [textdatei("secondary_color", "yellow"), settings()])
        secondary_color_yellow.grid(row=2, column=5, padx=0, pady=(width/100), sticky="e")
    
    menu.title("Settings")#Ändert den Title der Seite.

    #Konfiguriert den Canvas für die Einstellungen um.
    canvas = Canvas(menu, background=textdatei("secondary_color", "null"))
    canvas.place(width=width, height=height)
    
    #Erstellt einen zweiten Canvas zur Farblichen gestaltung
    mitte = Canvas(menu, background=textdatei("primary_color", "null"))
    mitte.place(x=0, y=height/8, width=width, height=height-(height/4))
    
    #Erstellt das Label SETTINGS
    title = Label(menu, text="SETTINGS", fg=textdatei("font_color_1", "null"), background=textdatei("secondary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_title", "null")))
    title.place(x=width/9, y=height/16)

    #Platziert 2 Linien auf zur Optischen gestaltung.
    mitte.create_line((width/3), 0, (width/3), (height-(height/4)), width=10, activefill=textdatei("font_color_1", "null"))
    mitte.create_line((2*(width/3)), 0, (2*(width/3)), (height-(height/4)), width=10, activefill=textdatei("font_color_1", "null"))

    #Konfiguriert das "Grid" mit dem der Inhalt der Einstellungen angeordnet wird.
    for i in range(9):
        #für die ersten 6 Spalten (mehr gibt es nicht) wird eine mindestbreite von 1/6 der Bildschirmbreite angeordnet.
        if i < 5:
            mitte.columnconfigure(i, minsize=width/6)
        #für die ersten 10 Zeilen (mehr gibt es nicht) wird eine mindesthöhe in höhe von 10% der höhe des mitte-canvas angeordnet
        mitte.rowconfigure(i, minsize=(height-height/4)/10)
    #Ein Frame blockiert die erste Zeile des Grid
    subtitle_frame = Frame(mitte, height=30, bg=textdatei("primary_color", "null"))
    subtitle_frame.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nesw")

    #Drei Überschriften werden erstellt und mit dem place-manager an der stelle der ersten Zeile des Grids platziert.
    subtitle_gameplay = Label(mitte, text="GAMEPLAY", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_gameplay.place(x=25, y=10, width=(width/3)-50)
    subtitle_keybinds = Label(mitte, text="KEYBINDS", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_keybinds.place(x=(width/3)+25, y=10, width=(width/3)-50)
    subtitle_customization = Label(mitte, text="CUSTOMIZATION", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")))
    subtitle_customization.place(x=(2*(width/3))+25, y=10, width=(width/3)-50)
    #Ein Button der die mainmenu-Funktion aufruft wird erstellt.
    back = Button(canvas, text="ZURÜCK", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")), command=mainmenu)
    back.place(x=width/9, y=height-(height/12))
    #Ein Button der die play-Funktion aufruft wird errstellt.
    play_settings = Button(canvas, text="Play", fg=textdatei("font_color_1", "null"), bg=textdatei("primary_color", "null"), font=(textdatei("font_1", "null"), textdatei("font_size_subtitle", "null")), command=play)
    play_settings.place(x=width-(width/9), y=height-(height/12))

    #die Funktionen zum Erstellen der drei Bereiche werden aufgerufen.
    gameplay()
    keybinds()
    customization()

#führt die erste Funktion aus
tk_menu()



