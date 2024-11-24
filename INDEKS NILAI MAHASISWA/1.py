print("=" * 56)
print("\tMenentukan Indeks Nilai Mahasiswa")
print("=" * 56)

nilai = int(input("Masukan Nilai Ujian = "))

if nilai >= 80:
    print("A")
elif 70 <= nilai <= 80 :
    print("B")
elif 55 <= nilai <= 70:
    print("C")
elif 40 <= nilai <= 55:
    print("D")
elif nilai <= 40:
    print("E")
else:
    print("Tidak Ada Nilai")