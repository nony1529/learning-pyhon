print("=" * 46)
print("\tMembuat Program Mencari KPK")
print("=" * 46)

def angka_kpk (x, y):
    kpk = max(x, y)
    cari = kpk

    while (kpk == max(x, y)):
        if (cari % x == 0) and (cari% y == 0):
            kpk = cari
        cari += 1

        return kpk

def main ():
    angka1 = int(input("Masukan Bilangan Pertama\t= "))
    angka2 = int(input("Masukan Bilangan Kedua\t\t= "))

    hasil_kpk = angka_kpk(angka1, angka2)
    print("KPK dari", angka1, "dan", angka2, "adalah\t=",hasil_kpk)

main()