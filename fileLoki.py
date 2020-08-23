def kirjoita_lokiin():
    teksti=open("teksti.txt","ta")
    teksti.write("\n")
    import datetime
    teksti.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S: "))

    teksti.write(input("Kirjoita uusi rivi: "))
    teksti.close()
    teksti=open("teksti.txt","r")
    print(teksti.read())
    teksti.close()
kirjoita_lokiin()