class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


    def kiihdytys(self, muutos):
        uusi_nopeus = self.nopeus + muutos

        if uusi_nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        elif uusi_nopeus < 0:
            self.nopeus = 0
        else:
            self.nopeus = uusi_nopeus

    def kulje(self, tunnit):
        kuljettu_matka = self.nopeus * tunnit
        self.matka += kuljettu_matka
        print(f"Auto kulki {kuljettu_matka:.1f} km/h {tunnit} tuntia. Uusi kuljettu matka: {self.matka:.1f} km")



def paaohjelma():
    auto = Auto("ABC-123", 142)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Nykyinen nopeus: {auto.nopeus} km/h")
    print(f"Kuljettu matka: {auto.matka} km")

    auto.kiihdytys(60)
    auto.kulje(1.5)
    auto.kiihdytys(30)
    auto.kulje(2)
    auto.kiihdytys(-200)

    print(f"Hätäjarrutuksen jälkeen nopeus: {auto.nopeus} km/h")

    auto.kulje(1)

if __name__ == "__main__":
    paaohjelma()
