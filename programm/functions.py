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
    
     #Checkt ob ein parameter den angegebenen value haben darf, bervor er ihn die txt eingetragen lässt und gibt entsprechend True, oder False aus.
        #wenn mode = 1, wird er auch wenn er passt nicht eingetragen.
    def integrity_check(parameter, value, mode):
    if parameter == "number_of_cards":
        if int(value) <= int(textdatei("cards_in_total", "null")) / (int(textdatei("number_of_bots", "null"))+1):
            if mode == 1:
                textdatei(parameter, value)
            return("True")
        else:
            return("False")
