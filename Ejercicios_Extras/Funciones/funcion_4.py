def area_rectangulo(base, altura):
    return base * altura

base_rectangulo = float(input("Ingresa un numero: "))
altura_rectangulo = float(input("Ingresa otro numero: "))
area = area_rectangulo(base_rectangulo, altura_rectangulo)

print(f"El area del rectangulo es {area}")
