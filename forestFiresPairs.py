tiedosto = open("forestfires.csv","r")

viikonpaivat={"mon":0,"tue":0,"wed":0,"thu":0,"fri":0,"sat":0,"sun":0}
lineNumber=1

for rivi in tiedosto:
    if lineNumber>1:
        viikonpaiva=rivi[8:11]
        viikonpaivat[viikonpaiva]+=1
    lineNumber+=1

tiedosto.close()
# lasketaan montako kertaa on listalla jokainen päivä
print(viikonpaivat)
