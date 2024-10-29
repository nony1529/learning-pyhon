print("=" * 45)
print("\tMenentukan Nilai Ganjil")
print("=" * 45)

awal = int(input("Masukan Nilai Awal\t= "))
akhir = int(input("Masukan Nilai Akhir\t= "))

ganjil = []
for i in range (awal, akhir +1) :
    if i%2 == 1:
        ganjil.append(i)

print("Nilai Ganjil Nya Adalah\t= ", ganjil)