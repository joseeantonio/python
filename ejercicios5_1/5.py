def ahorcado(palabra, acertadas ):
    guion="_"
    salida=""
    for x in palabra:
        if x in acertadas:
            salida += x
        else:
            salida += guion
    return salida


import random
lista = ["cerillas", "patrulla", "papel", "azor", "alerones", "conversar", "sollozo", "manzana"]
palabra = random.choice(lista)
intentos = 5
if __name__=="__main__":
    acertadas = ""
    while intentos > 0:
        try:
            print("Te quedan", intentos, "intentos")
            print(ahorcado(palabra, acertadas))
            letra = input("Introduce una letra: ")
            if palabra != ahorcado(palabra,letra):
                if (letra in palabra) :
                    acertadas+= letra
                else:
                    print("Ops has fallado")
                    intentos -= 1

            else:
                print("Has acertado la palabra.")
                break
        except ValueError:
            print ("Introduce una letra.")