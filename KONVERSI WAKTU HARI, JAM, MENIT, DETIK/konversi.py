print("=" * 65)
print("\tMengKonversi Waktu Dari Hari, Jam, Menit, dan Detik")
print("=" * 65)

#input waktu nya
nilai = input("Masukan Detik Nya = ")
satuan = 60
detik = int(nilai)

#konversi hari
hari = int(detik / (satuan * satuan * 24))
detik = int(detik - (satuan * satuan * 24) * hari)

#konversi jam
jam = int(detik / (satuan * satuan))
detik = int(detik - (satuan * satuan) * jam)

#konversi menit
menit = int(detik / satuan)

#konversi detik
detik = int(detik - (satuan * menit))

print(f"Hari = ", hari )
print(f"Jam = ", jam)
print(f"Menit = ", menit)
print(f"Detik = ", detik)