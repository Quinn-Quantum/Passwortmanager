import csv
import time
from tkinter import *
from tkinter.filedialog import askopenfilename
import os
from cryptography.fernet import Fernet

# funktion zum Anzeigen der vorhandenen Passwörtr
def passwortliste(filename):
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)
        # using the key
        fernet = b'j6sdd8XoYCPjU1iGWZ1aQhMebEIFrfZoYV9nma9dTOM='
        # opening the encrypted file
        with open('nba.csv', 'rb') as enc_file:
            encrypted = enc_file.read()
        # decrypting the file
        decrypted = fernet.decrypt(encrypted)
        # opening the file in write mode and
        # writing the decrypted data
        with open(filename, 'wb') as dec_file:
            dec_file.write(decrypted)
    time.sleep(5)
    pass


# Funktion zum Passwort hinzufügen
def addpasswort(g_passwortliste,filename):
    name = input("Für was soll das Passwort sein: ")
    b_name = input("Benutzername: ")
    passwd = input("Passwort: ")
    g_passwortliste += [[name, b_name, passwd]]
    with open(filename, 'wb') as filekey:
        filekey.write(b'j6sdd8XoYCPjU1iGWZ1aQhMebEIFrfZoYV9nma9dTOM=')
    # print(g_passwortliste)
    savealles(g_passwortliste,filename)
    return g_passwortliste


# Funktion zum Passwort löschen
def delet(g_passwortliste, filename):
    name_d = input("Für was möchten sie das Paswort löschen: ")
    if name_d != "Name":
        z = 0
        while z in range(len(g_passwortliste)):
            if g_passwortliste[z][0] == name_d:
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
            if g_passwortliste[z][0] == name_u:
                print("AltesPaswort: ")
                print(g_passwortliste[z][2])
                altpaswd = g_passwortliste[z][2]
                passneu = input("neues Paswort: ")
                while altpaswd == passneu:
                    print("selbes Paswort: ")
                    print("AltesPaswort: ")
                    print(g_passwortliste[z][2])
                    altpaswd = g_passwortliste[z][2]
                    passneu = input("neues Paswort: ")
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


def db_erstellen():
    nameDate = input(('Wie soll die Datei heißen: '))
    filename = nameDate + '.csv'
    #file = open(filename, 'w', newline='')
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name","Benutzername","Paswd"])
    print("wurde erstellt")
    time.sleep(2)
    return filename
    pass



def lesendatei(filename):
    print(filename)
    passwortliste_t = []
    with open(filename) as csvdatei:
        readerCSV = csv.reader(csvdatei)

        for tabelle in readerCSV:
            # print(f' {" | ".join(tabelle)}')
            passwortliste_t += [tabelle]

    return passwortliste_t


# Main
if __name__ == '__main__':
    g_passwortliste = []
    filename = ''
    run = False
    start = True

    while start == True:
        print("==================")
        print(" Passwordmanage")
        print("==================")
        print("")
        print("7 Passwörter DB anlegen")
        print("8 Passwort DB auswählen")
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
            if auswahl == 7:
                db_erstellen()
            if auswahl == 8:
                filename = askopenfilename()
                start = False
                run = True
                g_passwortliste = lesendatei(filename)
                while run:
                    print("==================")
                    print(" Passwordmanage")
                    print("==================")
                    print("")
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
                            print('/n')
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
