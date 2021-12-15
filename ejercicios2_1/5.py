lista = []
while True:
    try:
        n1 = int(input("Introduzca el primer numero: "))
        n2 = int(input("Introduzca el segundo numero: "))
        n3 = int(input("Introduzca el tercer numero: "))
        lista.append(n1)
        lista.append(n2)
        lista.append(n3)
        print(max(lista))
    except ValueError:
        print("Introduce un numero por favor")