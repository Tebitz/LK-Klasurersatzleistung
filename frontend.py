from tkinter import *
from random import randint

#Karten
farbe = ["yellow", "blue", "red", "green"]
zahl = [0, 1, 2, 3, 4, 5, 6, 7]
stapel = []
stapel()
stapel = [["green", "1"], ["blue", "2"], ["red", "3"], ["yellow", "4"]] #automatisch erstellen lassen
hand = [["green", "1"], ["blue", "2"], ["red", "3"], ["yellow", "4"]]

#stapel automatisch erstellen
def stapel():
    global stapel
    for i in range(len(farbe)):
        for y in range(len(zahl)):
            stapel = stapel + [farbe[i], zahl[y]]
    print(stapel)

#Variablen
width = 1070
y0 = 450
y1 = 700

# Ereignisbehandlung
def aufnehmen(event):
    random1 = randint(0,3)
    random2 = randint(0,6)

def ordnen(event):
    global x0, y0, x1, y1
    index = width / (len(hand)) 
    x0 = (index/2)-75
    x1 = x0 + 150
    for i in range(len(hand)):
        print(index)
        rectangle = f"id_Karte{i}"
        canvas.create_rectangle(x0, y0, x1, y1, fill=hand[i][0]) #hand[i][1]]
        x0 += index
        x1 = x0 + 150

def legen1(event):
    canvas.coords("id_Karte1", (550, 100, 700, 350)) #funktioniert noch nicht

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Leinwand")
tkFenster.geometry("1080x550")

# Zeichenleinwand
canvas = Canvas(master=tkFenster, background="brown")
canvas.place(x=5, y=5, width=width, height=540)
# Grafikobjekte
id_karte = canvas.create_rectangle(550, 100, 700, 350, fill="black") #x0, y0, x1, y1
id_stapel = canvas.create_rectangle(350, 100, 500, 350, fill="black") #x0, y0, x1, y1
# Schaltfaechen
tkFenster.bind('<KeyPress- >', ordnen)
tkFenster.bind('<KeyPress-1>', legen1)

# Aktivierung der Ereignisschleife
tkFenster.mainloop()
