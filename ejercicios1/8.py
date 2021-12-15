while True:
    try:
        n1 = int(input("Introduce un numero:"))
        n2 = int(input("Introduce el segundo numero:"))+n1
        n1 = int(input("Introduce el tercer numero:"))
        print("La suma total es:",n1+n2)
        break
    except ValueError:
        print("Introduce un numero por favor.")