elementos = []

while True:
    usuario = int(input("Ingresa un numero (0 para terminar): "))
    if usuario == 0:
        break 
    elementos.append(usuario)

conj_elementos = set(elementos)

eliminar = int(input("\nIngresa numero a eliminar: "))
if eliminar in conj_elementos:
    conj_elementos.remove(eliminar)
else:
    conj_elementos.discard(eliminar)

print(conj_elementos)    