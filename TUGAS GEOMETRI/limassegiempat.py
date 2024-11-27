print("=" * 55)
print("\tVolume Dan Luas Permukaan Limas Segiempat")
print("=" * 55)

s = int(input("Masukan Nilai Sisi\t\t\t\t= "))
lst = int(input("Masukan Nilai Luas Sisi Tegak\t\t\t= "))
t = int(input("Masukan Nilai Tinggi\t\t\t\t= "))

#Rumus
volume = 1/3 * (s *s) * t
luas_permukaan = (s *s) + (4 * lst)

print("Volume Dari Limas Segiempat Adalah\t\t=",volume)
print("Luas Permukaan Dari Limas Segiempat Adalah\t=",luas_permukaan)