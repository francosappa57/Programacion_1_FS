print("Bienvenido al Parque de Diversiones PythonLand!!")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print("\n-Atracciones-\n"+
      ". Montaña Rusa $1500\n"+
      ". Casa del Terror $1200\n"+
      ". Carrusel $800"
)

pago_total = 0
lista_atracciones = ""
atracciones_permitidas = ""

while True:
    atraccion = input("Ingrese la atraccion: ").lower()
    match atraccion:
        case "montaña rusa":
                lista_atracciones += "Montaña Rusa, "
                if edad >= 12:
                    print("Puede subir")
                    pago_total += 1500
                    atracciones_permitidas += "Montaña rusa, "
                else:
                    print("No se admiten menores de 12 años")
        case "casa del terror":
                lista_atracciones += "Casa del terror, "
                if edad > 6:
                    print("Puede subir")
                    pago_total += 1200
                    atracciones_permitidas += "Casa del terror, "
                else:
                    print("No se admiten menores de 6 años")
        case "carrusel":
                lista_atracciones += "Carrusel, "
                print("Puede subir")
                pago_total += 800
                atracciones_permitidas += "Carrusel, "
        case _:
                print("Atraccion inexistente")
    
    pregunta = input("Queres subirte a otra atraccion? ").lower()
    if pregunta == "si":
          continue
    else:
          break

print(f"\n-Resumen-\n"
      f"Nombre: {(nombre).capitalize()}\n"
      f"Atracciones Elegidas: {lista_atracciones}\n"
      f"Atracciones Permitidas: {atracciones_permitidas}\n"
      f"Total a pagar: ${pago_total}"
)