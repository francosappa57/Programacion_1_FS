numero = int(input("Ingresa un numero: "))

for x in range(1, numero + 1):
    if x == 1:
        pass
    else:
        print("")
    for j in range (1, x + 1):
        print(j, end=" ")
