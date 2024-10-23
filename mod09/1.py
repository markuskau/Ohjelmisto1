class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):

        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
        self.matka = 0


def pääohjelma():

    auto = Auto("ABC-123", 142)

    print(f"Rekisteritunnus: {auto.rekisteritunnus}")

