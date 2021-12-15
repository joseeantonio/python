from funciones import hay_duplicados
import random

if __name__ == '__main__':
    lista = []
    while True:
        lista.append(random.randint(1,101))
        if len(lista)==20:
            if not hay_duplicados(lista):
                print(lista)
                break
            lista = []