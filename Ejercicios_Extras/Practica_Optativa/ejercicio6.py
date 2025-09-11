num_positivo = 0
cont_posi = 0

num_negativo = 0
cont_neg = 0

while True:
    numero = float(input("Ingresa un numero(0 para finalizar): "))
    if numero > 0:
        num_positivo += numero
        cont_posi += 1
    else:
        num_negativo += numero
        cont_neg += 1   
    
    if numero == 0:
        break

prom_posi = num_positivo / cont_posi
prom_neg = num_negativo / cont_neg

print(f"El promedio de numeros positivos es {prom_posi:.2f}")
print(f"El promedio de numeros negativos es {prom_neg:.2f}")
