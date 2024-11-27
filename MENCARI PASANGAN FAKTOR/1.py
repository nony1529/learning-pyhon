print("=" * 56)
print("\tMencari Pasangan Faktor Dari Suatu Bilangan")
print("=" * 56)

def cari(n):
    pasangan = []

    for i in range (1, int(n**0.5) + 1):
        if (n % i == 0):
            pasang = (i, n // i)
            pasangan.append(pasang)
    return pasangan

def main():
    bilangan = int(input("Bilangan Berapa Yang Akan Dicari = "))
    pasangan = cari(bilangan)

    print("Pasangan Faktor Dari", bilangan, "Adalah  = ")
    for pair in pasangan:
        print(pair)

main()