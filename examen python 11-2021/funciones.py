import random

from ejercicios import ejercicios

#20->10 dic
#10->20 dic
#30->3 dic

def filtra_ejercicios(lista, minutos):
    l = []
    for diccionario in lista:
        if diccionario["duracion"]<=minutos:
            l.append(diccionario)
    return l


def duracion_ejercicios(lista):
    duracion_total = 0
    for diccionario in lista:
        duracion_total+=diccionario["duracion"]
    return duracion_total



def entrenamiento(lista,minutos):
    l = []
    while duracion_ejercicios(l)!=minutos:
        dic = random.choice(lista)
        if duracion_ejercicios(l)+dic["duracion"] <=minutos:
            l.append(dic)
    return l





