def hitung_jarak(v, t):
  s = v * t
  return s

# Input
kecepatan = float(input("Masukkan Kecepatan (KM/JAM) = "))
waktu = float(input("Masukkan Waktu Tempuh (JAM) = "))

# Rumus Hitung jarak
jarak = hitung_jarak(kecepatan, waktu)

# Tampilan
print("Jarak Yang Ditempuh Adalah  =", jarak, "km")
