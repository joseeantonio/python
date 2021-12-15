from funciones import central

if __name__ == '__main__':
    while True:
        try:
            n1 = int(input("Introduce el primer numero: "))
            n2 = int(input("Introduce el segundo numero: "))
            n3 = int(input("Introduce el tercer numero: "))
            print("El numero central es",central(n1,n2,n3))
        except ValueError:
            print("Introduce un numero por favor.")