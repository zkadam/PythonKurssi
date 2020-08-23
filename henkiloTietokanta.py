import sqlite3

print("aloitetaan suoritus")
conn=sqlite3.connect("henkilot.db")
print("tietokanta avattu")

#VAIHE 1, TIETOKANNAN RANKENTEEN LUONTI
sql = """CREATE TABLE IF NOT EXISTS nimet(
        nimi text, ikä integer)"""

print("Lisätään taulu tietokantaan")

kursori=conn.cursor()
kursori.execute(sql)
print("taulu lisätty tietokantaan")

#VAIHE 2, LISÄTÄÄN RIVI KANTAAN
nimi=input("Anna henkilön nimi: ")
ikä=input("Anna henkilön ikä: ")

print("Tallennetaan tietokantaan...")
sql=f'INSERT INTO nimet VALUES ("{nimi}",{ikä})'
kursori.execute(sql)
conn.commit()
print("Tallennus tehty")

#VAIHE 3 - TULOSTETAAN RIVIT KANNASTA

print("---------------------------------")
print("Tietokannan sisältö:")
sql="SELECT nimi, ikä FROM nimet"
for rivi in kursori.execute(sql):
    print(rivi)
#SULETAAN TIETOKANTAYHTEYS
conn.close()
print("Tietokanta suljettu")