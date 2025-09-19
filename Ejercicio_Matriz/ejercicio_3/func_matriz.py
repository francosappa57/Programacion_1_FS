def produccion_por_producto(matriz, producto, dia):
    total_producto = [0] * producto
    for i in range(producto):
        for j in range(dia):
            total_producto[i] += matriz[i][j]
    print("\nTotal de produccion x PRODUCTO")
    for x in range(len(total_producto)):
        print(f". Producto {x + 1}: {total_producto[x]}")


def produccion_por_dia(matriz, producto, dia):
    total_dia = [0] * dia
    for i in range(producto):
        for j in range(dia):
            total_dia[j] += matriz[i][j]
    print("\nTotal de produccion x DIA")
    for x in range(len(total_dia)):
        print(f". Dia {x + 1}: {total_dia[x]}")
    return total_dia


def mayor_dia_produccion(total):
    dia = None
    mayor_produccion = 0
    for i in range(len(total)):
        if total[i] >= mayor_produccion:
            mayor_produccion = total[i]
            dia = i + 1
    print("\nMayor produccion diaria")
    print(f"Dia {dia} - Total {mayor_produccion} produccion diaria")
    

