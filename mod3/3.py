sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()

hemoglobiiniarvo = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli =="nainen":
    if hemoglobiiniarvo < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiiniarvo <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")

elif sukupuoli == "mies":
    if hemoglobiiniarvo < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiiniarvo < 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")



