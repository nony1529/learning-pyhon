print("=" * 64)
print("\t\t\tMenghitung Umur")
print("=" * 64)

import datetime as dt
print("")
print("\t***Masukan Tanggal, Bulan, Dan Tahun Lahir Anda***")
print('')

tanggal = int(input("Masukan Tanggal Lahir\t\t= "))
bulan = int(input("Masukan Bulan Lahir \t\t= "))
tahun = int(input("Masukan Tahun Lahir \t\t= "))

lahir = dt.date(tahun,bulan,tanggal)
print("Tanggal lahirmu Adalah\t\t=",lahir)

hari_sekarang = dt.date.today()
print(f"Hari Ini Tanggal\t\t=", hari_sekarang)

umur_hari = hari_sekarang - lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) // 30

print(f"Hari Nya Adalah\t\t\t= {lahir:%A}")
print(f"Umur Anda Adalah\t\t= {umur_tahun} Tahun, {umur_bulan_sisa} Bulan")