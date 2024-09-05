def gallona_litroina(gallonat):
    return gallonat * 3.785

def syote():
    while True:
        gallonat = float(input("Anna bensiini gallonoina (negatiivinen luku lopettaa ohjelman): "))

        if gallonat < 0:
          print("Ohjelma lopetettu. ")
          break

        litrat = gallona_litroina(gallonat)
        print(f"{gallonat} gallonoina on {litrat:.2f} litraa. ")


syote()
