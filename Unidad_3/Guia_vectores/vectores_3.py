# Promedio de valores

vec_decimales = [2.3, 4.5, 1.3, 86.4, 9.74, 7.25]
suma = 0

for x in range(len(vec_decimales)):
    suma += vec_decimales[x]

promedio = suma / len(vec_decimales)
print(f"El promedio es {promedio:.2f}")