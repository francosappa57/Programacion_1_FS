# Programa de facturacion de servicio de agua potable

metros_cubicos = float(input("Indique consumo por metro cubico (numeros enteros): "))

print("\n-Lugar-\n"+
      "1. Residencial\n"+
      "2. Comercial\n"+
      "3. Industrial"
    )
cliente = int(input("Elija una opcion: "))

precio_fijo = 7000
consumo_metro_cubico = metros_cubicos * 200
subtotal_sin_impuesto = precio_fijo + consumo_metro_cubico
bonificacion = 0
recargo = 0

match cliente:
    case 1:
        if metros_cubicos < 30:
            bonificacion += 0.10
        elif metros_cubicos > 80:
            recargo += 1.15
    case 2:
        if metros_cubicos > 300:
            bonificacion += 0.12
        elif metros_cubicos > 150:
            bonificacion += 0.08
        elif metros_cubicos < 50:
            recargo += 1.05
    case 3:
        if metros_cubicos > 1000:
            bonificacion += 0.30
        elif metros_cubicos > 500:
            bonificacion += 0.20
        elif metros_cubicos < 200:
            recargo += 1.10
    case _:
        print("Opcion incorrecta")

if cliente == 1 and subtotal_sin_impuesto <= 35000:
    bonificacion += 0.05

bonificaciones = subtotal_sin_impuesto * bonificacion
recargos = subtotal_sin_impuesto * recargo
subtotal_recargos_bonificaciones = subtotal_sin_impuesto + recargos - bonificaciones
iva = subtotal_recargos_bonificaciones * 0.21
precio_final = subtotal_recargos_bonificaciones + iva

print("\n-----Resumen-----")
print(f"Subtotal: ${float(subtotal_sin_impuesto)}\n"
      f"Bonificaciones: -${float(bonificaciones)}\n"
      f"Recargos: +${float(recargos)}\n"
      f"Subtotal con recargos/bonificaciones: ${float(subtotal_recargos_bonificaciones)}\n"
      f"IVA: +${float(iva)}\n"
      f"Total a pagar: ${float(precio_final)}"
      )
