# Programa de facturacion de servicio de agua potable

cantidad_metros = int(input("Indique consumo por metro cubico (numeros enteros): "))

print("\n-Lugar-\n"+
      "1. Residencial\n"+
      "2. Comercial\n"+
      "3. Industrial"
    )
cliente = int(input("Elija una opcion: "))

precio_fijo = 7000
consumo_metro_cubico = cantidad_metros * 200
subtotal_sin_impuesto = precio_fijo + consumo_metro_cubico
bonificacion = 0
recargo = 0

match cliente:
    case 1:
        if cantidad_metros < 30:
            bonificacion += 10
        elif cantidad_metros > 80:
            recargo += 15
    case 2:
        if cantidad_metros > 300:
            bonificacion += 12
        elif cantidad_metros > 150:
            bonificacion += 8
        elif cantidad_metros < 50:
            recargo += 5
    case 3:
        if cantidad_metros > 1000:
            bonificacion += 30
        elif cantidad_metros > 500:
            bonificacion += 20
        elif cantidad_metros < 200:
            recargo += 10
    case _:
        if cliente == 1 and subtotal_sin_impuesto < 35000:
            bonificacion += 5

bonificaciones = consumo_metro_cubico * (bonificacion / 100)
recargos = consumo_metro_cubico * (recargo / 100)
# iva = * 0.21
# precio_final = 

print(bonificaciones)
