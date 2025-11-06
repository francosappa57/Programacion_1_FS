import validar

def crear_lista_prodcutos(producto, cantidad):
    print("\n--- Lista de productos ---")
    for i in range(cantidad):
        temporal = []
        print(f"\n. Producto {i + 1}")
        id = input("Ingresa ID del producto: ").strip().lower()
        elmento = input("Ingresa producto: ").strip().lower()
        precio = input("Ingresa precio producto: ").strip().lower()
        temporal.append(id)
        temporal.append(elmento)
        temporal.append(precio)
        producto.append(temporal)

def mostrar_catalogo(productos):
    if not validar.validar_catalogo_vacio(productos):
        return
    print("╔" + "═" * 7 + "╦" + "═" * 27 + "╦" + "═" * 17 + "╗")
    print(f"║ {'ID':^5} ║ {'PRODUCTO':^25} ║ {'PRECIO':^15} ║")
    print("╠" + "═" * 7 + "╬" + "═" * 27 + "╬" + "═" * 17 + "╣")
    for i, j in enumerate(productos):
        print(f"║ {j['id']:^5} ║ {j['producto']:^25} ║ {j['precio']:^15} ║")
        if i < len(productos):
            print("╠" + "═" * 7 + "╬" + "═" * 27 + "╬" + "═" * 17 + "╣")
    print("╚" + "═" * 7 + "╩" + "═" * 27 + "╩" + "═" * 17 + "╝")