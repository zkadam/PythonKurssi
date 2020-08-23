class OmaLuokka:
    oma_arvo=100
    
    def testi(self):
        print("OmaLuokka.testi -metodissa...")

class Auto:
    huippunopeus:0

# urheiluauto class gets the auto class parameters
class UrheiluAuto(Auto):
    pass

print("Suoritus alkaa...")

instanssi=OmaLuokka()
instanssi.testi()

instanssi2=OmaLuokka()
instanssi2.testi()

print("Suoritus päättyy.")