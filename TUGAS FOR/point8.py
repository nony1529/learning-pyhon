nilai = 0
for angka in range (2, 12, 2) :
    if angka < 10 :
        print(angka, end = " + ")
    else :
        print(angka, end = " = ")
    nilai = nilai + (angka)
print (nilai)