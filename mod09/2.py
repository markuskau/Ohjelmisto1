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



def paaohjelma():
    auto = Auto("ABC-123", 142)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huippunopeus: {auto.huippunopeus} km/h")
    print(f"Nykyinen nopeus: {auto.nopeus} km/h")

    auto.kiihdytys(30)
    auto.kiihdytys(70)
    auto.kiihdytys(50)

    print(f"Kiihdytyksen jälkeen nopeus: {auto.nopeus} km/h")

    auto.kiihdytys(-200)

    print(f"Hätäjarrutuksen jälkeen nopeus: {auto.nopeus} km/h")

if __name__ == "__main__":
    paaohjelma()
