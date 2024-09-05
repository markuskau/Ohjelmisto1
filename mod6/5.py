def suodata_parilliset(lista):
    return [luku for luku in lista if luku % 2 == 0]


def syote():
    alkuperäinen_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    karsittu_lista = suodata_parilliset(alkuperäinen_lista)
    print("Alkuperäinen lista:", alkuperäinen_lista)
    print("Karsittu lista :", karsittu_lista)
syote()