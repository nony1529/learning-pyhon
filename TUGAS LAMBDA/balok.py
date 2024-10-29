#Menghitung Luas Permukaan dan Volume Balok
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def balok() :
    panjang = int(input("Masukan nilai panjang\t= "))
    lebar = int(input("Masukan nilai lebar\t= "))
    tinggi = int(input("Masukan nilai tinggi\t= "))
    volume = lambda p,l,t: p * l * t
    luas = lambda p,l,t: 2 * p * l + p * t + l * t

    print("Volume balok adalah\t\t= ", volume(panjang,lebar,tinggi), " cm3")
    print("Luas Permukaan balok adalah\t= ", luas(panjang,lebar,tinggi), " cm3")

balok()
balok()
balok()
balok()