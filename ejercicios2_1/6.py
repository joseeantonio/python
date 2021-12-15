lista = []
while True:
    try:
        n1 = int(input("Introduzca el primer numero: "))
        lista.append(n1)
        n2 = int(input("Introduzca el segundo numero: "))
        n31 = int(input("Introduzca el tercer numero: "))
        lista.append(n1)
        lista.append(n2)
        print(max(lista))
    except ValueError:
        print("Introduce un numero por favor")