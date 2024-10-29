print("=" * 45)
print("\tMenentukan Lampu Lalu Lintas")
print("=" * 45)

kondisi1 = input("Kondisi Lampu\t\t= ").lower()
kondisi2 = input("Warna Lampu\t\t= ").lower()

status =''
if kondisi1 == "menyala":
    if kondisi2 == "merah":
        status = "berhenti"
    elif kondisi2 == "kuning":
        status = "bersiap"
    elif kondisi2 == "hijau":
        status = "maju"
    else :
        print ("Jalan Tidak Beraturan")

print("Status Lampu\t\t=", status)