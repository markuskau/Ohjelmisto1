luoti_grammoina = 13.3
naula_luoteina = 32
leiviska_nauloina = 20

leiviskat = int(input("Anna leivisköiden määrä: "))
naulat = int(input("Anna naulojen määrä: "))
luodit = int(input("Anna luotijen määrä: "))

kokonais_luodit = (leiviskat * leiviska_nauloina * naula_luoteina) + (naulat * naula_luoteina) + luodit
grammat = kokonais_luodit * luoti_grammoina

kilogrammat = int(grammat // 1000)
jäljellä_grammat = grammat % 1000

print(f"Massa on {kilogrammat} kg ja {jäljellä_grammat:.1f} g.")
