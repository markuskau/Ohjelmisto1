def lentoasematiedot():
    lentoasemat = {}

    while True:
        print("\nValitse toiminto:")
        print("1: Syötä uusi lentoasema")
        print("2: Hae lentoaseman tiedot")
        print("3: Lopeta")

        valinta = input("Anna numero (1/2/3): ")

        if valinta == '1':
            icao = input("Anna lentoaseman ICAO-koodi: ").upper()
            nimi = input("Anna lentoaseman nimi: ")
            lentoasemat[icao] = nimi
            print(f"Lentoasema {nimi} lisätty ICAO-koodilla {icao}.")

        elif valinta == '2':
            icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper()
            if icao in lentoasemat:
                print(f"Lentoaseman nimi ICAO-koodilla {icao} on {lentoasemat[icao]}.")
            else:
                print(f"Lentoasemaa ICAO-koodilla {icao} ei löytynyt.")

        elif valinta == '3':
            print("Ohjelma lopetetaan.")
            break

        else:
            print("Virheellinen valinta, yritä uudelleen.")

lentoasematiedot()
