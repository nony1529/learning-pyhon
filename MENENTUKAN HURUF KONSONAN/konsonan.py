print("=" * 55)
print("\t\tMenentukan Huruf Konsonan")
print("=" * 55)

teks = input("Masukan Kalimat\t\t\t\t= ")
jumlah = len(teks)
jumlah_konsonan = 0
huruf_konsonan = ''

for i in teks:
    if i not in "aiueo":
        jumlah_konsonan += 1
        huruf_konsonan = huruf_konsonan + i + " "

print("Jumlah Karakter\t\t\t\t= ", jumlah)
print("Jumlah Huruf konsonan\t\t\t= ", jumlah_konsonan)
print("Huruf konsonan Yang Terdapat Pada Teks\t= ", huruf_konsonan)