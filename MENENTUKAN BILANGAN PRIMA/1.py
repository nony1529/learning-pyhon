print("=" * 45)
print("\tMenentukan Bilangan Prima")
print("=" * 45)
print()

angka1 = int(input("Masukan Angka 1 (Kurang Dari Angka 2)   = "))
angka2 = int(input("Masukan Angka 2 (Lebih Dari Angka 1)    = "))

print("Bilangan Prima Antara",angka1, "dan",angka2, "Adalah = ")

for i in range (angka1, angka2 + 1):
    if i > 1:
        for n in range(2, i):
            if(i % n ) == 0:
                break
        else:
            print(i)