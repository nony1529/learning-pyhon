print("=" * 50)
print("\tMenentukan Nilai Terbesar Dan Terkecil")
print("=" * 50)

nilai1 = int(input("Masukan Nilai 1\t\t\t= "))
nilai2 = int(input("Masukan Nilai 2\t\t\t= "))
nilai3 = int(input("Masukan Nilai 3\t\t\t= "))

#Mencari Maksimal
maks = 0
if nilai1 > nilai2 :
    maks = nilai1
else :
    maks = nilai2
if nilai3 > maks :
    maks = nilai3

#Mencari Minimal
min = 0
if nilai1 < nilai2 :
    min = nilai1
else :
    min = nilai2
if nilai3 < maks :
    min = nilai3

print("Nilai Terbesar Nya Adalah\t=", maks)
print("Nilai Terkecil Nya Adalah\t=", min)