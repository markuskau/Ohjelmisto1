import random

arpakuutio = int(input("Kuinka monta arpakuutiota haluat heittää? "))
summa = 0
for i in range(arpakuutio):
    heitto = random.randint(1, 6)
    summa +=heitto
    print(f"Arpakuutio {i+1}: {heitto}")
print(f"Silmälukujen summa: {summa}")
