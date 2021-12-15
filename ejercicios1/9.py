while True:
    try:
        print("La suma total es",int(input("Introduce un numero: "))+int(input("Introduce el segundo numero: "))
        +int(input("Introduce el tercer numero: ")))
        break
    except ValueError:
        print("Introduce un numero por favor")