def potencia_numero(num, potencia):
    return num ** potencia

base = float(input("Ingresa un numero: "))
exponente = float(input("Ingresa un exponente: "))
resultado = potencia_numero(base, exponente)

print(f"{base} elevado a {exponente} = {resultado}")