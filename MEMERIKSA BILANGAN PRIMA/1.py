print("=" * 45)
print("\tMemeriksa Apakah Bilangan Prima")
print("=" * 45)

def cek_prima(n):
    prima = True
    if n < 2:
        prima = False

    for i in range (2, int(n ** 0.5) + 1):
        if(n % i == 0):
            prima = False 
    
    return prima

def main():
    angka = int(input("Masukan Bilangan = "))

    if cek_prima(angka):
        print(angka, "Adalah Bilangan Prima")
    else:
        print(angka, "Bukan Bilangan Prima")

main()