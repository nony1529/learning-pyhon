print("=" * 46)
print("\tMembuat Program Mencari FPB")
print("=" * 46)

def hitungFPB(a, b):
    while b !=0:
        a, b = b, a % b
    return a

def main():
    angka1 = int(input("Masukan Angka Pertama\t\t= "))
    angka2 = int(input("Masukan Angka Kedua\t\t= "))

    hasilFPB = hitungFPB(angka1, angka2)
    print("FPB dari", angka1, "Dan", angka2, "Adalah\t=",hasilFPB)

main()