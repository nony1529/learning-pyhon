print("=" * 79)
print("\tKonversi Panjang Sebuah Benda Dari Meter Ke Inch, Kaki, Dan Yard")
print("=" * 79)

def panjang_meter(meter):

  inci = meter * 39.3701
  kaki = meter * 3.28084
  yard = meter * 1.09361

  return {
    "inci": inci,
    "kaki": kaki,
    "yard": yard
  }

# Inputan
meter = float(input("Masukkan Panjang Dalam Meter = "))

#Rumus
hasil_konversi = panjang_meter(meter)

# Menampilkan hasil konversi
print("***Hasil konversi***")
print("Nilai Dalam Satuan Inch = ", hasil_konversi["inci"])
print("Nilai Dalam Satuan Kaki =", hasil_konversi["kaki"])
print("Nilai Dalam Satuan Yard =", hasil_konversi["yard"])
