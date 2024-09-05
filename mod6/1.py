import random

def heita_noppaa():
    return random.randint(1, 6)

def ohjelma():
    silmaluku = 0
    while silmaluku != 6:
        silmaluku = heita_noppaa()
        print(f"Nopan silmäluku: {silmaluku}")

ohjelma()
