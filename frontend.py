from tkinter import *
from random import randint

#Karten
farbe = ["yellow", "blue", "red", "green"]
zahl = [0, 1, 2, 3, 4, 5, 6, 7]
hand = []
gelegt = []
stapel = []

#Variablen
y0=0
y1=y0+250

#stapel automatisch erstellen
def stapelerstellen():
    global stapel, stapelanzahl
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
    global stapelanzahl, stapel, hand
    if stapelanzahl == 0:
        print("keine Karten mehr auf dem Stapel")
        stapelerneuern()
    else:
        random = randint(0, stapelanzahl-1)
        print(f"die {random}. Karte wird aufgenommen")
        hand = hand + [stapel[random]]
        stapel.pop(random)
        stapelanzahl -= 1
        print(f"Auf der Hand sind jetzt: {hand}")
        print(f"Auf dem Stapel: {stapel}")
        print(f"Das sind {stapelanzahl} Karten")
        ordnen()

def stapelerneuern():
    global stapelanzahl, stapel, gelegt
    stapelanzahl += len(gelegt)-1
    stapel = stapel + [gelegt[1:]]
    gelegt = gelegt[0]

def ordnen():
    canvascards.delete("all")
    global x0, y0, x1, y1
    index = width / (len(hand)) 
    x0 = (index/2)-75
    x1 = x0 + 150
    for i in range(len(hand)):
        #rectangle = f"id_Karte{i}"
        #canvascards.create_text(x1, y1, text=hand[i][1], fill="blue", font=('Helvetica 15 bold')) # bg //Hintergrund?
        canvascards.create_rectangle(x0, y0, x1, y1, fill=hand[i][0]) #hand[i][1] 
        x0 += index
        x1 = x0 + 150

def erstekarte():
    global stapelanzahl, stapel, gelegt
    random = randint(0, stapelanzahl-1)
    gelegt = [stapel[random]]
    stapel.pop(random)
    stapelanzahl -= 1
    id_karteoben = canvas.create_rectangle(550, 100, 700, 350, fill=gelegt[0][0]) #gelegt[0][1] #x0, y0, x1, y1

def legen1(event):
    global gelegt, hand
    gelegt = [hand[0]] + gelegt
    hand.pop(0)
    id_karteoben = canvas.create_rectangle(550, 100, 700, 350, fill=gelegt[0][0]) #gelegt[0][1] #x0, y0, x1, y1
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
