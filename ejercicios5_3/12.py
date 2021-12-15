from funciones import pulsaciones

if __name__ == '__main__':
    coma = "Las teclas son:"
    while True:
        try:
            palabra = input("Introduce una palabra: ")
            teclas = pulsaciones(palabra).values()
            for tecla in teclas:
                print(coma,tecla,sep="",end="")
                coma = ", "
            break
        except ValueError:
            print("Introduce una palabra valida")