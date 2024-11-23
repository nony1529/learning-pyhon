nilai = 5
pemisah = nilai - 1
for i in range (0, nilai):
    for d in range (0, pemisah):
        print("", end = " ")
    for f in range (0, i + 1):
        print("*", end = " ")
    pemisah = pemisah - 1
    print()
pemisah = 1
for i in range(nilai -1, 0, -1):
    for d in range (0, pemisah):
        print("", end = " ")
    for f in range (0, i):
        print("*", end = " ")
    pemisah = pemisah + 1
    print()