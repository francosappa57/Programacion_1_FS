import funciones_definidas.funcion as ff

cantidad = ff.pedir_cantidad()
vector = ff.agregar_numeros(cantidad)
promedio = ff.promedio_vec_positivos(vector)

print(f"El promedio de numeros positivos en {vector} es {promedio:.2f}")