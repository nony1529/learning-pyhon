print("=" * 45)
print("\tKonversi Derajat Ke Radian")
print("=" * 45)


import math
#Konversi Derajat Ke Radian

#input
derajat = int(input("Masukan Nilai Sudut Dalam Derajat\t= "))

#Rumus
rad = (math.pi / 180) * derajat
#Modul Math Python
rad2 = math.radians (derajat)

#Tampilan Hasil Konversi Derajat Ke Radian
print("Rumus\t\t\t\t\t=", rad, "Radian")
print("Modul Math Python\t\t\t=", round(rad2, 3), "Radian")
print()
