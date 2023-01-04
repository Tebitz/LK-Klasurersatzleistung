from tkinter import *
from random import randint

#Listen
farben = ["yellow", "blue", "red", "green"]
zahlen = [0, 1, 2, 3, 4, 5, 6, 7]
hand1 = []
hand2 = []
hand3 = []
hand4 = []
ablagestapel = []
nachziehstapel = []
#Variblen
spieler = 4
kartenaufnehmen = 5

def game(): #Funktion die das Menu aufruft

    #stapel automatisch erstellen
    def stapelerstellen():
        print("Stapel wird erstellt")
        global nachziehstapel
        for i in range(len(farben)):
            for y in range(len(zahlen)):
                nachziehstapel = nachziehstapel + [[farben[i], zahlen[y]]] + [[farben[i], zahlen[y]]] #erstellt jede mögliche Karte 2mal #einstellung für karte nur einmal
    #######plus karten#####
    ##print(f"Auf dem Stapel: {nachziehstapel}")

    def erstekarte(): #eine erste Karte muss als Grundlage gelegt werden
        print("Spielfeld wird vorbereitet")
        canvas.delete("all")
        global nachziehstapel, ablagestapel
        random = randint(0, len(nachziehstapel)-1)#??? muss -1?
        ablagestapel = [nachziehstapel[random]] 
        nachziehstapel.pop(random)
        temp = width/2
        canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
        canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
        ##print(f"die {random}. Karte wurde ausgewählt")
        ##print(f"gelegt wurde: {ablagestapel}")
        ##print(f"Auf dem Stapel: {nachziehstapel}") 
        #Random Karte wird plaziert

    def haende():
        print("Karten werden aufgenommen")
        for i in range(kartenaufnehmen):
            aufnehmen(1)
            aufnehmen(2)
            aufnehmen(3)
            aufnehmen(4)
        if spieler > 1:
            labelBot1 = Label(master=tkFenster, text="Bot1:\n0", bg='black', font=('Arial', 36), fg="white")
            labelBot1.place(x=10, y=(height/2)-125, width=150, height=250)
        if spieler > 2:
            labelBot2 = Label(master=tkFenster, text="Bot2:\n0", bg='black', font=('Arial', 36), fg="white")
            labelBot2.place(x=(width/2)-75, y=10, width=150, height=250)
        if spieler > 3:
            labelBot3 = Label(master=tkFenster, text="Bot3:\n0", bg='black', font=('Arial', 36), fg="white")
            labelBot3.place(x=width-165, y=(height/2)-125, width=150, height=250)

    def aufnehmen1e(event):
        aufnehmen(1) #für hand 1
    def aufnehmen1():
        aufnehmen(1) #für hand 1

    def aufnehmen(hand):
        print("Karte wird aufgenommen")
        global nachziehstapel, hand1, hand2, hand3, hand4
        if len(nachziehstapel) == 0: #guckt ob noch Karten auf dem Stapel sind
            print("keine Karten mehr auf dem Stapel")
            stapelerneuern() #kann man auch direkt tuen
        random = randint(0, len(nachziehstapel)-1)
        ##print(f"die {random}. Karte wird aufgenommen")
        if hand == 1:
            hand1 = hand1 + [nachziehstapel[random]]
        if hand == 2:
            hand2 = hand2 + [nachziehstapel[random]]
        if hand == 3:
            hand3 = hand3 + [nachziehstapel[random]]
        if hand == 4:
            hand4 = hand4 + [nachziehstapel[random]]
        nachziehstapel.pop(random)
        ##print(f"Auf der Hand sind jetzt: {hand}")
        ##print(f"Auf dem Stapel: {stapel}")
        ##print(f"Das sind {stapelanzahl} Karten")
        ordnen()

    #Wenn der Stapel leer ist werden die bereits gelegten karten wieder untergemischt
    def stapelerneuern(): #funktioniert nicht???
        print("Stapel wird erneuert")
        global nachziehstapel, ablagestapel
        nachziehstapel = nachziehstapel + ablagestapel[1:]
        ablagestapel = ablagestapel[0]
        ##print(f"Gelegt sind jetzt: {gelegt}")
        ##print(f"Auf dem Stapel: {stapel}")
        ##print(f"Das sind {stapelanzahl} Karten")

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

    def legen(karte): #Karte ab 0 (Index)
        global ablagestapel, hand1
        print(f"die {karte}. Karte wurde gelegt: {hand1[karte]}")
        if ablagestapel[0][0] == hand1[karte][0] or ablagestapel[0][1] == hand1[karte][1]:
            ablagestapel = [hand1[karte]] + ablagestapel #Karte vorne in Liste rein
            hand1.pop(karte) #Karte aus anderer Liste gelöscht
            temp = width/2
            canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
            canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
            ##print(f"gelegt wurden jetzt: {ablagestapel}")
            ordnen()
            tkFenster.after(2000, zugbot1)
        else: print(f"sie konnte nicht gelegt werden")

    def ordnen():
        if len(hand1) == 0:
            print("gewonnen")
            return
        print("Karten werden neu gerordnet")
        #framedeck.destroy
        framedeck = Frame(master=tkFenster, background="gray")
        framedeck.place(y=height-250, width=width, height=250)
        #canvascards.delete("all") #Canvas wird gelehrt
        index = width / (len(hand1)) 
        x0 = (index/2)-75
        #x1 = x0 + 150 #Abstände werden neu berechnet
        for i in range(len(hand1)): #Karten werden plaziert
            #command = f"legen({i})"
            button_Karten = Button(master=framedeck, text=hand1[i][1], bg=hand1[i][0], font=("Arial", 100), fg="black", command= lambda: legen(i))
            button_Karten.place(x=x0, y=0, width=150, height=250)
            """
            canvascards.create_rectangle(x0, 0, x1, 250, fill=hand1[i][0]) #Hintergrund der Karte
            canvascards.create_text(x0+75, 125, font=("Arial", 100), text=hand1[i][1], fill="black") #Vordergrund der Karte
            """
            x0 += index
            #x1 = x0 + 150

    def zugbot1():
        global ablagestapel, hand2, hand3, hand4
        if spieler > 1:
            print("Bots 1 ist dran")
            for i in range(len(hand2)):
                print(f"die {i}. Karte soll gelegt werden: {hand2[i]}")
                if ablagestapel[0][0] == hand2[i][0] or ablagestapel[0][1] == hand2[i][1]:
                    ablagestapel = [hand2[i]] + ablagestapel #Karte vorne in Liste rein
                    hand2.pop(i) #Karte aus anderer Liste gelöscht
                    temp = width/2
                    canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                    canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                    ##print(f"gelegt wurden jetzt: {ablagestapel}")
                    break
        if spieler > 2:
            tkFenster.after(1000, zugbot2)

    def zugbot2():
        print("Bots 2 ist dran")
        global ablagestapel, hand2, hand3, hand4
        for i in range(len(hand3)):
            print(f"die {i}. Karte wurde gelegt: {hand3[i]}")
            if ablagestapel[0][0] == hand3[i][0] or ablagestapel[0][1] == hand3[i][1]:
                ablagestapel = [hand3[i]] + ablagestapel #Karte vorne in Liste rein
                hand3.pop(i) #Karte aus anderer Liste gelöscht
                temp = width/2
                canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                ##print(f"gelegt wurden jetzt: {ablagestapel}")
                break
        if spieler > 3:
            tkFenster.after(1000, zugbot3)

    def zugbot3():
        print("Bots 3 ist dran")
        global ablagestapel, hand2, hand3, hand4
        for i in range(len(hand4)):
            print(f"die {i}. Karte wurde gelegt: {hand4[i]}")
            if ablagestapel[0][0] == hand4[i][0] or ablagestapel[0][1] == hand4[i][1]:
                ablagestapel = [hand4[i]] + ablagestapel #Karte vorne in Liste rein
                hand4.pop(i) #Karte aus anderer Liste gelöscht
                temp = width/2
                canvas.create_rectangle(temp-75, (height/2)-125, temp+75, (height/2)+125, fill=ablagestapel[0][0]) #Hintergrund der Karte wird plaziert
                canvas.create_text(temp, height/2, font=("Arial", 100), text=ablagestapel[0][1], fill="black") #Vordergrund der Karte wird plaziert
                ##print(f"gelegt wurden jetzt: {ablagestapel}")
                break
    
    stapelerstellen()
    # Erzeugung des Fensters
    tkFenster = Tk()
    tkFenster.title("Letzte Karte")
    tkFenster.attributes("-fullscreen", True)

    width = tkFenster.winfo_screenwidth()
    height = tkFenster.winfo_screenheight()
    #print(width)
    #print(height)

    # Zeichenleinwand
    canvas = Canvas(master=tkFenster, background="gray")
    canvas.place(width=width, height=height-250)
    framedeck = Frame(master=tkFenster, background="gray")
    framedeck.place(y=height-250, width=width, height=250)
    #canvascards = Canvas(master=tkFenster, background="gray")
    #canvascards.place(y=height-250, width=width, height=250)
    button_quit = Button(master=tkFenster, text="X", bg="red", font=("Arial", 35), command=quit)#close button
    button_quit.place(x=width-75, y=25, width=50, height=50)
    # Grafikobjekte
    erstekarte()
    button_aufnehmen = Button(master=tkFenster, text="aufnehmen", bg="black", font=("Arial", 20), fg="white", command=aufnehmen1)
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