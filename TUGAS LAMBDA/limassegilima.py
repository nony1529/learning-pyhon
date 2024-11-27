print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segilima")
print("=" * 55)

def limas_segilima():
    la = int(input("Masukan Nilai Luas Alas\t\t\t= "))
    keliling = int(input("Masukan Nilai Keliling Alas\t\t= "))
    t = int(input("Masukan Nilai Tinggi\t\t\t= "))

    #rumus
    volume = lambda la, t : 1/3 * la * t
    luas_permukaan = lambda la, keliling, t : 2 * la + (keliling * t)

    print("Volume Limas Segilima Adalah\t\t=",volume(la, t))
    print("Luas Permukaan Limas Segilima Adalah\t=",luas_permukaan(t, la, keliling))

limas_segilima()   