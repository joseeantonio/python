lista = []
while True:
    try:
        n = int(input("Introduzca el primer numero: "))
        if n%2 == 0:
            print("El numero",n,"es par")
        else:
            print("El numero",n,"es impar")
    except ValueError:
        print("Introduce un numero por favor")