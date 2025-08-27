def saludar(nombre):
    return nombre

usuario = input("Ingresa tu nombre: ").capitalize()
saludo = saludar(usuario)
print(f"Bienvenido {saludo} a Programación 1")