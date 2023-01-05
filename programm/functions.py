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
