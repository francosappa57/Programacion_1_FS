# Ejercicio 1: Registro de Temperaturas
# Una estación meteorológica registra las temperaturas diarias de una semana (7 días) en 3 horarios (mañana, tarde y noche).
# Cargar en una matriz 7x3 las temperaturas (números enteros) y mostrar:
#     El promedio de temperatura de cada día.
#     El promedio general de toda la semana.
import func_matriz as fm

SEMANA = 7
HORARIO = 3
DIAS = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
              
              # M  T  N
temperatura = [[0, 0, 0], # LUNES
               [0, 0, 0], # MARTES
               [0, 0, 0], # MIERCOLES 
               [0, 0, 0], # JUEVES
               [0, 0, 0], # VIERNES 
               [0, 0, 0], # SABADO
               [0, 0, 0]  # DOMINGO
               ]

salida = False

while salida == False:
    print("\t---Registro Meteorologico---")
    print("1. Cargar datos\n"
          "2. Mostrar promedio x dia\n"
          "3. Mostrar promedio semanal\n"
          "4. Salir")
    opcion = input(f"Elige una opcion: ")
    
    if opcion == "1":
        fm.cargar_datos(temperatura, SEMANA, HORARIO)
    elif opcion == "2":
        respuesta = fm.mostrar_promedio_dias(temperatura, SEMANA, HORARIO)
        print("Promdedio x DIA")
        for i in range(len(respuesta)):
            print(f"{DIAS[i]}: {respuesta[i]:.2f}")
    elif opcion == "3":
        respuesta = fm.mostrar_promedio_semanal(temperatura, SEMANA, HORARIO)
        print(f"El promedio semanal fue de {respuesta:.2f}")
    elif opcion == "4":
        salida = True