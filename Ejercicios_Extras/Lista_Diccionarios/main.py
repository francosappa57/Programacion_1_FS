from Lady_Gaga import playlist_lady_gaga as plg
import funciones as f

while True:
    print("\n--- Lady Gaga's Music Videos ---")
    print("1. Mostrar Tema\n"
          "2. Ordenar Temas\n"
          "3. Calcular promedio de visitas\n"
          "4. Mostrar video/s mas visto/s\n"
          "5. Mostrar video/s menos visto/s\n"
          "6. Mostrar Tema por URL\n"
          "7. Mostrar Tema/s por Colaboracion\n"
          "8. Mostrar Tema/s por Mes de lanzamiento\n"
          "9. Salir")
    opcion = input("Elige una opcion (1-9): ")

    if opcion == "1":
        f.monstrar_tema(plg)
    elif opcion == "2":
        f.ordenar_por_duracion(plg)
    elif opcion == "3":
        f.promedio_por_visitas(plg)
    elif opcion == "4":
        f.video_mas_visto(plg)
    elif opcion == "5":
        f.video_menos_visto(plg)
    elif opcion == "6":
        f.buscar_tema_url(plg)
    elif opcion == "7":
        pass
    elif opcion == "8":
        pass
    elif opcion == "9":
        break
    else:
        print("Opcion incorrecta. Intente nuevamente") 