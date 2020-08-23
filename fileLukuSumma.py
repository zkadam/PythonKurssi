numerot = open("lukuja.txt","r")
summa=0
lineNumber=1
for rivi in numerot:
    print(str(lineNumber) + " : " + rivi)
    lineNumber+=1
    summa+=int(rivi)
numerot.close()
print("loppusumma on: " + str(summa))