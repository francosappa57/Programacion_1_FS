# Función para buscar la primera aparición de un valor

def buscar_numero(vector, numero):
    valor = None
    primero = 0
    for x in range(len(vector)):
        if numero == vector[x]:
            primero += 1
            if primero == 1:
                valor = x
    
    if valor == None:
        valor = -1
    return valor
                
enteros = [6, 8, 12, 34, 0, 29, 456, 12, 13, 1, 5, 1]
pedir_numero = int(input("Ingresa un numero: "))
resultado = buscar_numero(enteros, pedir_numero)

print(f"El numero se encuentra en la posicion {resultado}")
