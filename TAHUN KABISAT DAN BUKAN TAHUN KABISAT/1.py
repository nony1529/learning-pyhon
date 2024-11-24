print("=" * 67)
print("\t\tMenentukan Tahun Kabisat Dan Bukan Kabisat")
print("=" * 67)

tahun = int(input("Masukan Tahun\t= "))

if (tahun % 400 == 0):
    print(tahun, "\t\t= Adalah Tahun Kabisat")
elif (tahun % 100 == 0):
    print(tahun, "\t\t= Bukan Tahun Kabisat")
elif (tahun % 4 == 0):
    print(tahun, "\t\t= Adalah Tahun Kabisat")
else:
    print(tahun, "\t\t= Bukan Tahun Kabisat")