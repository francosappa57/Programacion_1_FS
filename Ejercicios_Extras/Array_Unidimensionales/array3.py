import funciones_definidas.funcion as ff

cantidad = ff.pedir_cantidad()
vector = ff.agregar_numeros(cantidad)
promedio = ff.promedio_vec(vector)

print(f"El promedio de {vector} es {promedio}")
