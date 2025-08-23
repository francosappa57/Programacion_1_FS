# Determinar posicion de los jugadores de baloncesto en base a su altura

altura = int(input("Ingrese su altura en cm: "))

if altura < 160:
    posicion = "Base"
elif altura <= 179:
    posicion = "Escolta"
elif altura <= 199:
    posicion = "Alero"
else:
    posicion = "Pivot"

print(f"Tu posicion en el equipo es {posicion}")