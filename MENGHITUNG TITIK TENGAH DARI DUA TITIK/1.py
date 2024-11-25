print("=" * 54)
print("\tMenghitung Titik Tengah Dari Dua Titik")
print("=" * 54)

class titik:
    x = 0.0
    y = 0.0

titik1 = titik() 
titik2 = titik()
titik3 = titik()

x1 = input("Masukan Nilai Dari Titik Ke 1 (x) = ")
y1 = input("Masukan Nilai Dari Titik Ke 1 (y) = ")
titik1.x = float(x1)
titik1.y = float(y1)

x2 = input("Masukan Nilai Dari Titik Ke 2 (x) = ")
y2 = input("Masukan Nilai Dari Titik Ke 2 (y) = ")
titik2.x = float()
titik2.y = float()

titik3.x = (titik1.x + titik2.x)/2
titik3.y = (titik1.y + titik2.y)/2

print("Nilai Titik Tengah Nya (x)\t  =",titik3.x)
print("Nilai Titik Tengah Nya (y)\t  =",titik3.y)