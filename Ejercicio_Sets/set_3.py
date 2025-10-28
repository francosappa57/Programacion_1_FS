conjunto_musica = {"rap", "electronica", "rock"}
lista_genero = []

while True:
    pedir_genero = input("Ingresa un genero de musica (dejar en blanco para terminar): ").lower()
    if pedir_genero == "":
        break
    lista_genero.append(pedir_genero)

conjunto_musica.update(lista_genero)

print(conjunto_musica)