from tkinter import *
from random import randint
from functions import textdatei

#menu <> Auswertung?

def game(): #Gesammtfunktion die das Menu aufruft
    global hand1, hand2, hand3, hand4, ablagestapel, nachziehstapel
    global labelBot1, labelBot2, labelBot3, botsspielen, gewonnen

    #Listen
    hand1 = []
    hand2 = []
    hand3 = []
    hand4 = []
    ablagestapel = []
    nachziehstapel = []
    botsspielen = False #gibt an ob Bots gerade am Zug sind
    gewonnen = False

    #Variablen aus txt extrahiert:
    spieler = int(textdatei("number_of_bots", "null"))+1
    kartenaufnehmen = int(textdatei("number_of_cards", "null")) #Karten mit denen jeder Spieler startet
    primary_color = textdatei("primary_color", "null")
    secondary_color = textdatei("secondary_color", "null")
    font_color_1 = textdatei("font_color_1", "null")
    maximalekarten = 20 #10-20
    anzahlfarben = int(textdatei("colors", "null"))

    def aufnahmestapelerstellen():
        if anzahlfarben < 4: #Zwischen 3 Farbsets wird ausgewählt
            farben = ["blue", "red", "green"]
        elif anzahlfarben == 4:
            farben = ["yellow", "blue", "red", "green"]
        else: 
            farben = ["cyan", "yellow", "blue", "red", "green"]   
        zahlen = [0, 1, 2, 3, 4, 5, 6, 7]
        #Liste der einzelnen Zahlen und Farben
        global nachziehstapel
        for i in range(len(farben)):
            for y in range(len(zahlen)):
                nachziehstapel = nachziehstapel + [[farben[i], zahlen[y]]] + [[farben[i], zahlen[y]]] 
                #erstellt jede mögliche Karte 2 mal
        print(f"Der Nachziehstapel wird erstellt: {nachziehstapel}")

    def erstekarte(): #eine erste Karte muss als Grundlage gelegt werden
        global nachziehstapel, ablagestapel
        random = randint(0, len(nachziehstapel)-1) #random Zahl für die zugehörige Karte
        ablagestapel = [nachziehstapel[random]] #Karte wird auf Ablagestapel gelegt
        nachziehstapel.pop(random) #Karte wird aus Nachziehstapel gelöscht
        #Die Karte wird plaziert:
        temp = width/2
        canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
        canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
        print(f"Als Grundlage wurde die {random}. Karte wurde ausgewählt: {ablagestapel}")

    def haende():
        for i in range(kartenaufnehmen): #aufzunehmende Karten für Spielstart werden aufgenommen
            aufnehmen(1)
            if spieler > 1:
                aufnehmen(2)
            if spieler > 2:
                aufnehmen(3)
            if spieler > 3:
                aufnehmen(4)

    def aufnehmen1e(event): #Funktion für Tastendruck
        aufnehmen(1) #Befehl zur Aufnahme einer Karte wird weitergegeben
    def aufnehmen1(): #Funktion für Button
        aufnehmen(1) #Befehl zur Aufnahme einer Karte wird weitergegeben

    def aufnehmen(hand):
        global labelBot1, labelBot2, labelBot3
        global nachziehstapel, hand1, hand2, hand3, hand4
        if (botsspielen == False and gewonnen == False) or hand > 1: #Testet ob Spieler dran ist oder der Bot zug ausführt
            print(f"Der Stapel hat {len(nachziehstapel)} Karten")
            if len(nachziehstapel) == 0: #prüft ob noch Karten auf dem Stapel sind
                stapelerneuern() #Im falle würde er den Stapel neu mischen
            random = randint(0, len(nachziehstapel)-1) #eine zufällige Karte wird Ausgewählt
            print(f"Die Karte {nachziehstapel[random]} wird von Spieler {hand} aufgenommen")
            #Es wird geprüft, welcher Spieler aufnimmt
            if hand == 1:
                hand1 = hand1 + [nachziehstapel[random]] #Die ausgewählte Karte wird zur Liste hinzugefügt
                ordnen()# Die Hand des Spielers wird neu geordnet
            if hand == 2:
                hand2 = hand2 + [nachziehstapel[random]]
                labelBot1.config(text=f"Bot1:\n{len(hand2)}") #Anzeige für Spieler
            if hand == 3:
                hand3 = hand3 + [nachziehstapel[random]]
                labelBot2.config(text=f"Bot2:\n{len(hand3)}") #Anzeige für Spieler
            if hand == 4:
                hand4 = hand4 + [nachziehstapel[random]]
                labelBot3.config(text=f"Bot3:\n{len(hand4)}") #Anzeige für Spieler
            nachziehstapel.pop(random) #Karte wird aus Nachziehstapel entfernt

    #Wenn der Stapel leer ist werden die bereits gelegten karten wieder untergemischt:
    def stapelerneuern():
        global nachziehstapel, ablagestapel
        nachziehstapel = ablagestapel[1:] #alle außer die oberste Karte des Ablagestapel werden kopiert
        ablagestapel = [ablagestapel[0]] #und dann aus dem Ablagestapel entfernt
        print(f"Der Stapel wird erneuert:\n{nachziehstapel}\nübrig ist jetzt: {ablagestapel}")
        canvas.delete("all") #Optischer Stapel wird entfernt
        #übrige Karte wird in GUI plaziert:
        tempx = randint(width/2-20, width/2+20) #Random Versatz für "Stapel-Look"
        tempy = randint(height/2-30, height/2+30) 
        canvas.create_rectangle(tempx-75, tempy-125, tempx+75, tempy+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
        canvas.create_text(tempx, tempy, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert 

    #weitergabe commands Tastendrucke:
    def legen1(event): 
        legen(0)
    def legen2(event):
        legen(1)
    def legen3(event): 
        legen(2)
    def legen4(event):
        legen(3)
    def legen5(event):
        legen(4)
    def legen6(event):
        legen(5)
    def legen7(event):
        legen(6)
    def legen8(event):
        legen(7)
    def legen9(event):
        legen(8)
    def legen10(event):
        legen(9)

    #gewünschte karte legen (Spieler 1):
    def legen(karte): #Karte = (Index)
        global ablagestapel, hand1, botsspielen
        if botsspielen == False: #Testet ob Spieler dran ist
            if ablagestapel[0][0] == hand1[karte][0] or ablagestapel[0][1] == hand1[karte][1]: #Überprüfen, ob Karte gelegt werden darf
                print(f"die {karte}. Karte wurde gelegt: {hand1[karte]}")
                ablagestapel = [hand1[karte]] + ablagestapel #Karte vorne auf den Ablagestapel
                hand1.pop(karte) #Karte aus Hand gelöscht
                #Karte wird in GUI plaziert
                tempx = randint(width/2-20, width/2+20) #Random Versatz für "Stapel-Look"
                tempy = randint(height/2-30, height/2+30) 
                canvas.create_rectangle(tempx-75, tempy-125, tempx+75, tempy+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(tempx, tempy, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                ordnen() #Hand wird neu geordnet
                if spieler > 1 and gewonnen == False: #Überprüfen, ob Bots dran sind
                    labelAnzeige.config(text="Die Bots spielen!") #Benachrichtigung für Spieler
                    botsspielen = True #Buttons werden gespeert
                    tkFenster.after(1000, zugbot1) #Weitergabe an Bots
            else: 
                labelAnzeige.config(text="Diese Karte kannst du nicht legen!")
                print(f"Du kannst deine  {karte}. Karte {hand1[karte]} nicht legen!")
            #Benachrichtigung für Spieler, falls ungültiger Zug

    def ordnen():
        global gewonnen 
        gewonnen = False
        #neuer Frame wird für die Hand erstellt
        framedeck = Frame(master=tkFenster, background=primary_color)
        framedeck.place(y=height-250, width=width, height=250)
        print(f"deine {len(hand1)} Karten werden neu sotiert")
        #Abstände werden neu berechnet:
        if len(hand1) > 0: 
            index = width / (len(hand1)) 
            x0 = (index/2)-75 
            #x1 = x0 + 150 #Abstände werden neu berechnet
            for i in range(len(hand1)): #Karten werden plaziert
                #Sie sind Buttons, damit man sie durch einen Klick legen kann
                if i == 0:  #Es müssen immer neue Buttons erstellt werden, da sonst der command überschrieben wird
                    button_Karte1 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(0))
                    button_Karte1.place(x=x0, y=0, width=150, height=250)
                elif i == 1:
                    button_Karte2 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(1))
                    button_Karte2.place(x=x0, y=0, width=150, height=250)
                elif i == 2:
                    button_Karte3 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(2))
                    button_Karte3.place(x=x0, y=0, width=150, height=250)
                elif i == 3:
                    button_Karte4 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(3))
                    button_Karte4.place(x=x0, y=0, width=150, height=250)
                elif i == 4:
                    button_Karte5 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(4))
                    button_Karte5.place(x=x0, y=0, width=150, height=250)
                elif i == 5:
                    button_Karte6 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(5))
                    button_Karte6.place(x=x0, y=0, width=150, height=250)
                elif i == 6:
                    button_Karte7 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(6))
                    button_Karte7.place(x=x0, y=0, width=150, height=250)
                elif i == 7:
                    button_Karte8 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(7))
                    button_Karte8.place(x=x0, y=0, width=150, height=250)
                elif i == 8:
                    button_Karte9 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(8))
                    button_Karte9.place(x=x0, y=0, width=150, height=250)
                elif i == 9:
                    button_Karte10 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(9))
                    button_Karte10.place(x=x0, y=0, width=150, height=250)
                elif i == 10:
                    button_Karte11 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(10))
                    button_Karte11.place(x=x0, y=0, width=150, height=250)
                elif i == 11:
                    button_Karte12 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(11))
                    button_Karte12.place(x=x0, y=0, width=150, height=250)
                elif i == 12:
                    button_Karte13 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(12))
                    button_Karte13.place(x=x0, y=0, width=150, height=250)
                elif i == 13:
                    button_Karte14 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(13))
                    button_Karte14.place(x=x0, y=0, width=150, height=250)
                elif i == 14:
                    button_Karte15 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(14))
                    button_Karte15.place(x=x0, y=0, width=150, height=250)
                elif i == 15:
                    button_Karte16 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(15))
                    button_Karte16.place(x=x0, y=0, width=150, height=250)
                elif i == 16:
                    button_Karte17 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(16))
                    button_Karte17.place(x=x0, y=0, width=150, height=250)
                elif i == 17:
                    button_Karte18 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(17))
                    button_Karte18.place(x=x0, y=0, width=150, height=250)
                elif i == 18:
                    button_Karte19 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(18))
                    button_Karte19.place(x=x0, y=0, width=150, height=250)
                elif i == 19:
                    button_Karte20 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(19))
                    button_Karte20.place(x=x0, y=0, width=150, height=250)
                if i == maximalekarten: #Verlierbedingung
                        labelAnzeige.config(text="Du hast veloren, wegen zu vielen Karten auf der Hand!") #Velust wird dem Spieler angezeigt
                        gewonnen = True # Zustand, damit Bots nicht mehr weiterspielen
                        return
                x0 += index
        else: #wenn keine Karten mehr auf der Hand sind (Gewinnbedingung)
            labelAnzeige.config(text="Du hast gewonnen!") #Gewinn wird angezeigt
            gewonnen = True

    def zugbot1():
        #print("Bot1:")
        global ablagestapel, hand2, botsspielen
        gelegt = False
        if len(hand2) != 0:
            for i in range(len(hand2)): #versucht alle Karten zu legen
                if ablagestapel[0][0] == hand2[i][0] or ablagestapel[0][1] == hand2[i][1]: #Überprüfen, ob Karte gelegt werden darf
                    print(f"der Bot 1 hat {hand2[i]} gelegt")
                    ablagestapel = [hand2[i]] + ablagestapel #Karte vorne auf den Ablagestapel
                    hand2.pop(i) #Karte aus Hand gelöscht
                    #Karte wird in GUI plaziert:
                    tempx = randint(width/2-20, width/2+20) #Random Versatz für "Stapel-Look"
                    tempy = randint(height/2-30, height/2+30) 
                    canvas.create_rectangle(tempx-75, tempy-125, tempx+75, tempy+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                    canvas.create_text(tempx, tempy, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert 
                    labelBot1.config(text=f"Bot1:\n{len(hand2)}")
                    gelegt = True
                    if len(hand2) == 0: #überprüft, ob der Bot noch Karten hat
                        labelAnzeige.config(text="Bot 1 ist Fertig!") #Benachrichtigung für Spieler
                        if (len(hand3) == 0 and len(hand4) == 0) or (len(hand3) == 0 and spieler < 3) or spieler < 2: #überprüft, ob alle Bots gewonnen haben
                            labelAnzeige.config(text="Du hast verloren!")  #Benachrichtigung für Spieler
                            return #stoppt Zug
                    labelBot1.config(text=f"Bot1:\n{len(hand2)}") #Anzeige für Spieler
                    break #wenn eine Karte gelegt wurde ist der Zug zuende
        if gelegt == False and len(hand2) != 0: #wenn er nicht legen konnte und noch nicht Fertig ist
            aufnehmen(2)                        #nimmt er eine Karte auf
            tkFenster.after(1000, zugbot1)      #und versucht wieder eine Karte zu legen
            return
        else:
            if spieler > 2: #Abfrage ob Bot 2 auch Aktiv ist
                tkFenster.after(1000, zugbot2) #weitergabe
            else: 
                labelAnzeige.config(text="Du bist dran!")
                botsspielen = False
                #wenn nicht kommt der Spieler wieder dran

    def zugbot2():
        #print("Bot2:")
        global ablagestapel, hand3, botsspielen
        gelegt = False
        if len(hand3) != 0:
            for i in range(len(hand3)): #versucht alle Karten zu legen
                if ablagestapel[0][0] == hand3[i][0] or ablagestapel[0][1] == hand3[i][1]: #Überprüfen, ob Karte gelegt werden darf
                    print(f"der Bot 2 hat {hand3[i]} gelegt")
                    ablagestapel = [hand3[i]] + ablagestapel #Karte vorne auf den Ablagestapel
                    hand3.pop(i) #Karte aus Hand gelöscht
                    #Karte wird in GUI plaziert:
                    tempx = randint(width/2-20, width/2+20) #Random Versatz für "Stapel-Look"
                    tempy = randint(height/2-30, height/2+30) 
                    canvas.create_rectangle(tempx-75, tempy-125, tempx+75, tempy+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                    canvas.create_text(tempx, tempy, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert 
                    gelegt = True
                    if len(hand3) == 0: #Kontrolliert ob Bot noch Karten hat
                        labelAnzeige.config(text="Bot 2 ist Fertig!") #Benachrichtigung für Spieler
                        if (len(hand2) == 0 and len(hand4) == 0) or (len(hand2) == 0 and spieler < 3): #überprüft, ob alle Bots gewonnen haben
                            labelAnzeige.config(text="Du hast verloren!") #Benachrichtigung für Spieler
                            return #stoppt Zug 
                    labelBot2.config(text=f"Bot2:\n{len(hand3)}") #Anzeige für Spieler
                    break #wenn eine Karte gelegt wurde ist der Zug zuende
        if gelegt == False and len(hand3) != 0: #wenn er nicht legen konnte und noch nicht Fertig ist
            aufnehmen(3)                        #nimmt er eine Karte auf
            tkFenster.after(1000, zugbot2)      #und versucht wieder eine Karte zu legen
            return
        else:
            if spieler > 3: #Abfrage ob Bot 3 auch Aktiv ist
                tkFenster.after(1000, zugbot3) #weitergabe
            else: 
                labelAnzeige.config(text="Du bist dran!") #wenn nicht kommt der Spieler wieder dran
                botsspielen = False

    def zugbot3():
        #print("Bot3:")
        global ablagestapel, hand4, botsspielen
        gelegt = False
        if len(hand4) != 0:
            for i in range(len(hand4)): #versucht alle Karten zu legen
                if ablagestapel[0][0] == hand4[i][0] or ablagestapel[0][1] == hand4[i][1]: #Überprüfen, ob Karte gelegt werden darf
                    print(f"der Bot 3 hat {hand4[i]} gelegt")
                    ablagestapel = [hand4[i]] + ablagestapel #Karte vorne auf den Ablagestapel
                    hand4.pop(i) #Karte aus Hand gelöscht
                    #Karte wird in GUI plaziert:
                    tempx = randint(width/2-20, width/2+20) #Random Versatz für "Stapel-Look"
                    tempy = randint(height/2-30, height/2+30) 
                    canvas.create_rectangle(tempx-75, tempy-125, tempx+75, tempy+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                    canvas.create_text(tempx, tempy, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert 
                    gelegt = True
                    if len(hand4) == 0: #überprüft, ob der Bot noch Karten hat
                        labelAnzeige.config(text="Bot 1 ist Fertig!") #Benachrichtigung für Spieler
                        if len(hand3) == 0 and len(hand2) == 0: #überprüft, ob alle Bots gewonnen haben
                            labelAnzeige.config(text="Du hast verloren!") #Benachrichtigung für Spieler
                            return #stoppt Zug 
                    labelBot3.config(text=f"Bot3:\n{len(hand4)}") #Anzeige für Spieler
                    break #wenn eine Karte gelegt wurde ist der Zug zuende
        if gelegt == False and len(hand4) != 0: #wenn er nicht legen konnte und noch nicht Fertig ist
            aufnehmen(4)                        #nimmt er eine Karte auf
            tkFenster.after(1000, zugbot3)      #und versucht wieder eine Karte zu legen
            return
        else:
            labelAnzeige.config(text="Du bist dran!") #Der Spielr kommt dran
            botsspielen = False
    
    #def quit(event):
    #    textdatei("game_active", "False")

    ### Erzeugung des Fensters ###
    tkFenster = Tk()
    tkFenster.title("Letzte Karte") #Name des Fensters
    tkFenster.attributes("-fullscreen", True) #Fullscreen

    ### ermittelt Bidschirmmaße ###
    width = tkFenster.winfo_screenwidth()
    height = tkFenster.winfo_screenheight()
    #print(width)
    #print(height)

    ###Grafikobjekte###
    #Spielfeld
    canvas = Canvas(master=tkFenster, background=primary_color)
    canvas.place(width=width, height=height-250)
    #Frame Hand
    framedeck = Frame(master=tkFenster, background=primary_color)
    framedeck.place(y=height-250, width=width, height=250)
    #Menu Button
    button_quit = Button(master=tkFenster, text="X", bg="red", font=("Arial", 35), command=quit) #close button ≡
    button_quit.place(x=width-75, y=25, width=50, height=50)
    #Anzeige Bots
    #Anzeige zur Anzahl der Karten für Bots werden bei Bedarf erstellt
    if spieler > 1: 
        labelBot1 = Label(master=tkFenster, text=f"Bot1:\n{len(hand2)}", bg=secondary_color, font=('Arial', 36), fg=font_color_1)
        labelBot1.place(x=10, y=(height/2)-125, width=150, height=250)
    if spieler > 2:
        labelBot2 = Label(master=tkFenster, text=f"Bot2:\n{len(hand3)}", bg=secondary_color, font=('Arial', 36), fg=font_color_1)
        labelBot2.place(x=(width/2)-75, y=10, width=150, height=250)
    if spieler > 3:
        labelBot3 = Label(master=tkFenster, text=f"Bot3:\n{len(hand4)}", bg=secondary_color, font=('Arial', 36), fg=font_color_1)
        labelBot3.place(x=width-165, y=(height/2)-125, width=150, height=250)
    #Anzeige Text
    labelAnzeige = Label(master=tkFenster, text=f"Du bist dran!", bg=primary_color, font=('Arial', 36), fg="black")
    labelAnzeige.place(x=0, y=height-350, width=width, height=100)
    #Aufnahmebutton
    button_aufnehmen = Button(master=tkFenster, text="aufnehmen", bg=secondary_color, font=("Arial", 20), fg=font_color_1, command=aufnehmen1)
    button_aufnehmen.place(x=(2*width/3)-75, y=(height/2)-125, width=150, height=250)
    
    ###Vorbereitung Spielfeld###
    aufnahmestapelerstellen()
    erstekarte()
    haende()

    ###Keybinds### 
    tkFenster.bind('<KeyPress- >', aufnehmen1e)
    tkFenster.bind('<KeyPress-1>', legen1)
    tkFenster.bind('<KeyPress-2>', legen2)
    tkFenster.bind('<KeyPress-3>', legen3)
    tkFenster.bind('<KeyPress-4>', legen4)
    tkFenster.bind('<KeyPress-5>', legen5)
    tkFenster.bind('<KeyPress-6>', legen6)
    tkFenster.bind('<KeyPress-7>', legen7)
    tkFenster.bind('<KeyPress-8>', legen8)
    tkFenster.bind('<KeyPress-9>', legen9)
    tkFenster.bind('<KeyPress-0>', legen10)
    tkFenster.bind('<KeyPress-Escape>', quit)
    tkFenster.bind('<KeyPress-End>', quit)
    tkFenster.bind('<KeyPress-Delete>', quit)
    tkFenster.bind('<KeyPress-BackSpace>', quit)
    
    # Aktivierung der Ereignisschleife
    tkFenster.mainloop()

game()