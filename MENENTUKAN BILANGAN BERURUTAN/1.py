print("=" * 45)
print("\tMenentukan Bilangan Berurutan")
print("=" * 45)

def terkecil (n, jumlah):
    tengah = jumlah / n
    if (n % 2 == 1):
        jarak = (n-1) / 2
    else:
        jarak = (n/2)-0.5
    kecil = tengah - jarak
    return round(kecil)

def main():
    n = int(input("Berapa Banyak Bilangan Yang Ingin Dijumlah kan = "))
    jumlah = int(input("Jumlah\t\t\t\t\t       = "))

    isi = []
    kecil = terkecil(n, jumlah)
    for i in range (n):
        isi.append(kecil + i)

    print("Berikut Bilangannya\t\t\t       = ", isi)

main()