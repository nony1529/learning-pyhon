print("=" * 50)
print("\tMenentukan Nilai Terkecil")
print("=" * 50)

nilai1 = int(input("Masukan Nilai 1\t\t= "))
nilai2 = int(input("Masukan Nilai 2\t\t= "))
nilai3 = int(input("Masukan Nilai 3\t\t= "))

min = 0
if nilai1 < nilai2 :
    min = nilai1
else :
    min = nilai2
if nilai3 < min :
    min = nilai3

print("Nilai Terkecil Adalah\t=", min)