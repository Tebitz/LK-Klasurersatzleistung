from tkinter import *
from random import randint

#Karten
farbe = ["yellow", "blue", "red", "green"]
zahl = [0, 1, 2, 3, 4, 5, 6, 7]
hand = []
hand2 = []

#stapel automatisch erstellen
def stapelerstellen():
    global stapel, stapelanzahl
    stapel = []
    stapelanzahl = 0
    for i in range(len(farbe)):
        for y in range(len(zahl)):
            stapel = stapel + [[farbe[i], zahl[y]]]
            stapelanzahl += 1
    #print(stapel)
    #print(stapelanzahl)
stapelerstellen()

#Variablen
width = 1900
height = 980
y0 = height-150
y1 = y0+250

# Ereignisbehandlung
def aufnehmen(event):
    global stapelanzahl, hand
    random = randint(0, stapelanzahl)
    #print(random)
    hand = hand + [stapel[random]]
    stapel.pop(random)
    stapelanzahl -= 1
    #print(stapel)
    #print(stapelanzahl)
    #print(hand)
    ordnen()

def ordnen():
    #alte Karten müssen vorher gelöscht werden
    global x0, y0, x1, y1
    index = width / (len(hand)) 
    x0 = (index/2)-75
    x1 = x0 + 150
    for i in range(len(hand)):
        #print(index)
        rectangle = f"id_Karte{i}"
        canvas.create_rectangle(x0, y0, x1, y1, fill=hand[i][0]) #hand[i][1]]
        x0 += index
        x1 = x0 + 150

def legen1(event):
    canvas.coords("id_Karte1", (550, 100, 700, 350)) #funktioniert  nicht

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Leinwand")
tkFenster.geometry(f"{width}x{height}")

# Zeichenleinwand
canvas = Canvas(master=tkFenster, background="brown")
canvas.place(width=width, height=height)
# Grafikobjekte
id_karte = canvas.create_rectangle(550, 100, 700, 350, fill="black") #x0, y0, x1, y1
id_stapel = canvas.create_rectangle(350, 100, 500, 350, fill="black") #x0, y0, x1, y1
# Schaltfaechen
tkFenster.bind('<KeyPress- >', aufnehmen)
tkFenster.bind('<KeyPress-1>', legen1)

# Aktivierung der Ereignisschleife
tkFenster.mainloop()
