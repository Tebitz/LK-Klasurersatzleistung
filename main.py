from tkinter import *
from random import randint

#Listen
farben = ["yellow", "blue", "red", "green"]
zahlen = [0, 1, 2, 3, 4, 5, 6, 7]
hand1 = [] #variabel?
hand2 = []
hand3 = []
hand4 = []
gelegt = [] #ablagestapel
stapel = [] #nachziehstapel
#Variblen
spieler = 1
kartenaufnehmen = 5

#stapel automatisch erstellen
def stapelerstellen():
    print("Stapel wird erstellt")
    global stapel, stapelanzahl
    stapelanzahl = 0 ############stattdessen len(stapel)
    for i in range(len(farben)):
        for y in range(len(zahlen)):
            stapel = stapel + [[farben[i], zahlen[y]]] + [[farben[i], zahlen[y]]] #erstellt jede mögliche Karte 2mal #einstellung für karte nur einmal
            stapelanzahl += 2 #Stapelanzahl wird mitgezählt
    #######plus karten#####
    print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")
stapelerstellen()

def erstekarte(): #eine erste Karte muss als Grundlage gelegt werden
    print("Spielfeld wird vorbereitet")
    canvas.delete("all")
    global stapelanzahl, stapel, gelegt
    random = randint(0, len(stapel)-1)#??? muss -1?
    gelegt = [stapel[random]] 
    stapel.pop(random)
    stapelanzahl -= 1
    temp = width/2
    canvas.create_rectangle(temp-75, 300, temp+75, 550, fill=gelegt[0][0]) #Hintergrund der Karte wird plaziert
    canvas.create_text(temp, 425, font=("Arial", 100), text=gelegt[0][1], fill="black") #Vordergrund der Karte wird plaziert
    ##print(f"die {random}. Karte wurde ausgewählt")
    ##print(f"gelegt wurde: {gelegt}")
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")    
    #Random Karte wird plaziert

def haende():
    print("Karten werden aufgenommen")
    karten = 0
    while karten < kartenaufnehmen:
        if spieler > 0:
            aufnehmen1()
        #if spieler > 1:
            #aufnehmen2()
        #if spieler > 2:
            #aufnehmen3()
        #if spieler > 3:
            #aufnehmen4()
        karten += 1

def aufnehmen1e(event):
    aufnehmen1() #für hand 1

def aufnehmen1():
    print("Karte wird aufgenommen")
    global stapelanzahl, stapel, hand1
    if stapelanzahl == 0: #guckt ob noch Karten auf dem Stapel sind
        print("keine Karten mehr auf dem Stapel")
        stapelerneuern() #kann man auch direkt tuen
    random = randint(0, stapelanzahl-1)
    ##print(f"die {random}. Karte wird aufgenommen")
    hand1 = hand1 + [stapel[random]]
    stapel.pop(random)
    stapelanzahl -= 1
    ##print(f"Auf der Hand sind jetzt: {hand}")
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")
    ordnen()

#Wenn der Stapel leer ist werden die bereits gelegten karten wieder untergemischt
def stapelerneuern(): #funktioniert nicht???
    print("Stapel wird erneuert")
    global stapelanzahl, stapel, gelegt 
    stapelanzahl += len(gelegt)-1
    stapel = stapel + gelegt[1:]
    gelegt = gelegt[0]
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
    global gelegt, hand1
    print(f"die {karte}. Karte wurde gelegt: {hand1[karte]}")
    if gelegt[0][0] == hand1[karte][0] or gelegt[0][1] == hand1[karte][1]:
        gelegt = [hand1[karte]] + gelegt #Karte vorne in Liste rein
        hand1.pop(karte) #Karte aus anderer Liste gelöscht
        temp = width/2
        canvas.create_rectangle(temp-75, 300, temp+75, 550, fill=gelegt[0][0]) #Hintergrund der Karte wird plaziert ###########bischen random Position für optische illusion wie Stapel
        canvas.create_text(temp, 425, font=("Arial", 100), text=gelegt[0][1], fill="black") #Vordergrund der Karte wird plaziert
        ##print(f"die Karte {hand[0]} wurde gelegt")
        ##print(f"gelegt wurden jetzt: {gelegt}")
        ordnen()
    else: print(f"sie konnte nicht gelegt werden")

def ordnen():
    if len(hand1) ==0:
        print("gewonnen")
        return
    print("Karten werden neu gerordnet")
    canvascards.delete("all") #Canvas wird gelehrt
    global x0, x1
    index = width / (len(hand1)) 
    x0 = (index/2)-75
    x1 = x0 + 150 #Abstände werden neu berechnet
    for i in range(len(hand1)): #Karten werden plaziert
        #rectangle = f"id_Karte{i}"
        canvascards.create_rectangle(x0, 0, x1, 250, fill=hand1[i][0]) #Hintergrund der Karte
        canvascards.create_text(x0+75, 125, font=("Arial", 100), text=hand1[i][1], fill="black") #Vordergrund der Karte
        x0 += index
        x1 = x0 + 150

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Leinwand")
tkFenster.attributes("-fullscreen", True)

width = tkFenster.winfo_screenwidth()
height = tkFenster.winfo_screenheight()
#print(width)
#print(height)

# Zeichenleinwand
canvas = Canvas(master=tkFenster, background="gray")
canvas.place(width=width, height=height-250)
canvascards = Canvas(master=tkFenster, background="black")
canvascards.place(y=height-250, width=width, height=250)
# Grafikobjekte
erstekarte()
id_nachziehstapel = canvas.create_rectangle((3*width/4)-75, 300, (3*width/4)+75, 550, fill="black") #
id_aufnehmen = canvas.create_text(3*width/4, 425, font=("Arial", 20), text='aufnehmen', fill="white") #master?
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

# Aktivierung der Ereignisschleife
tkFenster.mainloop()
