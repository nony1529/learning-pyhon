print("=" * 65)
print("\tMenentukan Bilangan Positif/Negatif/Nol")
print("=" * 65)

angka = float(input("Masukan Angka\t= "))

if angka > 0:
    print("Status Angka\t= Positif ")
elif angka == 0:
    print("Angka Ini Bernilai = 0")
else:
    print("Status Angka\t= Negatif")