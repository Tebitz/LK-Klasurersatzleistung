from tkinter import *
from random import randint

#Karten
farbe = ["yellow", "blue", "red", "green"]
zahl = [0, 1, 2, 3, 4, 5, 6, 7]
hand = []
hand2 = []

#Variablen
y0=0
y1=y0+250

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

def  ordnen():
    canvascards.delete("all")
    global x0, y0, x1, y1
    index = width / (len(hand)) 
    x0 = (index/2)-75
    x1 = x0 + 150
    for i in range(len(hand)):
        #print(index)
        rectangle = f"id_Karte{i}"
        canvascards.create_rectangle(x0, y0, x1, y1, fill=hand[i][0]) #hand[i][1]]
        x0 += index
        x1 = x0 + 150

def legen1(event):
    canvascards.coords("id_Karte1", (550, 100, 700, 350)) #funktioniert  nicht

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
id_karte = canvas.create_rectangle(550, 100, 700, 350, fill="black") #x0, y0, x1, y1
id_stapel = canvas.create_rectangle(350, 100, 500, 350, fill="black") #x0, y0, x1, y1
# Schaltfaechen
tkFenster.bind('<KeyPress- >', aufnehmen)
tkFenster.bind('<KeyPress-1>', legen1)

# Aktivierung der Ereignisschleife
tkFenster.mainloop()
