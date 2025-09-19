import funciones_definidas.funcion as ff

def posiciones(vec):
    lista = [0] * len(vec)
    maximo = None
    indice = None
    for x in range(len(vec)):
        if x == 0:
            maximo = vec[x]
            indice = x
            lista[indice] = x
        elif vec[x] > maximo:
            maximo = vec[x]
            indice = 0
            lista[indice] = x
        elif vec[x] == maximo:
            lista[indice] = x
        indice += 1
    return lista

vector = ff.agregar_numeros()
maximo = posiciones(vector)
print(f"Valor maximo en la lista {vector}")
for i in maximo:
    if i != 0:
        print(f"Index {i}", end=", ")
