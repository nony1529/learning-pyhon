print("=" * 40)
print("\tMenghitung Cos, Sin, Tan")
print("=" * 40)

import math

derajat = int(input("Masukan Nilai Sudut Dalam Derajat\t= "))

#Rumus
rad = (math.pi / 180) * derajat

#Rumus Cos, Sin, Tan
sin = math.sin(rad)
cos = math.cos(rad)
tan = math.tan(rad)

#Tampilan Hasil Konversi Sin, Cos, Tan
print("Hasil Sinus\t\t\t\t=", derajat, "=", round(sin, 3))
print("Hasil Cosinus\t\t\t\t=", derajat, "=", round(cos, 3))
print("Hasil Tangen\t\t\t\t=", derajat, "=", round(tan, 3))
print()