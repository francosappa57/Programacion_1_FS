def buscar_mayor(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        if num2 >= num3:
            return num1, num2, num3
        else:
            return num1, num3, num2
    elif num2 >= num1 and num2 >= num3:
        if num1 >= num3:
            return num2, num1, num3
        else:
            return num2, num3, num1
    else:
        if num1 >= num2:
            return num3, num1, num2
        else:
            return num3, num2, num1

numero1 = float(input("Ingresa el primer numero: "))
numero2 = float(input("Ingresa el segundo numero: "))
numero3 = float(input("Ingresa el tercer numero: "))

num_max, num_medio, num_min = buscar_mayor(numero1, numero2, numero3)

print(f"Ordenados de mayor a menor: {num_max}, {num_medio}, {num_min}")