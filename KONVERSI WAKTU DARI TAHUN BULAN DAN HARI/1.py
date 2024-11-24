print("=" * 56)
print("\tKonversi Hari Jadi Tahun, Bulan, dan Hari")
print("=" * 56)

hariAwal=int(input("Masukan Hari Awal = "))

tahun = int(hariAwal / 365)
bulan = int((hariAwal - (tahun * 365))/30)
hari = int(hariAwal - tahun * 365 - bulan * 30)

print(f'''Tahun = {tahun}\r
Bulan = {bulan}\r
Hari  = {hari} ''')