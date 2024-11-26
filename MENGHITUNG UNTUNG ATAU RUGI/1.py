print("=" * 54)
print("\tMenentukan Presentasi Untung Atau Rugi")
print("=" * 54)

def main():
    beli = int(input("Berapa Jumlah Harga Yang Dibeli = "))
    jual = int(input("Berapa Jumlah Harga Jualnya\t= "))

    if (jual == beli):
        print("Harga Jual Sama Dengan Harga Beli")
        print("Tidak Ada Kerugian Maupun Keuntungan")
    elif (jual > beli):
        hasil = "untung"
    else:
        hasil = "rugi"

    selisih = abs(jual - beli)

    persen = selisih / beli * 100

    print("Mendapatkan Ke{}an Sebesar\t= {}%".format(hasil, persen))

main()