luvut = []

while True:
    luku = input("Anna luku tai paina Enter lopettaaksesi: ")
    if luku =="":
        break
    try:
        luku = int(luku)
        luvut.append(luku)
    except ValueError:
        print("Syötetty luku ei ollut kelvollinen kokonaisluku.")

    viisi_suurinta = sorted(luvut, reverse=True)

print("Viisi suurinta lukua ovat:")
for luku in viisi_suurinta:
     print(luku)
