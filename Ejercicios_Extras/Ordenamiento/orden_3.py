numeros = [-12, 9, 34, 1, -45, -3, 8, -666]

def mostrar_array(vector):
    for i in range(len(vector)):
        intercambio = False
        for j in range(len(vector) -i -1):
            if vector[j] < 0:
                if vector[j + 1] < 0:
                    if vector[j] < vector[j + 1]:
                        vector[j], vector[j + 1] = vector[j + 1], vector[j]
                        intercambio = True
            else: 
                if vector[j] > vector[j + 1]:
                    vector[j], vector[j + 1] = vector[j + 1], vector[j]
                    intercambio = True
        if intercambio == False:
            break

print(f"Antes\n {numeros}")
mostrar_array(numeros)
print(f"Despues\n {numeros}")