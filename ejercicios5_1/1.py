from funciones_5_1 import funcion_consonantes , funcion_vocales , vocales_mayusculas

if __name__ == '__main__':
    while True:
        try:
            palabra = input("Introduce una palabra: ")
            print(funcion_consonantes(palabra))
            print(funcion_vocales(palabra))
            print(vocales_mayusculas(palabra))
            break
        except ValueError:
            print("Introduce una palabra por favor.")