print("=" * 68)
print("\tMenentukan Jenis Segitiga Berdasarkan Sudut Dan Sisi")
print("=" * 68)

#Menentukan Berdasarkan Sisi Nya
def main():
    a = int(input("Masukan Panjang Sisi 1\t\t\t\t= "))
    b = int(input("Masukan Panjang Sisi 2\t\t\t\t= "))
    c = int(input("Masukan Panjang Sisi 3\t\t\t\t= "))

    if (a > c):
        a, c = c, a
    if (b > c):
        b, c = c, b

    if (c >= a + b):
        print("Ketiga Nilai Sisi Ini Tidak Membentuk Jenis Segitiga Apapun")
    elif (c * c == (a * a + b * b)):
        print("Ketiga Nilai Sisi Ini Merupakan Triple Pythagoras Dan Membentuk Segitiga SIku-Siku")
    else:
        if (a == b == c):
            jenis_sisi = "Segitiga Sama Sisi"
        elif (a == b or b == c or a == c):
            jenis_sisi = "Segitiga Sama Kaki"
        else:
            jenis_sisi = "Segitiga Sembarang"
        print("Berdasarkan Sisinya, Segitiga Ini Merupakan Jenis\t\t   =",jenis_sisi)


#Menentukan Berdasarkan Sudut Nya
        if (c * c > (a * a + b * b)):
            jenis_sudut = "Sudut Tumpul"
        else:
            jenis_sudut = "Sudut Lancip"
        print("Berdasarkan Sudutnya, Segitiga Ini Merupakan Segitiga Dengan Jenis =",jenis_sudut)

main()