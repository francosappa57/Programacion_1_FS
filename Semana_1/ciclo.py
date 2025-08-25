print("Bienvenido al Parque de Diversiones PythonLand!!")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
cantidad = int(input("A cuantas atracciones te vas a subir? "))

pago_total = 0
contador = 1
atracciones_elegidas = ""
atracciones_permitidas = ""

while contador <= cantidad:
    print("\n-Atracciones-\n"+
        ". Montaña Rusa $1500\n"+
        ". Casa del Terror $1200\n"+
        ". Carrusel $800")
    
    atraccion = input("Ingrese la atraccion: ").lower()
    match atraccion:
        case "montaña rusa":
                atracciones_elegidas += "Montaña Rusa, "
                contador += 1
                if edad >= 12:
                    print("Puede subir")
                    pago_total += 1500
                    atracciones_permitidas += "Montaña rusa, "
                else:
                    print("No se admiten menores de 12 años")
        case "casa del terror":
                atracciones_elegidas += "Casa del terror, "
                contador += 1
                if edad > 6:
                    print("Puede subir")
                    pago_total += 1200
                    atracciones_permitidas += "Casa del terror, "
                else:
                    print("No se admiten menores de 6 años")
        case "carrusel":
                atracciones_elegidas += "Carrusel, "
                contador += 1
                print("Puede subir")
                pago_total += 800
                atracciones_permitidas += "Carrusel, "
        case _:
                print("Atraccion inexistente. Intente nuevamente")

print(f"\n-Resumen-\n"
      f"Nombre: {(nombre).capitalize()}\n"
      f"Atracciones Elegidas: {atracciones_elegidas}\n"
      f"Atracciones Permitidas: {atracciones_permitidas}\n"
      f"Total a pagar: ${pago_total}"
)