print("=" * 57)
print("\tMenghitung Diskon Dan Harga Sesudah Diskon")
print("=" * 57)

total = int(input("Masukan Harga Barang\t\t= Rp "))
setelah_diskon = total
 
if total < 100000:
    diskon = total * (5/100)
else:
    diskon = total * (10/100)
 
setelah_diskon = total - diskon

print("Total Diskon Nya Adalah\t\t= Rp {:,}".format(int(diskon)).replace(',','.'))
print("Total Harga Sesudah Diskon\t= Rp {:,}".format(int(setelah_diskon)).replace(',','.'))
