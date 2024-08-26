sukupuoli = input("Anna biologinen sukupuoli (nainen/mies): ").lower()

hemoglobiini = int(input("Anna hemoglobiiniarvo (g/l): "))

if sukupuoli =="nainen":
    if hemoglobiini < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hemoglobiini <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")

elif sukupuoli == "mies":
    if hemoglobiini < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hemoglobiini < 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")



