print("=" * 67)
print("\tProgram Menghitung Sn Dan Un Dari Barisan Geometri")
print("=" * 67)

def geometri(n, a, r):
    un = a * (r ** (n -1))

    if (r == 1):
        sn = n * a
    else :
        sn = a * ((r ** n) - 1) / (r - 1)

    print("Suku Ke-{} (Un)\t\t\t= {}".format(n, un))
    print("Jumlah {} Suku Pertama (Sn)\t= {}".format(n, sn))
    return

def main():
    n = int(input("Suku Berapa Yang Akan Dicari\t= "))
    a = int(input("Dimulai Dari\t\t\t= "))
    r = int(input("Berapa Rasio/Selisih Antar Suku\t= "))

    geometri(n, a, r)

main()