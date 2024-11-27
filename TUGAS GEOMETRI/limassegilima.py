print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segilima")
print("=" * 55)

la = int(input("Masukan Nilai Luas Alas\t\t\t= "))
keliling = int(input("Masukan Nilai Keliling Alas\t\t= "))
t = int(input("Masukan Nilai Tinggi\t\t\t= "))

#rumus
volume = 1/3 * la * t
luas_permukaan = 2 * la + (keliling * t)

print("Volume Limas Segilima Adalah\t\t=",volume)
print("Luas Permukaan Limas Segilima Adalah\t=",luas_permukaan)