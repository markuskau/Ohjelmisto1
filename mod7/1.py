vuodenajat = ("talvi", "talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12): "))
if 1 <= kuukausi <= 12:
    vuodenaika = vuodenajat[kuukausi % 12]
    print(f"Kuukausi {kuukausi} kuuluu vuodenaikaan: {vuodenaika}")
