print("=" * 40)
print("\tMenampilkan Kalender")
print("=" * 40)

import calendar

tahun = int(input("Masukan Tahun = "))
bulan = int(input("Masukan Bulan = "))
print("")
print(calendar.month(tahun, bulan))