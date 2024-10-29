print("=" * 50)
print("\tMenentukan Nilai Terbesar")
print("=" * 50)

nilai1 = int(input("Masukan Nilai 1\t\t= "))
nilai2 = int(input("Masukan Nilai 2\t\t= "))
nilai3 = int(input("Masukan Nilai 3\t\t= "))

maks = 0
if nilai1 > nilai2:
    maks = nilai1
else :
    maks = nilai2
if nilai3 > maks :
        maks = nilai3

print("Nilai Terbesar Adalah\t=", maks)