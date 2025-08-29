def mostrar_atracciones():
    print("\n-Atracciones-\n"+
        ". Montaña Rusa $1500\n"+
        ". Casa del Terror $1200\n"+
        ". Carrusel $800")

def puede_subir(edad, atraccion):
    if atraccion == "montaña rusa":
        if edad >= 12:
            valor = True
        else:
            valor = False
    elif atraccion == "casa del terror":
        if edad > 6:
            valor = True
        else:
            valor = False
    else: 
        valor = True
    return valor
    
       
def calcular_precio(atraccion):
    if atraccion == "montaña rusa":
        pago = 1500
    elif atraccion == "casa del terror":
        pago = 1200
    else: 
        pago = 800
    return pago
    

def descuento(cantidad, pago):
    if cantidad >= 3:
        rebaja = pago * 0.10 
    else:
        rebaja = 0
    return rebaja
    

def registrar_visita(usuario, edad, atraccion_elegida, atraccion_permitida, pago):
    resumen = (f"\n-Resumen-\n"
      f"Nombre: {usuario}\n"
      f"Edad: {edad}\n"
      f"Atracciones Elegidas: {atraccion_elegida}\n"
      f"Atracciones Permitidas: {atraccion_permitida}\n"
      f"Total a pagar: ${pago}")
    return resumen
    

def mostrar_resumen(datos):
    print(datos)
    