import csv
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
import os



# funktion zum Anzeigen der vorhandenen Passwörtr
def passwortliste(filename):
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)
        lein = 0
        for row in readerCSV:
            row[0] = encod(row[0])
            row[1] = encod(row[1])
            row[2] = encod(row[2])
            if lein == 0:

                print("%s\t%s \t%s " % (row[0], row[1], row[2]))
            else:
                print("%s\t%s \t%s "%(row[0],row[1] ,row[2]))

    time.sleep(5)
    pass


# Funktion zum Passwort hinzufügen
def addpasswort(g_passwortliste, filename):
    name = input("Für was soll das Passwort sein: ")
    b_name = input("Benutzername: ")
    passwd = input("Passwort: ")
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
                g_passwortliste.pop(z)
            z = z + 1

    else:
        print("%s dafür gibt es kein Paswort" % name_d)
        time.sleep(5)
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
    if name_u != "Name":
        while z in range(len(g_passwortliste)):
            passname =encod(g_passwortliste[z][0])
            if passname== name_u:
                print("AltesPaswort: ")
                altpaswd = encod(g_passwortliste[z][2])
                print(altpaswd)
                passneu = input("neues Paswort: ")
                while altpaswd == passneu:
                    print("selbes Paswort: ")
                    print("AltesPaswort: ")
                    print(altpaswd)
                    passneu = input("neues Paswort: ")
                passneu = decod(passneu)
                g_passwortliste[z][2] = passneu
                z = z + 1
            else:
                z = z + 1
    else:
        print("%s dafür gibt es kein Paswort" % name_u)
        time.sleep(5)
    time.sleep(4)
    savealles(g_passwortliste, filename)
    return g_passwortliste

#erstelle eine Datei
def db_erstellen():
    passkey = 'wow'
    nameDate = input(('Wie soll die Datei heißen: '))
    filename = nameDate + '.csv'
    # file = open(filename, 'w', newline='')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        name = decod('Name')
        benutzername = decod('Benutzername')
        paswd =decod('Paswd')
        writer.writerow([name, benutzername, paswd])
    print("wurde erstellt")
    time.sleep(2)
    return filename
    pass

#öffne eine Datei
def lesendatei(filename):
    print(filename)
    passwortliste_t = []
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)

        for tabelle in readerCSV:
            # print(f' {" | ".join(tabelle)}')
            passwortliste_t += [tabelle]

    return passwortliste_t

#codiere einen String
def decod(text):
    codiert =""
    for zeichen in text:
        ascii = ord(zeichen)
        asciineu = ascii + 3
        zeichenneu = chr(asciineu)
        codiert = "".join((codiert , zeichenneu))
    return codiert

#decodiere einen String
def encod(text):
    endcodiert = ""
    for zeichen in text:
        ascii = ord(zeichen)
        asciineu = ascii - 3
        zeichenneu = chr(asciineu)
        endcodiert = "".join((endcodiert, zeichenneu))
    return endcodiert

# Main
if __name__ == '__main__':

    g_passwortliste = []
    filename = ''
    run = False
    start = True

    while start == True:
        print("==================")
        print(" Passwordmanage")
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
                    print("==================")
                    print(" Passwordmanage")
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
