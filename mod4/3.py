def main():
    luvut = []

    while True:
        syote = input("Anna luku (tai tyhjä lopettaaksesi): ")

        if syote == "":
            break

        try:
            luku = float(syote)
            luvut.append(luku)
        except ValueError:
            print("Syöte ei ollut kelvollinen luku. Yritä uudelleen.")

    if luvut:
        print(f"Pienin luku: {min(luvut)}")
        print(f"Suurin luku: {max(luvut)}")
    else:
        print("Et syöttänyt yhtään lukua.")

if __name__ == "__main__":
    main()



