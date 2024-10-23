import random

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

def paaohjelma():

    autot = []
    for i in range(1, 11):
        rekisteritunnus = f"ABC-{i}"
        huippunopeus = random.randint(100, 200)
        autot.append(Auto(rekisteritunnus, huippunopeus))

    auto_kilpailu = True
    tunti = 0

    while auto_kilpailu:
        tunti += 1
        print(f"\nTunti {tunti}:")

        for auto in autot:
            nopeuden_muutos = random.randint(-10, 15)
            auto.kiihdytys(nopeuden_muutos)

            auto.kulje(1)

            print(f"{auto.rekisteritunnus}: Nopeus {auto.nopeus} km/h, Kuljettu matka {auto.matka:.1f} km")

            if auto.matka >= 10000:
                auto_kilpailu = False
                break

    print("\nKilpailu päättyi! Tulokset:")
    print(f"{'Rekisteritunnus':<15}{'Huippunopeus (km/h)':<20}{'Nykyinen nopeus (km/h)':<25}{'Kuljettu matka (km)':<20}")
    print("-" * 80)

    for auto in autot:
            print(f"{auto.rekisteritunnus:<15}{auto.huippunopeus:<20}{auto.nopeus:<25}{auto.matka:<20.1f}")

if __name__ == "__main__":
    paaohjelma()