#Menghitung Luas Permukaan dan Volume Prisma Segitiga Siku Siku
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def prisma() :
    alas = int(input("Masukan nilai alas\t\t= "))
    tinggi = int(input("Masukan nilai tinggi\t\t= "))
    luas_permukaan = lambda a,t : 1/2 * (a *t)
    volume = lambda a,t : 1/2 * (a *t) * t

    print("Nilai Luas Permukaan Prisma Segitiga adalah\t= ", luas_permukaan(alas,tinggi), "cm3")
    print("Nilai Volume Prisma Segitiga adalah\t\t= ", volume(alas,tinggi), "cm3")

prisma()
prisma()
prisma()
prisma()