def kirjautuminen():
    oikea_kayttajatunnus = "ohjelmisto"
    oikea_salasana = "metropolia"
    yrityksia_jaljella = 5

    while yrityksia_jaljella > 0:
        kayttajatunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")

        if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
            print("Tervetuloa!")
            return
        else:
            yrityksia_jaljella -= 1
            print(f"Virheellinen käyttäjätunnus tai salasana. Yrityksiä jäljellä: {yrityksia_jaljella}")

    print("Pääsy evätty.")

kirjautuminen()
