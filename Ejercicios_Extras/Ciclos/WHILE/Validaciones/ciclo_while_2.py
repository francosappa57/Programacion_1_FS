intentos = 3

while intentos > 0:
    clave = input("Ingresa una clave: ")
    if clave == "Programacion 1":
        print("Acceso concedido")
        break
    else:
        intentos -= 1
        print(f"Acceso denegado. Intentos restantes: {intentos}")

if intentos == 0:
    print("Cuenta bloqueda")
else:
    print("Bienvenido")