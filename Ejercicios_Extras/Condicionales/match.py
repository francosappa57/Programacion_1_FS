# Mostrar si se puedo (o no) viajar a un cierto destino segun la estacion del año

print("-Agencia de Viajes (solo lugares Argentinos)-")
lugar = input("Indique su destino de viaje: ").lower()
estacion = input("En que estacion del año quieres viajar? ").lower()

if estacion == "invierno":
    if lugar == "bariloche":
        print("Se viaja")
    else:
        print("No se viaja")
elif estacion == "verano":
    if lugar == "mar del plata" or lugar == "cataratas":
        print("Se viaja")
    else:
        print("No se viaja")
elif estacion == "otoño":
    print("Se viaja")
elif estacion == "primavera":
    if lugar == "bariloche":
        print("No se viaja")
    else:
        print("Se viaja")
else:
    print("Estacion incorrecta. Introduzca una nuevamente")



        