# Von Amos
#diese Funktion ist die einzige Schnittstelle zur txt, sie liest diese aus und gibt bestimmte Werte zurück, oder berarbeitet sie.
def textdatei(parameter, value): #parameter = was gesucht wird ("number_of_cards"), value = in was der Wert geändert werden soll, beim auslesen value = "null".
    #Speichern des inhalts der txt als einzelnen String.
    text = open("settings.txt", "r") #Die txt wird im Lesemodus geöffnet
    data = text.read()
    text.close()
    data = data.split() #Erstellt eine Liste in der jede zusammenhängende zeichenkette ein Listenelement ist.
    i = 0
    #überprüft jedes zweite Listenelement, ob es dem ersten Parameter entspricht.
    while i < len(data)-1:
        if data[i] == parameter:
            #wenn der zweite Parameter (value) "null" ist, wird das nächste Listenelement zurück gegeben.
            if value == "null":
                return(data[i + 1])
            #wenn nicht wird i dem Index des nächsten Listenelements zugeordnet und die Schleife beendet.
            else:
                i = i + 1
                break
        i = i + 2 #+2 weil er nur die Namen unter denen die Werte in der txt gespeichert sind abrufen soll/muss, nicht die Werte selbst.
    data[i] = str(value) #der mitgegebene Wert wird zum String und ersetzt das zuvor ermittelte Listenelement.
    text = open("settings.txt", "w") #Die txt wird erneut geöffnet, diesmal im schreibmodus. Der Inhalt wird Vollständig überschrieben.
    #Die veränderte Liste wird Element für Element in die leere txt eingetragen.
    for i in range(len(data)):
        text.write(data[i] + "\n") #Nach jedem Element wird ein Zeilenumbruch eingefügt.
    text.close()

#Prüft und gibt aus, ob das Verhältnis von Karten im Spiel und Startkarten pro Spielende Partei bei Veränderung einer dieser Werte stimmt.
def cards_check(parameter):
    #Prüft für einen Bot mehr als aktuell.
    if parameter == "number_of_bots":
        # Die Anzahl der Startkarten muss gleich oder niedriger sein als die Gesamtanzahl der Karten im Spiel 
        # geteilt duch die anzahl an Bots plus zwei (+1 für den Spieler, +1 für einen Bot mehr).
        if int(textdatei("number_of_cards", "null")) <= (int(textdatei("colors", "null"))*14) / (int(textdatei("number_of_bots", "null"))+2):
            return("True")
        else:
            return("False")
     #Prüft für eine Startkarte mehr als aktuell.
    if parameter == "number_of_cards":
        if int(textdatei("number_of_cards", "null"))+1 <= (int(textdatei("colors", "null"))*14) / (int(textdatei("number_of_bots", "null"))+1):
            return("True")
        else:
            return("False")
     #Prüft für eine Farbe weniger als aktuell.
    if parameter == "colors":
        if int(textdatei("number_of_cards", "null")) <= ((int(textdatei("colors", "null"))-1)*14) / (int(textdatei("number_of_bots", "null"))+1):
            return("True")
        else:
            return("False")