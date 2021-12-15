while True:
    try:
        n = float(input("Introduzca una calificacion entre 0.0 y 1.0: "))
        if n<0:
            print("Introduce un numero mayor de 0")
        elif n>1.0:
            print("Introduce un numero menor de 1.0")
        else:
            break
    except ValueError:
        print("Introduce un numero por favor.")

if n>=0.9:
    print("Sobresaliente")
elif n>=0.8:
    print("Notable")
elif n>=0.7:
    print("Bien")
elif n>=0.6:
    print("Suficiente")
else:
    print("Insufuciente")