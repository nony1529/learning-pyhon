print("=" * 54)
print("\t\tMencari Nilai Faktor")
print("=" * 54)

def cari_faktor(angka):
    faktor = []

    for i in range (1, angka +1 , 1):
        if(angka % i == 0):
            faktor.append(i)

    return faktor

def main():
    angka = int(input("Masukan Bilangan Yang Ingin Dicari Faktor Nya   = "))

    faktor = cari_faktor(angka)

    print("Faktor - Faktor Dari", angka, "Adalah\t\t\t= ", faktor)

main()