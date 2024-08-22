import math
name = input("Anna nimesi: ")
print("Moi  " + name)


age = input("Anna ikäsi: ")
print("Ikäsi on " + age)

age = int(age) + 1
age_string = str(age)
print("Ikäsi on vuoden päästä " + age_string)

age = age + 1
print("Ikäsi on kahden vuoden päästä " + str(age))

height = float(input("Anna pituus (m): "))
height = height + 0.1
print(f"Nimi: {name}, Ikä: {age*2} , Pituus: {height:.2f} metriä,")


print(math.pi)

