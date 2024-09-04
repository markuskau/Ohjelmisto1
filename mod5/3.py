def onko_alkuluku(luku):
    if luku < 2:
        return False
    for i in range(2, int(luku ** 0.5) + 1):
        if luku % i == 0:
            return False
    return False

luku = int(input("Anna kokonaisluku: "))

if onko_alkuluku(luku):
    print(f"Luku {luku} on alkuluku.")
else:
    print(f"Luku {luku} ei ole alkuluku.")

