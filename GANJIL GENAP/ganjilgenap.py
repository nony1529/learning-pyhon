print("=" * 50)
print("\tMenentukan Nilai Ganjil Dan Genap")
print("=" * 50)

nilai_awal = int(input("Masukan Nilai Awal\t= "))
nilai_akhir = int(input("Masukan Nilai Akhir\t= "))

ganjil = []
genap = []
for i in range (nilai_awal, nilai_akhir + 1):
    if i%2 == 1:
        ganjil.append(i)
    if i%2 == 0:
        genap.append(i)

print("Nilai Ganjil Nya Adalah\t= ", ganjil)
print("Nilai Genap Nya Adalah\t= ", genap)