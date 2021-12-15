from funciones_4_2 import billete

if __name__ == '__main__':
    while True:
        try:
            distancia_recorrer = int(input("Introduce la distancia a recorrer: "))
            dias_estancia = int(input("Introduce los dias de estancia: "))
            if distancia_recorrer<=0 or dias_estancia<=0:
                print("Introduce un numero mayor que cero por favor.")
            else:
                print("El coste del billete es",billete(distancia_recorrer,dias_estancia))
        except ValueError:
            print("Introduce un numero por favor.")