numero = [5, 12, 1, 8, -3]

def orden_array(vec, opcion = False):
    for i in range(len(vec)):
        intercambio = False
        for j in range(len(vec) -i -1):
            if opcion == False:
                if vec[j] > vec[j + 1]:
                    vec[j], vec[j + 1] = vec[j + 1], vec[j] 
                    intercambio = True
            else:
                if vec[j] < vec[j + 1]:
                    vec[j], vec[j + 1] = vec[j + 1], vec[j] 
                    intercambio = True
        if intercambio == False:
            break

print(f"Antes {numero}")
orden_array(numero)
print(f"Despues {numero}")