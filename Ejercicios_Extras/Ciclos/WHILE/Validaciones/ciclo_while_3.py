while True:
    nota = int(input("Ingresa tu nota: "))
    if nota <=10 and nota >= 1:
        print(f"Tu nota es {nota}")
        break
    else:
        print("La nota tiene que estar en el 1 y 10")
