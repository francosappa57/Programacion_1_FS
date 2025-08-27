import funcion_primos.primos as fp

num = int(input("Ingresa un numero entero: "))
resultado = fp.calcular(num)

if resultado <= 1:
    print("El numero tiene que ser mayor a 1")
else:
    print(f"Cantidad de primos: {resultado}")

