from tkinter import *
from random import randint

#Listen
farbe = ["yellow", "blue", "red", "green"]
zahl = [0, 1, 2, 3, 4, 5, 6, 7]
hand = []
gelegt = []
stapel = []

#stapel automatisch erstellen
def stapelerstellen():
    print("Stapel wird erstellt")
    global stapel, stapelanzahl
    stapelanzahl = 0
    for i in range(len(farbe)):
        for y in range(len(zahl)):
            stapel = stapel + [[farbe[i], zahl[y]]] + [[farbe[i], zahl[y]]] #erstellt jede mögliche Karte 2mal
            stapelanzahl += 2 #Stapelanzahl wird mitgezählt
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")
stapelerstellen()

#Wenn der Stapel leer ist werden die bereits gelegten karten wieder untergemischt
def stapelerneuern(): #funktioniert nicht
    print("Stapel wird erneuert")
    global stapelanzahl, stapel, gelegt 
    stapelanzahl += len(gelegt)-1
    stapel = stapel + gelegt[1:]
    gelegt = gelegt[0]
    ##print(f"Gelegt sind jetzt: {gelegt}")
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")

# Ereignisbehandlung
def aufnehmen(event):
    print("Karte wird aufgenommen")
    global stapelanzahl, stapel, hand
    if stapelanzahl == 0: #guckt ob noch Karten auf dem Stapel sind
        print("keine Karten mehr auf dem Stapel")
        stapelerneuern() #kann man auch direkt tuen
    random = randint(0, stapelanzahl-1)
    ##print(f"die {random}. Karte wird aufgenommen")
    hand = hand + [stapel[random]]
    stapel.pop(random)
    stapelanzahl -= 1
    ##print(f"Auf der Hand sind jetzt: {hand}")
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")
    ordnen()

def ordnen():
    print("Karten werden neu gerordnet")
    canvascards.delete("all") #Canvas wird gelehrt
    global x0, y0, x1, y1
    index = width / (len(hand)) 
    x0 = (index/2)-75
    x1 = x0 + 150 #Abstände werden neu berechnet
    for i in range(len(hand)): #Karten werden plaziert
        #rectangle = f"id_Karte{i}"
        #canvascards.create_text(x1, y1, text=hand[i][1], fill="blue", font=('Helvetica 15 bold')) # bg //Hintergrund?
        canvascards.create_rectangle(x0, 0, x1, 250, fill=hand[i][0]) #hand[i][1] 
        x0 += index
        x1 = x0 + 150

def erstekarte(): #eine erste Karte muss als Grundlage gelegt werden
    print("die Erste Karte wird gelegt")
    global stapelanzahl, stapel, gelegt
    random = randint(0, stapelanzahl-1)
    gelegt = [stapel[random]] 
    stapel.pop(random)
    stapelanzahl -= 1
    id_karteoben = canvas.create_rectangle(550, 100, 700, 350, fill=gelegt[0][0]) #gelegt[0][1] #x0, y0, x1, y1
    ##print(f"die {random}. Karte wurde ausgewählt")
    ##print(f"gelegt wurde: {gelegt}")
    ##print(f"Auf dem Stapel: {stapel}")
    ##print(f"Das sind {stapelanzahl} Karten")    
    #Random Karte wird plaziert

def legen1(event): #Bedingung fehlt
    print("eine Karte wird gelegt")
    global gelegt, hand
    gelegt = [hand[0]] + gelegt #Karte vorne in Liste rein
    hand.pop(0) #Karte aus anderer Liste gelöscht
    id_karteoben = canvas.create_rectangle(550, 100, 700, 350, fill=gelegt[0][0]) #gelegt[0][1] #x0, y0, x1, y1 #Karte wird plaziert
    ##print(f"die Karte {hand[0]} wurde gelegt")
    ##print(f"gelegt wurden jetzt: {gelegt}")
    ordnen()

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
id_stapel = canvas.create_rectangle(350, 100, 500, 350, fill="black") #x0, y0, x1, y1 #text='aufnehmen'
erstekarte()
# Schaltfaechen
tkFenster.bind('<KeyPress- >', aufnehmen)
tkFenster.bind('<KeyPress-1>', legen1)

# Aktivierung der Ereignisschleife
tkFenster.mainloop()
