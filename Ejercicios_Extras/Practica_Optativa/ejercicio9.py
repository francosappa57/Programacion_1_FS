numero = int(input("Ingresa un numero entero: "))
siguiente = 0
anterior = 1

print(f"\t---Secuencia Fibonacci de {numero} terminos---")
for x in range(numero):
    siguiente = x
    anterior -= x
    print(siguiente + anterior, end=" ")
    
