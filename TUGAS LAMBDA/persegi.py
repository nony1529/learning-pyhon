#Menghitung Luas dan Keliilng Persegi
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def persegi() :
    sisi = int(input("Masukan nilai sisi\t\t= "))
    luas = lambda s : s * s
    keliling = lambda s : 4 * s

    print("Nilai Luas Persegi adalah\t\t= ", luas(sisi), "cm")
    print("Nilai Keliing Persegi adalah\t\t= ", keliling(sisi), "cm")

persegi()
persegi()
persegi()
persegi()