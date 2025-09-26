import funciones_definidas.funcion as ff

vector = ff.agregar_nombres(ff.pedir_cantidad())

vec_viejo = [0] * len(vector)
vec_nuevo = [0] * len(vector)

for i in range(len(vector)):
    viejo = input("Ingresa nombre a buscar: ")
    nuevo = input("Ingresa nombre a reemplazar: ")
    vec_viejo[i] = viejo
    vec_nuevo[i] = nuevo
    opcion = input("Queres cambiar otro nombre? (s/n) ").lower()
    if opcion == "n":
        break

total = ff.reemplazar_nombre(vector, vec_viejo, vec_nuevo)
print(f"Total de reemplazos realizados: {total}")


