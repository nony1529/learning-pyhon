print("=" * 55)
print("\tMenghitung Luas Dan Keliling Lingkaran")
print("=" * 55)

phi = 3.14
def lingkaran():
    jari_jari = int(input("Masukan nilai jari jari\t\t= "))
    luas = lambda r : phi * r**2
    keliling = lambda r : 2 * phi * r

    print("Nilai Luas Kubus adalah\t\t=",luas(jari_jari), "cm")
    print("Nilai Keliling Kubus adalah\t=",keliling(jari_jari), "cm")

lingkaran()