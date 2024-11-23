nilai = 5

for i in range (0, nilai):
    for y in range (0, nilai - i - 1):
        print(" ", end="")
    for y in range(0, i + 1):
        print("*", end=" ")
    print()