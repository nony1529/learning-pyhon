#Menghitung Luas dan Keliing Belah Ketupat
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def ketupat ():
    diagonal1 = int(input("Masukan nilai diagonal 1\t\t= "))
    diagonal2 = int(input("Masukan nilai diagonal 2\t\t= "))
    sisi = int(input("Masukan nilai sisi\t\t\t= "))
    luas = lambda d1,d2 : 1/2 * d1 * d2
    keliling = lambda s : 4 * s

    print("Nilai Luas Belah Ketupat adalah\t\t\t= ", luas(diagonal1,diagonal2), "cm")
    print("NIlai Keliling Belah Ketupat adalah\t\t= ", keliling(sisi), "cm") 

ketupat()
ketupat()
ketupat()
ketupat()