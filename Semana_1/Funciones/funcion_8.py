def calcular_edad(anio_nacimiento):
    return 2025 - anio_nacimiento

anio = int(input("Ingresa tu año de nacimiento: "))
edad = calcular_edad(anio)

print(f"Tenes {edad} años")
