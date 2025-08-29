import gestion_parque.parque as gp

print("Bienvenido al Parque de Diversiones PythonLand!!")
nombre = input("Ingresa tu nombre: ").capitalize()
edad = int(input("Ingresa tu edad: "))
cantidad = int(input("A cuantas atracciones te vas a subir? "))
atracciones_elegidas = ""
atracciones_permitidas = ""
contador = 0
pago_total = 0

while contador < cantidad:
    gp.mostrar_atracciones()
    atraccion = input("Ingrese la atraccion: ").lower()
    if atraccion != "montaña rusa" and atraccion != "carrusel" and atraccion != "casa del terror":
        print("Atraccion inexistente")
        pass
    else:
        atracciones_elegidas += atraccion.capitalize()
        if gp.puede_subir(edad, atraccion) == True:
            print("Puede subir")
            pago_total += gp.calcular_precio(atraccion)
            atracciones_permitidas += atraccion.capitalize()
        else:
            print("No tiene edad suficiente para subir")
        contador += 1
            
descuento = gp.descuento(cantidad, pago_total)
pago_total -= descuento
resumen = gp.registrar_visita(nombre, edad, atracciones_elegidas, atracciones_permitidas, pago_total)
gp.mostrar_resumen(resumen)



    