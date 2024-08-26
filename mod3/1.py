kuhan_pituus = float(input("Anna kuhan pituus (cm): "))


alamitta = 37.0

if kuhan_pituus <alamitta:
    puuttuva_pituus = alamitta - kuhan_pituus
    print(f"Kuha on alamittainen. Laskethan sen takaisin järveen. Kuha tarvitsee vielä {puuttuva_pituus:.1f} cm kasvaakseen sallituksi. ")

else:
    print("Kuha ei ole alamittainen. ")

