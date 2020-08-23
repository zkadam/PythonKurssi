def tietokantataulun_luonti():
    sql = """CREATE TABLE IF NOT EXISTS paikkakunnat(
        paikkakunta text)"""
    kursori.execute(sql)

# -----------------------------------------funktio joka pyytää paikkakunnan nimi, tarkistaa onko olemassa ja lisaa tietokantaan jos on
def lisaa_paikkakunta():
    paikkakunta=input("Anna lisättävän paikkakunnan nimi: ")
    import http.client
    conn=http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
    conn.request("GET", "/saa/" + paikkakunta,)
    vastaus=conn.getresponse()

    if vastaus.status > 200:
        print('paikkakunta ei löytyy')
    else:
        print("Tallennetaan tietokantaan...")
        sql=f'INSERT INTO paikkakunnat VALUES(?)'
        kursori.execute(sql,(paikkakunta,))
        dbconn.commit()
        print("Tallennus tehty")
    
def paikkakunta_dbtulostus():
    print("---------------------------------")
    print("Täällä hetkellä näitä paikkakuntia seurataan:")
    sql="SELECT paikkakunta FROM paikkakunnat"
    for rivi in kursori.execute(sql):
        print(rivi)
    
    print("Tietokanta suljettu")
def Seuranta_muutos():
    print("Haluatko muuttaa seurattavia paikkakuntia?")
    whats_next=input("'k'=kyllä(poistaa kaiken), 'l'=lisää uuden paikkakunnan, 'x'=ei muutoksia")
    while whats_next.upper() != 'X':
        if whats_next.upper()=='K':
            sql="DELETE FROM paikkakunnat"
            kursori.execute(sql)
            lisaa_paikkakunta()
            paikkakunta_dbtulostus()
            print("Haluatko muuttaa seurattavia paikkakuntia? \n 'k'=kyllä(poistaa kaiken), 'l'=lisää uuden paikkakunnan, 'x'=ei muutoksia")
            whats_next=input(" ")
        elif whats_next.upper()=='L':
             lisaa_paikkakunta()  
             print("Haluatko muuttaa seurattavia paikkakuntia? \n 'k'=kyllä(poistaa kaiken), 'l'=lisää uuden paikkakunnan, 'x'=ei muutoksia \n")
             whats_next=input("") 
             paikkakunta_dbtulostus()
        else:
            break

def lampo_haku():
    #     seuraavaksi ohjelma kysyy haluatko hakea lämpötilatiedon ilmatieteenlaitokselta?
    # jos käyttäjä vastaa kyllä "K", ohjelma
    # lukee paikkakunnat-taulun rivit silmukassa
    # hakee ilmatieteenlaitoksen sivuilta kunkin tauluun tallennetun paikkakunnan lämpötilan
    # tulostaa tiedot siististi allekkain konsoli-ikkunaan "Paikkakunta - tab - lämpötila" (tab = sarkain taikka sopiva määrä välilyöntejä, jotta paikakuntien nimet sekä lämpötilat olisivat siististi allekkain)
    whats_next=input("Haluatko hakea läpötilatiedon imlatieteenlaitokselta? (kyllä = 'K' / ei='X')")
    if whats_next.upper()=='K':
        import http.client
        conn=http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")
        sql="SELECT paikkakunta FROM paikkakunnat"
        for rivi in kursori.execute(sql):
            paikkakunta=''.join(rivi)
            conn.request("GET", "/saa/" + paikkakunta,)
            vastaus=conn.getresponse()
            if vastaus.status > 200:
                print('lämötila tai paikkakunta ei löydy')
            else:
                html=str(vastaus.read())
                indeksi = html.index('<span class="temperature-')
                alku=indeksi+47
                loppu=alku+3
                lämpötila=html[alku:loppu]
                # print(lämpötila)x

                if lämpötila[2]=="\\":
                    lämpötila=lämpötila[0:2]
                print(f"Lämpötila Porvoossa:          {lämpötila} astetta.")
    else:
        print("Näkemiin!")

# --------------------------------------tässä alkaa pääohjelma
import sqlite3
dbconn=sqlite3.connect("saatiedot.db")
kursori=dbconn.cursor()

print("Tervetuloa sää hakuun")


tietokantataulun_luonti()
paikkakunta_dbtulostus()
Seuranta_muutos()

paikkakunta_dbtulostus()

lampo_haku()
#SULjETAAN TIETOKANTAYHTEYS
dbconn.close()

# import http.client

# conn=http.client.HTTPSConnection("www.ilmatieteenlaitos.fi")



# conn.request("GET", "/saa/porvoo",)
# vastaus=conn.getresponse()

# if vastaus.status > 200:
#    print('paikkakunta ei löytyy')
# else:
#     html=str(vastaus.read())


#     indeksi = html.index('<span class="temperature-')

#     alku=indeksi+47
#     loppu=alku+3
#     lämpötila=html[alku:loppu]
#     # print(lämpötila)
#     if lämpötila[2]=="\\":
#         lämpötila=lämpötila[0:2]
#     print(f"Lämpötila Porvoossa: {lämpötila} astetta.")