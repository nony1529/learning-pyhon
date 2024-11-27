print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segiempat")
print("=" * 55)

def limas_segiempat():
    s = int(input("Masukan Nilai Sisi\t\t\t\t= "))
    lst = int(input("Masukan Nilai Luas Sisi Tegak\t\t\t= "))
    t = int(input("Masukan Nilai Tinggi\t\t\t\t= "))

    #Rumus
    volume = lambda s, t: 1/3 * (s *s) * t
    luas_permukaan = lambda lst, s : (s *s) + (4 * lst)

    print("Volume Dari Limas Segiempat Adalah\t\t=",volume(s, t))
    print("Luas Permukaan Dari Limas Segiempat Adalah\t=",luas_permukaan(lst, s))

limas_segiempat()