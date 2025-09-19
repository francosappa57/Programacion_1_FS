def agregar_numeros(num=5):
    vec_numeros = [0] * num
    for x in range(len(vec_numeros)):
        solicitar_num = int(input("Ingresar numero entero: "))
        vec_numeros[x] = solicitar_num
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


# def posiciones(vec):
#     lista = [0] * len(vec)
#     maximo = None
#     indice = None
#     for x in range(len(vec)):
#         if x == 0:
#             maximo = vec[x]
#             indice = x
#             lista[indice] = x
#         elif vec[x] > maximo:
#             maximo = vec[x]
#             indice = 0
#             lista[indice] = x
#         elif vec[x] == maximo:
#             lista[indice] = x
#         indice += 1
#     return lista
 

def reemplazar_nombre(lista_nombres, nombre_antiguo, nombre_nuevo):
    reemplazo = 0
    for x in range(len(lista_nombres)):
        for j in range(len(nombre_antiguo)):
            if lista_nombres[x] == nombre_antiguo[j]:
                for v in nombre_nuevo:
                    pass
                    lista_nombres[x] = v
                
                reemplazo += 1
    return reemplazo