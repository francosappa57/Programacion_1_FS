while True:
    color = input("Ingresa un color: ").lower()
    if color == "rojo" or color == "verde" or color == "azul":
        print((color).capitalize())
        break
    else:
        print("Solo los colores primarios")

