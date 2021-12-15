from funciones import numeros_perfectos

if __name__ == '__main__':
    while True:
        try:
            n = int(input("Introduce un numero: "))
            if n<=0:
                print("Introduce un numero por favor.")
            else:
                for x in numeros_perfectos(n):
                    print("El numero",x,"es perfecto")
        except ValueError:
            print("Introduce un numero por favor")
