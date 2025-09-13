import funciones_definidas.funcion as ff

vector = ff.agregar_nombres(ff.pedir_cantidad())
#reemplazos = None

while True:
    nom_viejo = []
    nom_nuevo = []

    viejo = input("Ingresa el nombre a buscar: ")
    nuevo = input("Ingresa nombre para reeemplazar el anterior: ")
    buscar = input("Queres buscar otro?(y/n) ").lower()
    if buscar == "n":
        reemplazos = ff.reemplazar_nombre(vector, viejo, nuevo)
        break
    
    
    
    
print(f"Se realizaron {reemplazos} reemplazos")

