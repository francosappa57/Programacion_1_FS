CANTIDAD = 5
usuario_1 = [''] * CANTIDAD
usuario_2 = [''] * CANTIDAD

def productos_comun(vec_1, vec_2):
    for i in range(len(vec_1)):
        for j in range(len(vec_2)):
            if vec_1[i].lower() == vec_2[j].lower():
                print(vec_2[j])

def productos_dif(vec_1, vec_2):
    u1 = [''] * len(vec_1)
    u2 = [''] * len(vec_2)
    for i in range(len(vec_1)):
        for j in range(len(vec_2)):
            if vec_1[i].lower() != vec_2[j].lower():
                pass