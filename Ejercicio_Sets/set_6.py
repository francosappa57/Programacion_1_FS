tareas_hoy = {"estudiar", "cocinar", "lavar", "jugar", "descansar"}
tareas_listas = {"estudiar", "jugar"}

faltantes = tareas_hoy.difference(tareas_listas)

print("\n--- Tareas faltantes a realizar ---")
print(f"{faltantes}\n")