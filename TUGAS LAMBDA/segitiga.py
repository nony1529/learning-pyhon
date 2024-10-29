#Menghitung Luas dan Keliling Segitiga
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def segitiga() :
    alas = int(input("Masukan nilai alas\t= "))
    tinggi = int(input("Masukan nilai tinggi\t= "))
    sisi1 = int(input("Masukan nilai sisi 1\t= "))
    sisi2 = int(input("Masukan nilsi sisi 2\t= "))
    sisi3 = int(input("Masukan nilai sisi 3\t= "))
    luas = lambda s1,s2,s3 : s1 + s2 + s3
    keliling = lambda a,t : 1/2 * a * t

    print("Nilai Luas Persegi adalah\t= ", luas(sisi1,sisi2,sisi3), "cm")
    print("Nilai Keliling Persegi adalah\t= ", keliling(alas,tinggi), "cm")

segitiga()
segitiga()
segitiga()
segitiga()