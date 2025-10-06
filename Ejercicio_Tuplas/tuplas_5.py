def datos_usuario():
    datos = []
    nombre = input("\nIngresa tu nombre: ").title()
    edad = int(input("Ingresa tu edad: "))
    pais = input("En que pais vivis? ").title()
    datos.append(nombre)
    datos.append(edad)
    datos.append(pais)
    tupla = tuple(datos)
    return tupla

info = datos_usuario()
print("\n--- Datos del Usuario ---")
print(info)