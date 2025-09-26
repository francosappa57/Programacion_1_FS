def datos():
    vector = [0] * 10
    for x in range(len(vector)):
        validar = False
        while validar == False:
            dato = int(input("Ingresa numero entero: "))
            if dato > -1000 and dato < 1000:
                vector[x] = dato
                validar = True
            else:
                print("El numero tiene que estar entre -1000 y 1000")
    return vector


def sumar_pares(vector):
    sum_par = 0
    for x in range(len(vector)):
        if vector[x] %2 == 0:
            sum_par += vector[x]
    print(f"\nLa suma de numeros pares es {sum_par}")


def mostrar_todos(vector):
    print("\nNumeros ingresados")
    for x in range(len(vector)):
        print(vector[x], end=" ")


def mostrar_pares(vector):
    print("\nNumeros pares")
    for x in range(len(vector)):
        if vector[x] != 0:
            print(vector[x], end=" ")


def mostrar_num_indice_impar(vector):
    print("\nNumeros en indices impares")
    for x in range(len(vector)):
        if x %2 != 0:
            print(vector[x], end=" ")