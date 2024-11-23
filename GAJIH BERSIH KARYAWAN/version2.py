print("=" * 45)
print("\t\tMenghitung Upah Per Jam")
print("=" * 45)


def total_upah(jam_kerja, upah_per+jam):
    upah = jam_kerja * upah_per+jam
    return upah

jam_kerja = float(input("Masukkan jumlah jam kerja: "))
upah_per+jam = float(input("Masukkan tarif per jam: "))

total_upah = total_upah(jam_kerja, upah_per+jam)
print(f"Total upah buruh kerja adalah: {total_upah}")