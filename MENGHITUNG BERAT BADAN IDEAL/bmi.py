print("=" * 40)
print("\tBoddy Mass Index (BMI)")
print("=" * 40)

tinggi = float(input("Masukan Tinggi Badan\t= "))
berat = float(input("Masukan Berat Badan\t= "))

tinggi = tinggi / 100
bmi = berat / (tinggi**2)

if bmi < 18.5:
    status = "Berat Badan Kurang"
elif bmi >= 18.5 and bmi <= 22.9:
    status = "Berat Badan Normal"
elif bmi >= 23 and bmi <= 24.9:
    status = "Berat Badan Kelebihan"
elif bmi >= 25 and bmi <= 29.9:
    status = "Obesitas Tingkat 1"
elif bmi > 30:
    status = "Obesitas Tingkat 2"

print(f"Boddy Mass Index\t= {bmi}\nStatus\t\t\t= {status}")