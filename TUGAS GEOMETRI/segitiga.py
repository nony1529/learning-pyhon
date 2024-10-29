print('=================================')
print("Hitung Luas dan Keliling Segitiga")
print('=================================')

luas = int(input('Masukan nilai luas \t\t= '))
keliling = int(input('Masukan nilai keliling \t\t= '))
alas = int(input('Masukan nilai alas segitiga \t= '))
tinggi = int(input('Masukan nilai tinggi \t\t= '))
sisi1 = int(input('Masukan nilai sisi1 \t\t= '))
sisi2 = int(input('Masukan nilai sisi2 \t\t= '))
sisi3 = int(input('Masukan nilai sisi3 \t\t= '))

keliling = (sisi1+sisi2+sisi3)
luas = 1/2*alas*tinggi

print("Keliling segitiga adalah \t=",keliling)
print("Luas segitiga adalah \t\t=",luas)