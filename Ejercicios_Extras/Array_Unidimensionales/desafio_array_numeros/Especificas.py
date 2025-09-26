def pos_o_neg(vector):
    cant_pos = 0
    cant_neg = 0
    for x in range(len(vector)):
        if vector[x] >= 0:
            cant_pos += 1
        else:
            cant_neg += 1
    print(f"\nCantidad de positivos: {cant_pos}"
          f"\nCantidad de negativos: {cant_neg}")


def num_par(vector):
    par = [0] * len(vector)
    cont_par = 0
    for x in range(len(vector)):
        if vector[x] %2 == 0:
            par[cont_par] = vector[x]
            cont_par += 1
    return par

def num_impar(vector):
    impar = [0] * len(vector)
    cont_impar = 0
    for x in range(len(vector)):
        if vector[x] %2 != 0:
            impar[cont_impar] = vector[x]
            cont_impar += 1
    return impar


def mayor_impar(vector):
    impar_mayor = 0
    for x in range(len(vector)):
        if vector[x] > impar_mayor:
            impar_mayor = vector[x]
    print(f"\nEl mayor numero impar es {impar_mayor}")