# Comparar dos arrays

numeros_1 = [63, 4, 98, 2, 27]
numeros_2 = [0, 4, 5, 2, 27]

for x in range(len(numeros_1)):
    if numeros_1[x] == numeros_2[x]:
        print(f"Elemento {x + 1}: Son el mismo elemento")
    else:
        print(f"Elemento {x + 1}: Son diferentes elementos")