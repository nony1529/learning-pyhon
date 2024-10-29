#Menghitung Luas dan Keliling Trapesium Siku Siku
print("=" * 50)
print("\tMerubah Program ke Function dan Lambda")
print("=" * 50)

def trapesium() :
    sisi1 = int(input("Masukan nilai sisi 1\t\t\t= "))
    sisi2 = int(input("Masukan nilai sisi 2\t\t\t= "))
    tinggi = int(input("Masukan nilai tinggi\t\t\t= "))
    ab = int(input("Masukan nilai ab\t\t\t= "))
    bc = int(input("Masukan nilai bc\t\t\t= "))
    cd = int(input("Masukan nilai cd\t\t\t= "))
    da = int(input("Masukan nilai da\t\t\t= "))
    luas = lambda s1,s2,t : 1/2 * (s1+s2) * t
    keliling = lambda ab,bc,cd,da : ab + bc + cd + da

    print("Nilai Luas Trapesium Siku Siku adalah\t\t= ", luas(sisi1,sisi2,tinggi), "cm")
    print("Nilai Keliling Trapesium Siku Siku adalah\t= ", keliling(ab,bc,cd,da), "cm")

trapesium()
trapesium()
trapesium()
trapesium()