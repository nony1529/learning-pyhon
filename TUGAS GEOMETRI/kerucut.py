print("=" * 55)
print("\tVolume Dan Luas Permukaan Kerucut")
print("=" * 55)

phi = 3.14

r = int(input("Masukan Nilai Jari-Jari\t\t= "))
t = int(input("Masukan Nilai Tinggi\t\t= "))
s = int(input("Masukan Nilai Sisi\t\t= "))

#Rumus
volume = 1/3 * phi * r**2 * t
luas_permukaan = (phi * r**2) + (phi * r * s)

print("Volume Kerucut Adalah\t\t=",volume)
print('Luas Permukaan Kerucut Adalah\t=',luas_permukaan)