def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area

base = float(input("Ingresa un numero: "))
altura = float(input("Ingresa otro numero: "))

resultado = area_triangulo(base, altura)

print(f"El area del triangulo es {resultado}")
