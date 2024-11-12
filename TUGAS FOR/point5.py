angka = 0
for deret in range(1,6) :
    if deret < 5 :
        print(deret, end = " + ")
    else:    
        print (deret, end= " = ")
    angka = angka + (deret)

print (angka)