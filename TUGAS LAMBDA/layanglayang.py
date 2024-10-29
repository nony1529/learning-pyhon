#Menghitung Luas dan Keliling Layang Layang
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def layang ():
    diagonal1 = int(input("Masukan nilai diagonal 1\t\t= "))
    diagonal2 = int(input("Masukan nilai diagonal 2\t\t= "))
    sisi1 = int(input("Masukan nilai sisi 1\t\t\t= "))
    sisi2 = int(input("Masukan nilai sisi 2\t\t\t= "))
    keliling = lambda d1,d2 : 1/2 * (d1 * d2)
    luas = lambda s1,s2 : 2 * (s1+s2)

    print("Nilai Keliling Layang Layang adalah\t\t= ", keliling(sisi1,sisi2), "cm")
    print("Nilai Luas Layang layang adalah\t\t\t= ", luas(diagonal1,diagonal2), "cm")

layang()
layang()
layang()
layang()