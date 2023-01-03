from tkinter import *
from functions import *
from random import randint

# Erzeugung des Fensters
tkFenster = Tk()
tkFenster.title("Leinwand")
tkFenster.attributes("-fullscreen", True)

stapelerstellen()
# Zeichenleinwand
canvases()
# Grafikobjekte
erstekarte()
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
