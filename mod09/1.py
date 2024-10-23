class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


def paaohjelma():

    auto = Auto("ABC-123", 142)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}")
    print(f"Huipunopeus: {auto.huippunopeus} km/h")
    print(f"Nopeus: {auto.nopeus} km/h")
    print(f"Matka: {auto.matka} km")

if __name__ == "__main__":
     paaohjelma()

