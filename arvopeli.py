Jatkuu="k"
while Jatkuu=="k":

    import  random
    randomNum = random.randrange(1,21)

    for x in range(3):
        arvo = input("Arvaa numero välillä 1-20: ")
        arvo = int(arvo)
        if  arvo>randomNum:
            print("Sinun arvosi on suurempi kun random numero")
            # print(randomNum)

        elif arvo<randomNum:
                print("Sinun arvosi, '",arvo,"' on pienempi kun random numero")
                # print(randomNum)
        else:
            print("Arvasit oikein, random numero oli : ",randomNum)
            break
        if x ==2:
            print("Et pystunyt arvaamaan numero, se oli: ",randomNum)
    print("Peli loppui, haluatko pelata uudestaan? k/e")        
    Jatkuu = input()
