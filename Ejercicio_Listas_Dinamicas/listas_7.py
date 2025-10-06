import funciones_listas as fl
estudiante = ["Franco", "Sappa", 39760175]

lista_notas = fl.agregar_notas()
estudiante.append(lista_notas)
print("\n--- Informacion del estudiante ---")
print(estudiante)

fl.agregar_nueva_nota(estudiante)
print("\n--- Informacion actualizada del estudiante ---")
print(estudiante)