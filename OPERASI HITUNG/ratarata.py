print("=" * 55)
print("\tMembuat Program Menghitung Rata-Rata")
print("=" * 55)

nilai, y, i, jumlah = 0, 0, 0, 0
rata_rata = 0.0

nilai = int(input("Berapa Nilai Yang Ingin Dimasukan = "))

for i in range(0, nilai):
    y = int(input("Nilai Nya Berapa\t\t  = "))
    jumlah += y

print("Jumlah Nya Adalah\t\t  =",jumlah)
rata_rata = jumlah/nilai
print("Rata-Rata Nya Adalah\t\t  =",rata_rata)