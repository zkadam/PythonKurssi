tiedosto = open("forestfires.csv","r")
summa=0
lineNumber=1
monFires=0
tueFires=0
wedFires=0
thuFires=0
friFires=0
satFires=0
sunFires=0
spellmiatake=0
for rivi in tiedosto:
    if lineNumber>1:
        viikonpaiva=rivi[8:11]
        print(viikonpaiva)
        if viikonpaiva =="mon":
            monFires+=1
        elif viikonpaiva=="tue":
            tueFires+=1
        elif viikonpaiva=="wed":
            wedFires+=1
        elif viikonpaiva=="thu":
            thuFires+=1
        elif viikonpaiva=="fri":
            friFires+=1
        elif viikonpaiva=="sat":
            satFires+=1
        elif viikonpaiva=="sun":
            sunFires+=1
        else:
            print("Tuntematon viikonpäivä: " + viikonpaiva)
        
    lineNumber+=1

tiedosto.close()
# tulostus
print("Monday fires: " + str(monFires))
print("Tuesday fires: " + str(tueFires))
print("Wednesday fires: " + str(wedFires))
print("Thursday fires: " + str(thuFires))
print("Friday fires: " + str(friFires))
print("Saturday fires: " + str(satFires))
print("Sunday fires: " + str(sunFires))
