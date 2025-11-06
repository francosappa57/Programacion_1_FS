persona_1 = {"francia", "brazil", "noruega"}
persona_2 = {"argentina", "noruega", "inglaterra", "brazil", "suiza"}
persona_3 = {"china", "japon", "noruega"}

validar = False
while validar == False:
    print("\n\t--- Menu de opciones ---")
    print("1. Total de paises visitados X persona\n"
          "2. Paises vistados por la perona 1 y persona 2\n"
          "3. Paises visitados por las 3 personas\n"
          "4. Salir")
    opcion = input("Elige una opcion: ")
    if opcion == "1":
        total_paises = persona_1.union(persona_2, persona_3)
        print("\n--- Total de paises visitados ---")
        print(f"Total = {len(total_paises)}\n"
              f"Paises = {total_paises}")
    elif opcion == "2":
        interseccion = persona_1.intersection(persona_2) - persona_3
        print("\n--- Paises vistados por persona 1 y persona 2 ---")
        print(interseccion)
    elif opcion == "3":
        paises_en_comun = persona_1.intersection(persona_2, persona_3)
        print("\n--- Paises visitados por las 3 personas ---")
        print(paises_en_comun)
    elif opcion == "4":
        validar = True
