while True:
    try:
        h = int(input("Horas de trabajo: "))
        c = int(input("Coste por horas: "))
        print("Importe total: ",h*c)
        break
    except ValueError:
        print("Introduce un numero por favor.")