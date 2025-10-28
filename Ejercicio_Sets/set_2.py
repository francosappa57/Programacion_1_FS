primera_frase = input("Ingresa una frase: ").lower()
segunda_frase = input("Ingresa otra frase: ").lower()

lista_f1 = set(primera_frase.split())
lista_f2 = set(segunda_frase.split())

nuevo_conj = lista_f1.intersection(lista_f2)

print(nuevo_conj)

