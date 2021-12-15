from funciones import factores

if __name__ == '__main__':
    while True:
        try:
            n = int(input("Introduce un numero mayor que 2: "))
            if n<3:
                print("Mayor que 2 por favor.")
            else:
                print(*factores(n))
                break
        except ValueError:
            print("Introduce un numero por favor.")