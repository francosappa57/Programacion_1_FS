alumnos = int(input("Cuantos alumnos son en la clase? "))
aprobados = 0
desaprobados = 0

for x in range(alumnos):
    nota = float(input(f"Ingresar nota alumno {x + 1}: "))
    if nota >= 4:
        aprobados += 1
    else:
        desaprobados += 1

print(f"En la clase con {alumnos} alumnos, aprobaron {aprobados} y desaprobaron {desaprobados}")

