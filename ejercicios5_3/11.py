from funciones import cuenta_caracteres

if __name__ == '__main__':
    coma = ""
    while True:
        try:
            palabra = input("Introduce una palabra: ")
            diccionario = cuenta_caracteres(palabra)
            for letra, num in diccionario.items():
                print(coma,num,letra,end="")
                coma= ","
            break
        except ValueError:
            print("Introduce una palabra por favor")
