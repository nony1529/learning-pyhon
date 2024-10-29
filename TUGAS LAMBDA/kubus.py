#Menghitung Luas dan Keliing Kubus
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def kubus():
    jari_jari = int(input("Masukan nilai jari jari = "))
    sisi = int(input("Masukan nilai sisi = "))
    luas = lambda r : 6 * r * r
    keliling = lambda s : 6 * s

    print("Nilai Luas Kubus adalah =  ", luas(jari_jari), "cm")
    print("Nilai Keliling Kubus adalah = ", keliling(sisi), "cm")

kubus()
kubus()
kubus()
kubus()