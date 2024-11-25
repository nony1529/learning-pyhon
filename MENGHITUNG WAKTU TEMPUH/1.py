print("=" * 47)
print("\tProgram Menghitung Waktu Tempuh")
print("=" * 47)

tempuh = 0.0
jarak = 0.0
kecepatan = 0.0

jarak = float(input("Masukan Nilai Jarak (KM)\t\t= "))
kecepatan = float(input("Masukan Nilai Kecepatan (KM/JAM)\t= "))

tempuh = jarak/kecepatan
print("Waktu Tempuh Nya Adalah\t\t\t=",tempuh, "jam")