print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segitiga")
print("=" * 55)

def limas_segitiga():
    la = int(input("Masukan Nila Luas Alas\t\t\t\t= "))
    ls = int(input("Masukan Nila Luas Sisi\t\t\t\t= "))
    luas = int(input("Masukan Nilai Luas\t\t\t\t= "))
    t = int(input("Masukan Nilai Tinggi\t\t\t\t= "))

    #Rumus
    volume = lambda l, t : 1/3 * luas * t
    luas_permukaan = lambda la, ls:  la + ls

    print("Nilai Volume Dari Limas Segitiga Adalah\t\t=",volume(luas, t))
    print("Nilai Luas Permukaan Limas Segitiga Adalah\t=",luas_permukaan(la, ls))

limas_segitiga()