print("Bienvenido al Parque de Diversiones PythoLand!!")
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print("\n-Atracciones-\n"+"Montaña Rusa $1500\n"+"Casa del Terror $1200\n"+"Carrusel $800")

cantidad_atracciones = int(input("A cuantas quiere subirse? "))
pago_total = 0
lista_atracciones = []
atracciones_permitidas = []

for i in range(cantidad_atracciones):
      atraccion = input("Ingrese la atraccion: ").capitalize()
      lista_atracciones.append(atraccion)
      match atraccion:
            case "Montaña rusa":
                  if edad >= 12:
                        print("Puede subir")
                        pago_total += 1500
                        atracciones_permitidas.append("Montaña rusa")
                  else:
                        print("No se admiten menores de 12 años")
            case "Casa del terror":
                  if edad > 6:
                        print("Puede subir")
                        pago_total += 1200
                        atracciones_permitidas.append("Casa del terror")
                  else:
                        print("No se admiten menores de 6 años")
            case _:
                  print("Puede subir")
                  pago_total += 800
                  atracciones_permitidas.append("Carrusel")

print(f"\n-Resumen-\n"
      f"Nombre: {nombre}\n"
      f"Atracciones Elegidas: {lista_atracciones}\n"
      f"Atracciones Permitidas: {atracciones_permitidas}\n"
      f"Total a pagar: {pago_total}"
)
