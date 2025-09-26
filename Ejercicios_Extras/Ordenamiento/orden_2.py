num_1 = [1, 3, 5, 7, 9]
num_2 = [-5, -1, 4, 8, 12]

def intercalar_vectores(vector_1, vector_2, opcional = False):
    total = len(vector_1) + len(vector_2)
    vector_ordenado = [0] * total
    contador = 0
    for i in range(len(vector_ordenado)):
        if i < 5:
            vector_ordenado[i] = vector_1[contador]
        elif i == 5:
            contador = 0
            vector_ordenado[i] = vector_2[contador]
        else:
            vector_ordenado[i] = vector_2[contador]
        contador += 1
    print(f"Antes {vector_ordenado}")
    
    for j in range(len(vector_ordenado)):
        intercambio = False
        for x in range(len(vector_ordenado) -j -1):
            if opcional == False:
                if vector_ordenado[x] > vector_ordenado[x + 1]:
                    vector_ordenado[x], vector_ordenado[x + 1] = vector_ordenado[x + 1], vector_ordenado[x]
                    intercambio = True
            else:
                if vector_ordenado[x] < vector_ordenado[x + 1]:
                    vector_ordenado[x], vector_ordenado[x + 1] = vector_ordenado[x + 1], vector_ordenado[x]
                    intercambio = True
        if intercambio == False:
            break 
    print(f"Despues {vector_ordenado}")

intercalar_vectores(num_1, num_2)
