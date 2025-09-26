import Especificas as fe
import Array_Generales as fa

validacion = False
num = None

while validacion == False:
    print("\n---Sistema de opereciones numericas---")
    print("1. Ingresar datos\n"
          "2. Mostrar cantidad de positivos y negativos\n"
          "3. Sumar numeros pares\n"
          "4. Motrar mayor numero impar\n"
          "5. Mostrar numeros ingresados\n"
          "6. Mostrar numeros pares\n"
          "7. Mostrar numeros en posiciones impares\n"
          "8. Salir")
    opcion = input("Elige una opcion: ")


    if opcion == "1":
        num = fa.datos()
    elif opcion == "8":
        validacion = True
    
    if num == None:
        print("Tiene que ingresar datos antes de utilizar otras opciones")
    else:
        if opcion == "2":
            fe.pos_o_neg(num)
        elif opcion == "3":
            fa.sumar_pares(fe.num_par(num))
        elif opcion == "4":
            fe.mayor_impar(fe.num_impar(num))
        elif opcion == "5":
            fa.mostrar_todos(num)
        elif opcion == "6":
            fa.mostrar_pares(fe.num_par(num))
        elif opcion == "7":
            fa.mostrar_num_indice_impar(num)
