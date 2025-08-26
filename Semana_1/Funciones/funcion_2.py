def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multi = num1 * num2
    return suma, resta, multi

num1 = float(input("Ingresa un numero: "))
num2 = float(input("Ingresa otro numero: "))

resultado_suma, resultado_resta, resultado_multi = operaciones(num1, num2)

print(f"La suma de {num1} + {num2} = {resultado_suma}")
print(f"La resta de {num1} - {num2} = {resultado_resta}")
print(f"La multiplicacion de {num1} x {num2} = {resultado_multi}")


