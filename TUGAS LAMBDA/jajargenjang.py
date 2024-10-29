#Menghitung Luas dan Keliling Jajar Genjang
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def genjang ():
    panjang = int(input("Masukan nilai panjang\t\t\t= "))
    sisi = int(input("Masukan nilai sisi\t\t\t= "))
    alas = int(input("Masukan nilai alas\t\t\t= "))
    tinggi = int(input("Masukan nilai tinggi\t\t\t= "))
    luas = lambda a,t : a * t
    keliling = lambda p,s : p*s

    print("Nilai Luas Jajar Genjang adalah\t\t\t= ", luas(alas,tinggi), "cm")
    print("Nilai Keliling Jajar Genjang adalah\t\t= ", keliling(panjang,sisi), "cm")

genjang()
genjang()
genjang()
genjang()