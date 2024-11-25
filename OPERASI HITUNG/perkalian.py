print("=" * 50)
print("\tMembuat Tabel Perkalian Hingga 100")
print("=" * 50)

angka = int(input("Masukan Perkalian Yang Diingkan = "))

for i in range (1, 101):
    print(angka, "x", i, "=", angka * i)