print("======================================")
print('Hitung Luas Permukaan Dan Volume Balok')
print('======================================')

panjang = int(input('Masukan panjang balok\t\t= '))
lebar = int(input('Masukan lebar balok\t\t= '))
tinggi = int(input('Masukan tinggi balok\t\t= '))

volume =panjang*lebar*tinggi 
Luas_Permukaan =2*(panjang*lebar+panjang*tinggi+lebar*tinggi)

print('Volume balok adalah \t\t=',volume,'cm3')
print('Luas p ermukaan balok adalah \t=' , Luas_Permukaan, 'cm3') 