
from funciones_4_2 import raiz_cuadrada

if __name__ == '__main__':
    while True:
        try:
            n = int(input("Introduce un numero: "))
            if n<=0:
                print("Introduce un numero positivo por favor.")
            else:
                print("La raiz cuadrada del numero",n,"es",raiz_cuadrada(n))
                break
        except ValueError:
            print("Introduce un numero por favor.")