print("=" * 40)
print("\tSensus Usia")
print("=" * 40)


kelompok_usia = {
    "0-18": 0,
    "19-30": 0,
    "31-50": 0,
    "51+": 0
}

def kategori_usia(usia):
    if usia <= 18:
        return "0-18"
    elif usia <= 30:
        return "19-30"
    elif usia <= 50:
        return "31-50"
    else:
        return "51+"

jumlah_orang = int(input("Masukan Jumlah Individu Yang Akan Di Input = "))

for i in range(jumlah_orang):
    usia = int(input(f"Masukan Usia Individu {i+1}= "))
    kelompok = kategori_usia(usia)
    kelompok_usia[kelompok] += 1

print("Kelompok Usia = ")
for kelompok, hitung in kelompok_usia.items():
    print(f"{kelompok}: {hitung} individu")
