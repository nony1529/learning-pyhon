print("=" *50)
print('\tMengurutkan Angka Dari YAng Terbesar Ke Yang Terkecil')
print("=" *50)

y = int(input("Berapa Banyak Angka Yang Ingin Di Masukan = "))

bilangan = []

for i in range (y) :
    angka = int(input("Masukan Angka\t\t\t\t= "))
    bilangan.append(angka)
print("Angka Sebelum Di Urutkan\t\t=", bilangan)
bilangan.sort()
print("Angka Sesudah Di Urutkan\t\t=", bilangan)