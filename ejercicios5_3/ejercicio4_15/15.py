import operator

from funciones import *


if __name__ == '__main__':
    diccionario = {}
    while True:
        try:
            entrada = input("Introduce algo por teclado: ")
            if entrada == "adios":
                print("Hasta luego")
                break
            elif entrada == "listado":
                diccionario_ordenado = sorted(diccionario.items(), key=operator.itemgetter(0))
                print(diccionario_ordenado)
            elif validar_busqueda(entrada):
                print(busqueda(diccionario,entrada))
            elif validar_nombre(entrada):
                if existe_nombre(diccionario,entrada):
                    print("El telefono de",entrada,"es",mostrar_tlf(diccionario,entrada))
                else:
                    tlf = input("Introduce su numero: ")
                    if validar_tlf(tlf):
                        if not existe_tlf(diccionario,tlf):
                            diccionario[entrada] = tlf
                        else:
                            print("El telefono",tlf,"ya existe.")
                    else:
                        print("Introduzca un telefono valido por favor.")
            elif validar_tlf(entrada):
                if existe_tlf(diccionario,entrada):
                    print("El telefono",entrada,"esta en uso por",mostrar_nombre(diccionario,entrada))
                else:
                    nombre = input("Introduce el nombre: ")
                    if validar_nombre(nombre):
                        if not existe_nombre(diccionario,nombre):
                            diccionario[nombre] = entrada
                        else:
                            print("El nombre", nombre, "esta en uso.")
                    else:
                        print("El nombre no es correcto.")
            else:
                print("Introduce un valor correcto")
        except ValueError:
            print("Introduce algo correcto")