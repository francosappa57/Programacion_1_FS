estudiante = ("Franco", "Sappa", (6.5, 9.0, 3.5))
nombre, apellido, notas = estudiante

suma = 0
for i in notas:
    suma += i
promedio = suma / len(notas)

print(f"\n--- Estudiante ---")
print(f"Nombre completo: {nombre} {apellido}\n"
      f"Promedio: {promedio:.2f}\n")
