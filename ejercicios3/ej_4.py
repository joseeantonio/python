def progresion_geometrica (n):
    x=1
    for i in range(1, n+1):
        x = n**i+x
    return x

if __name__ == '__main__':
    while True:
        try:
            n = int(input("Introduce un numero: "))
            if n<=0:
                print("Introduce un numero mayor que 0")
            else:
                print("El resultado es", progresion_geometrica(n))
                break
        except ValueError:
            print("Introduce un numero por favor.")