#Menghitung Luas dan Keliling Persegi Panjang
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def persegi() :
    panjang = int(input("Masukan nilai panjang\t= "))
    lebar = int(input("Masukan nilai lebar\t= "))
    luas = lambda p,l: p * l
    keliling = lambda p,l: 2 * p + l

    print("Luas nya adalah\t\t\t= ", luas(panjang,lebar), ' cm2')
    print("Keliing nya adalah\t\t= ", keliling(panjang,lebar), 'cm2')

persegi()
persegi()
persegi()
persegi()