tiedosto = open("forestfires.csv","r")
viikko_lista=[]
paivat_lista=['mon','tue','wed','thu','fri','sat','sun']
lineNumber=1
# viedään jokaisen päivän listalle
for rivi in tiedosto:
    if lineNumber>1:
        viikonpaiva=rivi[8:11]
        viikko_lista.append(viikonpaiva)
    lineNumber+=1

tiedosto.close()
# lasketaan montako kertaa on listalla jokainen päivä
x=1
y=len(paivat_lista)
most_fires=['nullDay',0]
for x in range(y):
    print(f"{paivat_lista[x]} fires occured: {viikko_lista.count(paivat_lista[x])} times.")
# tarkistetaan onko juuri katsomassa oleva päivän palomääriä ovat korkeinta
    if most_fires[1]<viikko_lista.count(paivat_lista[x]):
        most_fires[0]=paivat_lista[x]
        most_fires[1]=viikko_lista.count(paivat_lista[x])
    x+=1
print(f"Most  fires occured on {most_fires[0]}: {most_fires[1]} fire cases.")
