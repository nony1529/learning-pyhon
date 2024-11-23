print("=" * 45)
print("\t\tMenghitung Upah Per Jam")
print("=" * 45)

golongan = input("Masukan Golongan Pekerja\t\t= ")
jam = int(input("Masukan Total Jam Pekerja\t\t= "))

#menghitung upah bersih
if golongan.upper() == "A" :
    upah_per_jam = 4000
elif golongan.upper() == "B" :
    upah_per_jam = 4000
elif golongan.upper() == "C" :
    upah_per_jam = 4000
elif golongan.upper() == "D" :
    upah_per_jam = 4000

#konverensi upah per jam
total_upah1 = jam * upah_per_jam

#menghitung upah lembur
if jam - 24 > 0 :
    total_upah = total_upah1 + ((jam - 24)*4000)
    print("Hasil Upah Pekerja Lembur Adalah\t=", "Rp", total_upah)

print("Hasil Upah Bersih Pekerja Adalah\t=", "Rp", total_upah1)