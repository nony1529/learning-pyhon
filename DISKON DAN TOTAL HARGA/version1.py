print("================================================")
print('\tMenghitung Diskon Dan Total Harga')
print("================================================")

harga =int(input("Masukan Harga Pembelian\t\t=  " ))

if harga >= 100000:
   A = harga * 5/100
   print("Kamu mendapatkan Diskon\t\t= ", int(A))
   B = harga-A
   print("Jumlah Yang Harus Di Bayar\t= ", int(B))
else:
   A = harga * 0
   print("Kamu Tidak Mendapatkan Diskon\t= ", int(A))
   B = harga-A
   print("Jumlah Yang Harus Di Bayar\t= ", int(B)) 