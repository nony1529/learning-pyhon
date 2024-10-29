print('==========================================')
print('Menghitung Luas dan Keliling Layang-Layang')
print("==========================================")

diagonal1 =int(input("Masukan nilai diagonal1\t\t= "))
diagonal2 =int(input("Masukan nilai diagonal2\t\t= "))
sisi1 =int(input('Masukan nilai sisi1 \t\t= ')) 
sisi2 =int(input('Masukan nilai sisi2 \t\t= ')) 

luas = 1/2*(diagonal1*diagonal2)
keliling = 2*(sisi1+sisi2)

print('Luas layang-layang adalah\t=',luas)
print('Keliling layang-layang adalah\t=',keliling)