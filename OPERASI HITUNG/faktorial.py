print("=" * 57)
print("\tMembuat Program Menghitung Faktorial")
print("=" * 57)

y, nilai, faktorial = 0, 0, 1
nilai = int(input("Masukan Nilai\t\t= "))

for y in range(1, nilai + 1):
    faktorial *= y

print("faktorial Nya Adalah\t=",faktorial)