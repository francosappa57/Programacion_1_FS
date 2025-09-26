def agregar_numeros(num=5):
    vec_numeros = [0] * num
    for x in range(len(vec_numeros)):
        validar = False
        while validar == False:
            solicitar_num = int(input("Ingresar numero entero: "))
            if solicitar_num == 0:
                print("Solo entero mayores a 0")
            else:
                vec_numeros[x] = solicitar_num
                validar = True
    return vec_numeros


def agregar_nombres(num=5):
    vec = [0] * num
    for x in range(len(vec)):
        solicitar_name = input("Ingresar un nombre: ")
        vec[x] = solicitar_name
    return vec
    

def pedir_cantidad():
    cantidad = int(input("Cuantos elementos queres en la lista? "))
    return cantidad


def promedio_vec(vec):
    suma = 0
    for x in range(len(vec)):
        suma += vec[x] 
    promedio = suma / len(vec)
    return promedio
    

def promedio_vec_positivos(vec):
    suma = 0
    positivos = 0
    for x in range(len(vec)):
        if vec[x] >= 0:
            suma += vec[x]
            positivos += 1
    promedio = suma / positivos
    return promedio


def producto_vec(vec):
    producto = 1
    for x in range(len(vec)):
        producto *= vec[x]  
    return producto


def posicion_valor_max(vec):
    maximo = 0
    posicion = None
    for x in range(len(vec)):
        if vec[x] > maximo:
            maximo = vec[x]
            posicion = x
    return posicion


def posiciones(vec):
    num_mayor = 0
    for i in range(len(vec)):
        if vec[i] >= num_mayor:
            num_mayor = vec[i]
    print(f"Numero mayor - {num_mayor}")
    for x in range(len(vec)):
        if num_mayor == vec[x]:
            print(f"Posicion - index {x}")
 

def reemplazar_nombre(lista_nombres, nombre_antiguo, nombre_nuevo):
    reemplazo = 0
    for x in range(len(lista_nombres)):
        for j in range(len(nombre_antiguo)):
            if lista_nombres[x] == nombre_antiguo[j]:
                lista_nombres[x] = nombre_nuevo[j]
                reemplazo += 1
    return reemplazo


def interseccion_vectores(lista1, lista2):
    print(f"Interseccion entre {lista1} y {lista2}")
    for i in range(len(lista1)):
        for j in range(len(lista2)):
            if lista1[i] == lista2[j]:
                print(lista2[j], end=" ")


def union_vectores(lista1, lista2):
    union = len(lista1) + len(lista2)
    vec_union = [0] * union 
    contador = 0
    print(f"Union entre {lista1} y {lista2}")
    for i in range(union):
        if i < len(lista1):
            vec_union[i] = lista1[contador]
        else:
            if i == len(lista1):
                contador = 0
            vec_union[i] = lista2[contador]
        contador += 1
    print(vec_union)


def diferencia_vectores(lista1, lista2):
    print(f"Diferencias entre {lista1} y {lista2}")
    for i in range(len(lista1)):
        diferente = True
        for j in lista2:
            if lista1[i] == j:
                diferente = False
        if diferente == True:
            print(lista1[i], end=" ")

    for i in range(len(lista2)):
        diferente = True
        for j in lista1:
            if lista2[i] == j:
                diferente = False
        if diferente == True:
            print(lista2[i], end=" ")     