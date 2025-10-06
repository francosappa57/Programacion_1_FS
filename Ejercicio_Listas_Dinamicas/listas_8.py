import funciones_listas as fl
estudiante = ["Franco", "Sappa", 39760175]

nuevo = fl.cargar_nuevo_estudiante()
estudiante.extend(nuevo)
print("\n--- Actualizacion lista de estudiantes ---")
print(estudiante)