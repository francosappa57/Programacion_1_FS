def validar_texto_vacio(texto):
    return texto.strip() != ""

def validar_catalogo_vacio(catalogo):
    if len(catalogo) == 0:
        print("No existe catalogo...")
        return False
    return True