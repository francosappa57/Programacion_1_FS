import validar

def crear_archivo(nombre, productos):
    with open(nombre, "w", encoding="utf-8") as arch:
        arch.write("ID,PRODUCTO,PRECIO")
        for fila in productos:
            linea = ", ".join(fila)
            arch.write(linea + "\n")


def leer_archivo(nombre):
    lista_productos = []
    with open(nombre, "r", encoding="utf-8") as arch:
        encabezado = arch.readlines()
        for i in arch:
            i = i.strip()
            if validar.validar_texto_vacio(i):
                partes = i.split(",")
                if len(partes) == 3:
                    producto = {
                        "id": partes[0].strip(),
                        "producto": partes[1].strip(),
                        "precio": partes[2].strip()
                    }
                    lista_productos.append(producto)
    return lista_productos