print("=" * 46)
print("\tMembuat Program Mencari KPK")
print("=" * 46)

def cari_kpk (a, b):
    kpk = max(a, b)
    cari = kpk

    while (kpk == max(a, b)):
        if (cari % a == 0) and (cari % b == 0):
            kpk = cari
        cari += 1

    return kpk

def main():
    bilangan1 = int(input("Masuka Bilangan Pertama = "))
    bilangan2 = int(input("Masukan Bilangan Kedua = "))

    hasil_kpk = cari_kpk(bilangan1, bilangan2)
    print("KPK dari", bilangan1, "dan", bilangan2, "adalah", hasil_kpk)

main()