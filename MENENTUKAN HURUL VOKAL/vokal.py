print("=" * 50)
print("\t\tMenentukan Huruf Vokal")
print("=" * 50)

teks = input("Masukan Kalimat\t\t\t\t= ")
jumlah = len(teks)
jumlah_vokal = 0
huruf_vokal = ''

for i in teks:
    if i in 'aiueo':
        jumlah_vokal += 1
        huruf_vokal = huruf_vokal + i + ' '

print("Jumlah Karakter\t\t\t\t= ", jumlah)
print("Jumlah Huruf Vokal\t\t\t= ", jumlah_vokal)
print("Huruf Vokal Yang Terdapat Pada Teks\t= ", huruf_vokal)