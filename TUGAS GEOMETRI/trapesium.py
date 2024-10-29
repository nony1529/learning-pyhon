print("================================================")
print("Menghitung Luas dan Keliling Trapesium Siku-Siku")
print("================================================")

luas = int(input('Masukan nilai luas\t\t\t= '))
keliling = int(input('Masukan nilai keliling\t\t\t= '))
sisi1 = int(input('Masukan nilai sisi1\t\t\t= '))
sisi2 =int(input('Masukan nilai sisi2\t\t\t= '))
tinggi =int(input('Masukan nilai tinggi\t\t\t= '))
ab =int(input('Masukan nilai ab\t\t\t= '))
bc =int(input('Masukan nilai bc\t\t\t= '))
cd =int(input('Masukan nilai cd\t\t\t= '))
da =int(input('Masukan nilai da\t\t\t= '))

luas = 1/2*(sisi1+sisi2)*tinggi
keliling = ab+bc+cd+da

print('Luas trapesium siku siku adalah\t\t=',luas)
print('Keliling trapesium siku siku adalah\t=',keliling)