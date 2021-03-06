import csv
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
import os

# funktion zum Anzeigen der vorhandenen Passwörtr
def passwortliste(filename):
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for row in readerCSV:
            #row encoden
            row[0] = encod(row[0])
            row[1] = encod(row[1])
            row[2] = encod(row[2])
            print("{0:<20} {1:<20} {2:<20}".format(row[0],row[1] ,row[2]))
    time.sleep(3)
    pass

# Funktion zum Passwort hinzufügen
def addpasswort(g_passwortliste, filename):
    name = input("Für was soll das Passwort sein: ")
    b_name = input("Benutzername: ")
    while True:
        passwd = input("Passwort: ")
        if "~" in passwd or "#" in passwd or "^" in passwd or "°" in passwd:
            print("ungültiges Passwort")
        else:
            break
    #verschlüsseln
    name = decod(name)
    b_name = decod(b_name)
    passwd = decod(passwd)
    g_passwortliste += [[name, b_name, passwd]]
    savealles(g_passwortliste, filename)
    return g_passwortliste


# Funktion zum Passwort löschen
def delet(g_passwortliste, filename):
    name_d = input("Für was möchten sie das Paswort löschen: ")
    if name_d != "Name":
        z = 0
        while z in range(len(g_passwortliste)):
            passname = encod(g_passwortliste[z][0])
            if  passname == name_d:
                g_passwortliste.pop(z) #löschfunktion
            z = z + 1
    else:
        print("%s dafür gibt es kein Paswort" % name_d)
        time.sleep(3)
    savealles(g_passwortliste, filename)
    return g_passwortliste


# speicher Funktion
def savealles(g_passwortliste, filename):
    file = open(filename, 'w', newline='')
    with file:
        writer = csv.writer(file)
        for row in g_passwortliste:
            writer.writerow(row)
        print("wurde gespeichert")
        time.sleep(2)
        pass


# update funktion
def updatepw(g_passwortliste, filename):
    name_u = input("Für was möchten sie das Paswort updaten: ")
    z = 0
    change = True
    if name_u != "Name":
        while z in range(len(g_passwortliste)):
            passname = encod(g_passwortliste[z][0])
            if passname== name_u:
                while change == True: #damit man nicht immer in diesen menü wechsel muss um was zu ändern
                    print("1 Passwort ändern")
                    print("2 Name ändern")
                    print ("3 Fertig")
                    auswahl = (input("Was möchten sie tun: "))
                    try:  # abfrage ob tipp ein int ist
                        int(auswahl)
                        it = True
                    except ValueError:
                        it = False
                    if it:
                        auswahl = int(auswahl)
                    #paswd ändern
                    if (auswahl == 1):
                        print("Altes Passwort: ")
                        altpaswd = encod(g_passwortliste[z][2]) #paswd encoden
                        print(altpaswd)
                        passneu = input("neues Paswort: ")
                        while altpaswd == passneu: #abgleich damit nicht das selbe benuzt wird
                            print("selbes Paswort: ")
                            print("AltesPaswort: ")
                            print(altpaswd)
                            passneu = input("neues Paswort: ")
                        passneu = decod(passneu)
                        g_passwortliste[z][2] = passneu
                        change = True
                    #username ändern
                    elif (auswahl == 2):
                        print("Alter Name: ")
                        altname= encod(g_passwortliste[z][1])
                        print(altname)
                        neuname = input("neues Paswort: ")
                        while altname == neuname:
                            print("selbes Paswort: ")
                            print("AltesPaswort: ")
                            print(altname)
                            neuname = input("neues Paswort: ")
                        neuname = decod(neuname)
                        g_passwortliste[z][1] = neuname
                        change = True
                    else:
                        change = False

                z = z + 1
            else:
                z = z + 1
    else:
        print("%s dafür gibt es kein Paswort" % name_u)
        time.sleep(3)
    time.sleep(3)
    savealles(g_passwortliste, filename)
    return g_passwortliste

