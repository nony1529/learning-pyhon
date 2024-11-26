print("=" * 67)
print("\tProgram Menghitung Sn Dan Un Dari Barisan Aritmatika")
print("=" * 67)

def aritmatika(n, a, b):
    un = a +(n-1) * b;
    sn = (n / 2) * (2 * a + (n - 1) * b);

    print("Suku Ke-{} (Un)\t\t\t= {}".format(n,un));
    print("Jumlah {} Suku Pertama (Sn)\t= {}".format(n,sn));

    return

def main():
    n = int(input("Masukan Suku Yang Akan Di Cari  = "));
    a = int(input("Dimulai Dari\t\t\t= "))
    b = int(input("Berapa Beda Antar Suku\t\t= "))

    aritmatika (n, a, b);

main()