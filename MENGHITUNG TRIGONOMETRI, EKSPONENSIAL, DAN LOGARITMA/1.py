print("=" * 67)
print("\tMenghitung Trigonometri, Eksponensial, Dan Logaritma")
print("=" * 67)

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

#Rumus Cos, Sin, Tan
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

#Tampilan Hasil Konversi Sin, Cos, Tan
print("Hasil Sinus\t\t\t\t=", derajat, "=", round(sin, 3))
print("Hasil Cosinus\t\t\t\t=", derajat, "=", round(cos, 3))
print("Hasil Tangen\t\t\t\t=", derajat, "=", round(tan, 3))
print()

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

#Trigonometri
x = float(input("Masukan Gaya Komponen 1\t\t\t= "))
y = float(input("Masukan Gaya Komponen 2\t\t\t= "))
print()

#Arc Tan (x/y) = theta (rad)
rad = math.atan(y/x)
sudut = math.degrees(rad)
print("Maka Nilai Sudut\t\t\t=", sudut)

#Exponensial
j = 0
print("Hasil Eksponensial",j, "\t\t\t=", math.exp(j))
print()

#Algoritma
k = 100
print("Hasil Logaritma",k, "\t\t\t=", math.log(k))
print("Hasil Logaritma Basis 10",k, "\t\t=", math.log10(k))