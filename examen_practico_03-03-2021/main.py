from funciones import *


# JUGADORES -> {"NOMBRE":"pepe","PV":56}
#ATACAR -> {"TIPO":"ATACAR","PV":60,"POSIBILIDAD":"34}
# ACCION CURAR -> {"TIPO":"CURAR","PV":60,"OBJETIVO":"Mario"}


if __name__ == '__main__':
    print("""ÓRDENES:
- crear NOMBRE PV
- ataque JUGADOR OBJETIVO PV POSIBILIDAD
- cura JUGADOR PV
- listado
- Fin""")
    lista_jugadores = []
    while True:
        try:
            entrada = input("Introduzca una orden: ")
            if entrada=="crear":
                nombre = input("Introduzca su nombre: ")
                pv = int(input("Introduzca su pv: "))
                crear(lista_jugadores,nombre,pv)
            elif entrada=="atacar":
                pv = int(input("Introduce el pv a atacar: "))
                objetivo = input("Introduce el objetivo: ")
                posibilidad = int(input("Introduce la posibilidad de ataque: "))
                dic_objetivo = jugador(lista_jugadores,objetivo)
                aplica(dic_objetivo, {"TIPO":"ATACAR","PV":pv,"POSIBILIDAD":posibilidad})
            elif entrada=="curar":
                objetivo = input("¿A quien quieres curar? ")
                pv = int(input("¿Cuanta vida le vas a dar? "))
                dic_objetivo = jugador(lista_jugadores,objetivo)
                aplica(dic_objetivo, {"TIPO":"CURAR","PV":pv})
            elif entrada=="listado":
                print(lista_jugadores)
            elif entrada=="fin":
                print("Adios")
                break
            else:
                print("Accion no identificada.")
        except ValueError:
            print("Entrada no valida.")