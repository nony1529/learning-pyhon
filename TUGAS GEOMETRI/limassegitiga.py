print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segitiga")
print("=" * 55)

la = int(input("Masukan Nila Luas Alas\t\t\t\t= "))
ls = int(input("Masukan Nila Luas Sisi\t\t\t\t= "))
luas = int(input("Masukan Nilai Luas\t\t\t\t= "))
t = int(input("Masukan Nilai Tinggi\t\t\t\t= "))

#Rumus
volume = 1/3 * luas * t
luas_permukaan = la + ls

print("Nilai Volume Dari Limas Segitiga Adalah\t\t=",volume)
print("Nilai Luas Permukaan Limas Segitiga Adalah\t=",luas_permukaan)