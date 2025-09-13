numero = int(input("Ingresa un numero entero: "))
siguiente = 1
anterior = 0

print(f"\t---Secuencia Fibonacci de {numero} terminos---")
for x in range(numero):
    if x == 0:
        print(anterior, end=" ")
    elif x == 1:
        print(siguiente, end=" ")
    else:
        secuencia = siguiente + anterior
        print(secuencia, end=" ")
        anterior = siguiente
        siguiente = secuencia