#erstelle eine Datei
def db_erstellen():
    nameDate = input(('Wie soll die Datei heißen: '))
    filename = nameDate + '.csv'
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        #verschlüsseln des Tabellenkopfes
        name = decod('Name')
        benutzername = decod('Benutzername')
        paswd =decod('Paswd')
        #eintragen
        writer.writerow([name, benutzername, paswd])
    print("wurde erstellt")
    time.sleep(2)
    return filename
    pass

#in liste schreiben
def lesendatei(filename):
    #print(filename)
    passwortliste_t = []
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)
        for tabelle in readerCSV:
            passwortliste_t += [tabelle]
    return passwortliste_t

#codiere einen String
def decod(text):
    codiert =""
    for zeichen in text:
        ascii = ord(zeichen) #char zu einen int
        if ascii >=153:
            if ascii == 253:
                asciineu = 0
                zeichenneu = chr(asciineu)  # int zu char
            if ascii == 254:
                asciineu = 1
                zeichenneu = chr(asciineu)  # int zu char
            if ascii == 255:
                asciineu = 2
                zeichenneu = chr(asciineu)  # int zu char
        else:
            asciineu = ascii + 3 #verschibung um 3
            zeichenneu = chr(asciineu) #int zu char
        codiert = "".join((codiert , zeichenneu))
    return codiert

#decodiere einen String
def encod(text):
    endcodiert = ""
    for zeichen in text:
        ascii = ord(zeichen)
        if ascii <=2:
            if ascii == 0:
                asciineu = 253
                zeichenneu = chr(asciineu)
            if ascii == 1:
                asciineu = 254
                zeichenneu = chr(asciineu)
            if ascii == 2:
                asciineu = 255
                zeichenneu = chr(asciineu)
        else:
            asciineu = ascii - 3
            zeichenneu = chr(asciineu)
        endcodiert = "".join((endcodiert, zeichenneu))
    return endcodiert

# Main
if __name__ == '__main__':
    g_passwortliste = [] #liste in der die CSV gespeichert wird zum lesen und verarbeiten
    filename = '' #welche CSV
    run = False
    start = True
    #Strat des eigentlichen Programmes
    while start == True:
        print("==================")
        print(" Passwordmanager")
        print("==================\n")
        print("1 Passwörter DB anlegen")
        print("2 Passwort DB auswählen")
        print("6 Exit")
        auswahl = (input("Was möchten sie tun: "))
        try:  # abfrage ob tipp ein int ist
            int(auswahl)
            it = True
        except ValueError:
            it = False
        if it:
            auswahl = int(auswahl)
            if auswahl == 6:
                exit()
            if auswahl == 1:
                db_erstellen()
            if auswahl == 2:
                filename = askopenfilename()
                start = False
                run = True
                g_passwortliste = lesendatei(filename)
                while run:
                    #funktionen zum bearbeiten einer CSV
                    print("==================")
                    print(" Passwordmanager")
                    print("==================\n")
                    print("1 Passwörter anzeigen")
                    print("2 Passwort Add")
                    print("3 Lösche eines Passwortes")
                    print("4 update Passwort")
                    print("5 Save")
                    print("6 Exit")
                    eingabe = (input("Was möchten sie tun: "))
                    try:  # abfrage ob tipp ein int ist
                        int(eingabe)
                        it_is = True
                    except ValueError:
                        it_is = False
                    # Eingabe Abfrage
                    if it_is:
                        eingabe = int(eingabe)
                        if eingabe == 6:
                            print('\n')
                            start = True
                            run = False
                        if eingabe == 1:
                            passwortliste(filename)
                        if eingabe == 2:
                            addpasswort(g_passwortliste, filename)
                        if eingabe == 3:
                            delet(g_passwortliste, filename)
                        if eingabe == 4:
                            updatepw(g_passwortliste, filename)
                        if eingabe == 5:
                            savealles(g_passwortliste, filename)
                    else:
                        print("Falsche eingabe")