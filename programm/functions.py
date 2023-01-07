def textdatei(parameter, value): #parameter = was gesucht wird ("number_of_cards"), value = in was der Wert geändert werden soll, beim auslesen value = "null"
    text = open("settings.txt", "r")
    data = text.read()
    text.close()
    data = data.split()
    i = 0
    while i < len(data)-1:
        if data[i] == parameter:
            if value == "null":
                return(data[i + 1])
            else:
                i = i + 1
                break
        i = i + 2
    data[i] = str(value)
    text = open("settings.txt", "w")
    for i in range(len(data)):
        text.write(data[i] + "\n")
    text.close()
    
#Checkt ob ein parameter den angegebenen value haben darf und gibt entsprechend True, oder False aus.
def cards_check(parameter):
    if parameter == "number_of_bots":
        if int(textdatei("number_of_cards", "null")) <= (int(textdatei("colors", "null"))*14) / (int(textdatei("number_of_bots", "null"))+2):
            return("True")
        else:
            return("False")
    if parameter == "number_of_cards":
        if int(textdatei("number_of_cards", "null"))+1 <= (int(textdatei("colors", "null"))*14) / (int(textdatei("number_of_bots", "null"))+1):
            return("True")
        else:
            return("False")
    if parameter == "colors":
        if int(textdatei("number_of_cards", "null")) <= ((int(textdatei("colors", "null"))-1)*14) / (int(textdatei("number_of_bots", "null"))+1):
            return("True")
        else:
            return("False")
