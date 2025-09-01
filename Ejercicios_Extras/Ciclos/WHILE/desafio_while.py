empleados = 0
cantidad_masculinos_iot = 0
cantidad_masculinos_ia = 0

no_votos_ia = 0

empleado_masculino_mayor = None
edad_masculino_mayor = 0
voto_masculino_mayor = None

while empleados <= 10:
    usuario = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    if edad < 18:
        print("No puede participar de la encuesta")
    else:
        genero = int(input("1. Masculino\n"
                        "2. Femenino\n" 
                        "3. Otro\n"
                        "Eliga una opcion: "))
        
        tecnologia = input("-Inteligencia Articifial (IA)\n"
                        "-Realidad Virtual/Aumentada (RV/RA)\n"
                        "-Internet de las Cosas (IOT)\n"
                        "Eliga una opcion: ").lower()
        if tecnologia != "ia" and tecnologia != "rv" and tecnologia != "ra" and tecnologia != "iot":
            print("Tecnologia inexistente. Intente nuevamente")
        else:
            if genero == 1:
                if edad >= 25 and edad <= 50:
                    if tecnologia == "iot":
                        cantidad_masculinos_iot += 1
                    elif tecnologia == "ia":
                        cantidad_masculinos_ia += 1

                if edad > edad_masculino_mayor:
                    empleado_masculino_mayor = usuario
                    voto_masculino_mayor = tecnologia

            if genero != 2:
                if edad >= 33 and edad <= 40:
                    if tecnologia != "ia":
                        no_votos_ia += 1
            
            empleados += 1
    vuelta = input("Quiere ingresar otro usuario? (s/n) ").lower()
    if vuelta == "n":
        break


if empleados == 0:
    print("No hubo votos en la encuesta")
else:
    porcentaje_no_ia = (no_votos_ia * 100) / empleados
    print("\n---Datos---")
    print(f"Cantidad de empleados que votaron: {empleados}\n"
          f"Empleados masculinos (25 a 50 años) votaron por IOT: {cantidad_masculinos_iot}\n"
          f"Empleados masculinos (25 a 50 años) votaron por IA: {cantidad_masculinos_ia}\n"
          f"Porcentaje empleados (33 a 40 años) no votaron por IA: {porcentaje_no_ia}%\n"
          f"Empleado masculino de mayor edad es {(empleado_masculino_mayor).capitalize()} y voto por {(voto_masculino_mayor).upper()}\n")
    



