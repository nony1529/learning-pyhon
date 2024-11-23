print("=" * 40)
print("\tSensus Usia")
print("=" * 40)

usia = [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
sensus_usia = {}

for u in usia:
    sensus_usia[u] = 0
    
# Input usia individu dari pengguna
while True:
    try:
        usia_input = int(input("Masukkan usia individu (atau ketik 'selesai' untuk mengakhiri): "))
    except ValueError:
        break
        
    if usia_input in sensus_usia:
        sensus_usia[usia_input] += 1

# Menampilkan hasil sensus usia
print("\nHasil Sensus Usia:")
for u in sensus_usia:
    print(f"Usia {u}: {sensus_usia[u]} orang")