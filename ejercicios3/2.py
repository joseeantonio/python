def longitud_circunferencia(radio):
    return 2*3.14*radio

while True:
    try:
        r = int(input("Introduce el radio de la circunferencia: "))
        if r<=0:
            print("Introduce un numero mayor que 0 por favor.")
        else:
            print("La longitud de la circunferencia es:", longitud_circunferencia(r))
            break
    except ValueError:
        print("Introduce un numero por favor.")