print("=" * 38)
print("\tMenghitung Deret Angka")
print("=" * 38)

def deret_angka():
    print()
    jumlah = int(input("Masukan Jumlah Deret\t\t= "))
    kelipatan = int(input("Masukan Kelipatan\t\t= "))
    print()

    for i in range(1, jumlah + 1):
        print(i * kelipatan, end = " ")
    print()

def main():
    print("Berapa Jumlah Deret Yang Akan Dibuat ")
    jml = input("Jumlah Deret\t\t\t= ")
    i = 0
    while i < int(jml):
        deret_angka()
        i = i + 1

if __name__=='__main__':
    main()