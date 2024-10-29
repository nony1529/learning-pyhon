print("=" * 45)
print("\tMenentukan Nilai Genap")
print("=" * 45)

awal = int(input("Masukan Nilai Awal\t= "))
akhir = int(input("Masukan Nilai Akhir\t= "))

genap = []
for i in range (awal, akhir + 1):
    if i%2 == 0:
        genap.append(i)

print("Nilai Genap Nya Adalah\t= ", genap)