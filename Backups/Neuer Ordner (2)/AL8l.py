from tkinter import *
from random import randint

#einstellung für karte nur einmal
#menu
#anzahl Farben
#aus txt bekommen
#Bug: Bot nimmt 50 Karten auf
#wenn der bot gewinnt spielt er weiter mit?

#Listen (Kartenstapel werden erstellt)
hand1 = []
hand2 = []
hand3 = []
hand4 = []
ablagestapel = []
nachziehstapel = []

#Variblen #aus txt
spieler = 2 #bots + 1
kartenaufnehmen = 5 #Karten mit denen jeder Spieler startet
primary_color = "gray"
secondary_color = "black"
font_color_1 = "white"
maximalekarten = 20 #10-20
anzahlfarben = 5

def game(): #Gesammtfunktion die das Menu aufruft

    def aufnahmestapelerstellen():
        if anzahlfarben < 4:
            farben = ["blue", "red", "green"]
        if anzahlfarben == 4:
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
        print("Spielfeld wird vorbereitet")
        canvas.delete("all")
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
        global labelBot1, labelBot2, labelBot3
        for i in range(kartenaufnehmen): #aufzunehmende Karten für Spielstart werden aufgenommen
            aufnehmen(1)
            aufnehmen(2)
            aufnehmen(3)
            aufnehmen(4)
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

    def aufnehmen1e(event): #Funktion für Tastendruck
        aufnehmen(1) #Befehl zur Aufnahme einer Karte wird weitergegeben
    def aufnehmen1(): #Funktion für Button
        aufnehmen(1) #Befehl zur Aufnahme einer Karte wird weitergegeben

    def aufnehmen(hand):
        global nachziehstapel, hand1, hand2, hand3, hand4
        if len(nachziehstapel) == 0: #prüft ob noch Karten auf dem Stapel sind
            stapelerneuern() #Im falle würde er den Stapel neu mischen
        random = randint(0, len(nachziehstapel)-1) #eine zufällige Karte wird Ausgewählt
        #Es wird geprüft, welcher Spieler aufnimmt
        if hand == 1:
            hand1 = hand1 + [nachziehstapel[random]] #Die ausgewählte Karte wird zur Liste hinzugefügt
            ordnen()# Die Hand des Spielers wird neu geordnet
        if hand == 2:
            hand2 = hand2 + [nachziehstapel[random]]
        if hand == 3:
            hand3 = hand3 + [nachziehstapel[random]]
        if hand == 4:
            hand4 = hand4 + [nachziehstapel[random]]
        print(f"Die Karte {nachziehstapel[random]} wird von Spieler {hand} aufgenommen")
        nachziehstapel.pop(random) #Karte wird aus Nachziehstapel entfernt

    #Wenn der Stapel leer ist werden die bereits gelegten karten wieder untergemischt:
    def stapelerneuern():
        global nachziehstapel, ablagestapel
        nachziehstapel = ablagestapel[1:] #alle außer die oberste Karte des Ablagestapel werden kopiert
        ablagestapel = ablagestapel[0] #und dann aus dem Ablagestapel entfernt
        print(f"Der Stapel wird erneuert:\n{nachziehstapel}\nübrig ist jetzt: {ablagestapel}")

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
        global ablagestapel, hand1
        if ablagestapel[0][0] == hand1[karte][0] or ablagestapel[0][1] == hand1[karte][1]: #Überprüfen, ob Karte gelegt werden darf
            ablagestapel = [hand1[karte]] + ablagestapel #Karte vorne auf den Ablagestapel
            hand1.pop(karte) #Karte aus Hand gelöscht
            #Karte wird in GUI plaziert
            temp = width/2
            canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
            canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
            #print(f"die {karte}. Karte wurde gelegt: {hand1[karte]}")
            ordnen() #Hand wird neu geordnet
            if spieler > 1 and gewonnen == False: #Überprüfen, ob Bots dran sind
                labelAnzeige.config(text="Die Bots spielen!") #Benachrichtigung für Spieler
                #Buttons werden gespeert
                tkFenster.after(1000, zugbot1) #Weitergabe an Bots
        else: labelAnzeige.config(text="Diese Karte kannst du nicht legen!")
        #Benachrichtigung für Spieler, falls ungültiger Zug

    def ordnen():
        global gewonnen 
        gewonnen = False
        #framedeck.destroy
        framedeck = Frame(master=tkFenster, background=primary_color)
        framedeck.place(y=height-250, width=width, height=250)
        #canvascards.delete("all") #Canvas wird gelehrt
        if len(hand1) > 0:
            index = width / (len(hand1)) 
        else: index = 0
        x0 = (index/2)-75
        #x1 = x0 + 150 #Abstände werden neu berechnet
        for i in range(len(hand1)): #Karten werden plaziert
            if i == 0:
                button_Karte1 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(0))
                button_Karte1.place(x=x0, y=0, width=150, height=250)
            if i == 1:
                button_Karte2 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(1))
                button_Karte2.place(x=x0, y=0, width=150, height=250)
            if i == 2:
                button_Karte3 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(2))
                button_Karte3.place(x=x0, y=0, width=150, height=250)
            if i == 3:
                button_Karte4 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(3))
                button_Karte4.place(x=x0, y=0, width=150, height=250)
            if i == 4:
                button_Karte5 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(4))
                button_Karte5.place(x=x0, y=0, width=150, height=250)
            if i == 5:
                button_Karte6 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(5))
                button_Karte6.place(x=x0, y=0, width=150, height=250)
            if i == 6:
                button_Karte7 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(6))
                button_Karte7.place(x=x0, y=0, width=150, height=250)
            if i == 7:
                button_Karte8 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(7))
                button_Karte8.place(x=x0, y=0, width=150, height=250)
            if i == 8:
                button_Karte9 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(8))
                button_Karte9.place(x=x0, y=0, width=150, height=250)
            if i == 9:
                button_Karte10 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(9))
                button_Karte10.place(x=x0, y=0, width=150, height=250)
            if i == 10:
                button_Karte11 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(10))
                button_Karte11.place(x=x0, y=0, width=150, height=250)
            if i == 11:
                button_Karte12 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(11))
                button_Karte12.place(x=x0, y=0, width=150, height=250)
            if i == 12:
                button_Karte13 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(12))
                button_Karte13.place(x=x0, y=0, width=150, height=250)
            if i == 13:
                button_Karte14 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(13))
                button_Karte14.place(x=x0, y=0, width=150, height=250)
            if i == 14:
                button_Karte15 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(14))
                button_Karte15.place(x=x0, y=0, width=150, height=250)
            if i == 15:
                button_Karte16 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(15))
                button_Karte16.place(x=x0, y=0, width=150, height=250)
            if i == 16:
                button_Karte17 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(16))
                button_Karte17.place(x=x0, y=0, width=150, height=250)
            if i == 17:
                button_Karte18 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(17))
                button_Karte18.place(x=x0, y=0, width=150, height=250)
            if i == 18:
                button_Karte19 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(18))
                button_Karte19.place(x=x0, y=0, width=150, height=250)
            if i == 19:
                button_Karte20 = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(19))
                button_Karte20.place(x=x0, y=0, width=150, height=250)
            if i == 20:
                print("veloren")
                gewonnen = True
                return
            """
            canvascards.create_rectangle(x0, 0, x1, 250, fill=hand1[i][0]) #Hintergrund der Karte
            canvascards.create_text(x0+75, 125, font=("Arial", 100), text=hand1[i][1], fill="black") #Vordergrund der Karte
            """
            x0 += index
            #x1 = x0 + 150
        if len(hand1) == 0:
            labelAnzeige.config(text="Du hast gewonnen!")
            gewonnen = True

    def zugbot1():
        global ablagestapel, hand2
        labelAnzeige.config(text="Die Bots spielen!")
        gelegt = False
        for i in range(len(hand2)):
            print(f"die {i}. Karte soll von Bot 1 gelegt werden: {hand2[i]}")
            if ablagestapel[0][0] == hand2[i][0] or ablagestapel[0][1] == hand2[i][1]:
                ablagestapel = [hand2[i]] + ablagestapel #Karte vorne in Liste rein
                hand2.pop(i) #Karte aus anderer Liste gelöscht
                temp = width/2
                canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                labelBot1.config(text=f"Bot1:\n{len(hand2)}")
                gelegt = True
                if len(hand2) == 0:
                    labelAnzeige.config(text="Bot 1 ist Fertig!")
                    if len(hand3) == 0 and len(hand4) == 0:
                        labelAnzeige.config(text="Du hast verloren!") 
                        return   
                break
        labelBot1.config(text=f"Bot1:\n{len(hand2)}")
        if gelegt == False:
            aufnehmen(2)
            zugbot1()
        else:
            if spieler > 2:
                tkFenster.after(1000, zugbot2)
            else: labelAnzeige.config(text="Du bist dran!")

    def zugbot2():
        global ablagestapel, hand3
        gelegt = False
        for i in range(len(hand3)):
            print(f"die {i}. Karte soll von Bot 2 gelegt werden: {hand3[i]}")
            if ablagestapel[0][0] == hand3[i][0] or ablagestapel[0][1] == hand3[i][1]:
                ablagestapel = [hand3[i]] + ablagestapel #Karte vorne in Liste rein
                hand3.pop(i) #Karte aus anderer Liste gelöscht
                temp = width/2
                canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                labelBot2.config(text=f"Bot2:\n{len(hand3)}")
                gelegt = True
                if len(hand3) == 0:
                    labelAnzeige.config(text="Bot 2 ist Fertig!")
                    if len(hand2) == 0 and len(hand4) == 0:
                        labelAnzeige.config(text="Du hast verloren!") 
                        return   
                break
        labelBot2.config(text=f"Bot2:\n{len(hand3)}")
        if gelegt == False:
            aufnehmen(3)
            zugbot2()
        else:
            if spieler > 3:
                tkFenster.after(1000, zugbot3)
            else: labelAnzeige.config(text="Du bist dran!")

    def zugbot3():
        global ablagestapel, hand4
        labelAnzeige.config(text="Die Bots spielen!")
        gelegt = False
        for i in range(len(hand4)):
            print(f"die {i}. Karte soll von Bot 3 gelegt werden: {hand4[i]}")
            if ablagestapel[0][0] == hand4[i][0] or ablagestapel[0][1] == hand4[i][1]:
                ablagestapel = [hand4[i]] + ablagestapel #Karte vorne in Liste rein
                hand4.pop(i) #Karte aus anderer Liste gelöscht
                temp = width/2
                canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                labelBot3.config(text=f"Bot3:\n{len(hand4)}")
                gelegt = True
                if len(hand4) == 0:
                    labelAnzeige.config(text="Bot 1 ist Fertig!")
                    if len(hand3) == 0 and len(hand2) == 0:
                        labelAnzeige.config(text="Du hast verloren!")   
                        return 
                break
        labelBot3.config(text=f"Bot3:\n{len(hand4)}")
        if gelegt == False:
            aufnehmen(4)
            zugbot3()
        else:
            labelBot3.config(text=f"Bot3:\n{len(hand4)}")
            labelAnzeige.config(text="Du bist dran!")
    
    aufnahmestapelerstellen()
    # Erzeugung des Fensters
    tkFenster = Tk()
    tkFenster.title("Letzte Karte")
    tkFenster.attributes("-fullscreen", True)

    width = tkFenster.winfo_screenwidth()
    height = tkFenster.winfo_screenheight()
    #print(width)
    #print(height)

    # Grafikobjekte
    canvas = Canvas(master=tkFenster, background=primary_color)
    canvas.place(width=width, height=height-250)
    framedeck = Frame(master=tkFenster, background=primary_color)
    framedeck.place(y=height-250, width=width, height=250)
    #canvascards = Canvas(master=tkFenster, background=primary_color)
    #canvascards.place(y=height-250, width=width, height=250)
    button_quit = Button(master=tkFenster, text="X", bg="red", font=("Arial", 35), command=quit)#close button ≡
    button_quit.place(x=width-75, y=25, width=50, height=50)
    labelAnzeige = Label(master=tkFenster, text=f"Du bist dran!", bg=primary_color, font=('Arial', 36), fg="black")
    labelAnzeige.place(x=0, y=height-350, width=width, height=100)
    erstekarte()
    button_aufnehmen = Button(master=tkFenster, text="aufnehmen", bg=secondary_color, font=("Arial", 20), fg=font_color_1, command=aufnehmen1)
    button_aufnehmen.place(x=(2*width/3)-75, y=(height/2)-125, width=150, height=250)
    haende()
    # Schaltfaechen
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