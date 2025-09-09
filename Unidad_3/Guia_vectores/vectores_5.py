# Buscar un valor

vec_enteros = [5, 6, 12, 87, 154, 32, 10, 27, 9, 0]
usuario = int(input("Ingresa un numero entero: "))

for x in range(len(vec_enteros)):
    if usuario == vec_enteros[x]:
        print(f"El numero {usuario} se encuentra en el indice {x}")
        break

    if x == len(vec_enteros) - 1:
        print("No se encuentra el numero solicitado")

