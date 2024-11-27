print("=" * 40)
print("\tKonversi Radian Ke Derajat")
print("=" * 40)

import math

#Konversi Radian Ke Derajat

#Input
radian = float(input("Masukan Nilai Sudut Dalam Radian\t= "))

#Rumus
derajat2 = radian * (180/math.pi)
derajat3 = math.degrees(radian)

#Tampilan Hasil Konversi Radian Ke Derajat
print("Hasil Konversi (Rumus) \t\t\t=",radian, "=", derajat2, "Derajat")
print("Hasil Konversi (Modul Math Python) \t=",radian, "=", derajat3, "Derajat")
print()