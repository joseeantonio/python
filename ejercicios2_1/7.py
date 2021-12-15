lista = []
while True:
    try:
        n1 = int(input("Introduzca el primer numero: "))
        n2 = int(input("Introduzca el segundo numero: "))
        operacion= input(("Escribe una de las siguientes operaciones : sumar, restar, multiplicar o dividir: "))
        if operacion == "sumar":
            print("La suma es",n1+n2)
            break
        elif operacion == "restar":
            print("La resta es",n1-n2)
            break
        elif operacion == "multiplicar":
            print("La multiplicacion es",n1*n2)
            break
        elif operacion == "dividir":
            print("La division es",n1/n2)
            break
        else:
            print("Introduce una operacion valida,por favor")
    except ValueError:
        print("Introduce un numero por favor")