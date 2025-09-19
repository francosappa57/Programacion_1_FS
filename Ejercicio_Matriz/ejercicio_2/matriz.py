# Ejercicio 2: Puntajes de un Torneo
# En un torneo de programación hay 4 equipos que compiten en 5 rondas.
# Cargar en una matriz 4x5 los puntajes obtenidos (enteros). Luego mostrar:
#     El puntaje total de cada equipo.
#     Qué equipo obtuvo el mayor puntaje en total.
import func_matriz as fm

EQUIPOS = 4
RONDAS = 5

         # R1 R2 R3 R4 R5
torneo = [[0, 0, 0, 0, 0], # EQUIPO 1 
          [0, 0, 0, 0, 0], # EQUIPO 2
          [0, 0, 0, 0, 0], # EQUIPO 3
          [0, 0, 0, 0, 0]  # EQUIPO 4
          ]

print("\t---Inicio del Torneo---")
fm.inicio_torneo(torneo, EQUIPOS, RONDAS)

print("\n---Puntajes Totales---")
total = fm.puntaje_total_equipo(torneo, EQUIPOS, RONDAS)
for i in range(len(total)):
    print(f"Equipo {i + 1}: {total[i]} puntos")

print("\n---Resultado Final---")
equipo_ganador, pun_mayor = fm.ganador(total)
print(f"El ganador es el Equipo {equipo_ganador} con {pun_mayor} puntos")