def numero_mayor(n1, n2, n3):
    return max(n1, n2, n3)

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa un segundo numero: "))
num3 = float(input("Ingresa un tercer numero: "))

maximo = numero_mayor(num1, num2, num3)
print(f"El mayor numero es {maximo}")