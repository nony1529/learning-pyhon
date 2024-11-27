print("=" * 55)
print("\tVolume Dan Luas Permukaan Kerucut")
print("=" * 55)

phi = 3.14
def kerucut():
    r = int(input("Masukan Nilai Jari-Jari\t\t= "))
    t = int(input("Masukan Nilai Tinggi\t\t= "))
    s = int(input("Masukan Nilai Sisi\t\t= "))

    volume = lambda r, t: 1/3 * phi * r**2 * t
    luas_permukaan = lambda r, s : (phi * r**2) + (phi * r * s)

    print("Volume Kerucut Adalah\t\t=",volume(r,t))
    print('Luas Permukaan Kerucut Adalah\t=',luas_permukaan(r,s))

kerucut()