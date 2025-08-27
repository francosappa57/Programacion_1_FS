def area_circulo(radio, pi=3.14):
    return pi * (radio ** 2)

radio_circulo = float(input("Ingresa un numero: "))
area = area_circulo(radio_circulo)

print(f"El area del circulo es {area}")