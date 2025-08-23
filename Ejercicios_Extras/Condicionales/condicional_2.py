# Mostrar un mensaje especifico en base la nota introducida por el usuario

nota = float(input("Ingresa tu nota: "))

if nota < 4 and nota > 0:
    print(f"Desaprobado. Tu nota es {nota}")
elif nota < 6:
    print(f"Aprobado. Tu nota es {nota}")
elif nota <= 10:
    print(f"Promocion directa. Tu nota es {nota}")
else:
    print("Nota incorrecta. Las notas son del 1 al 10")