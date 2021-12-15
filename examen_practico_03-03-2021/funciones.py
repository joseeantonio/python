# JUGADORES -> {"NOMBRE":"pepe","PV":56}
# ACCION ATACAR -> {"TIPO":"ATACAR","PV":60,"OBJETIVO":"Mario","POSIBILIDAD":"34}
# ACCION CURAR -> {"TIPO":"CURAR","PV":60,"OBJETIVO":"Mario"}
import random
from random import randint


def jugador(lista,nombre):
    for diccionario in lista:
        for valor in diccionario.values():
            if valor==nombre:
                return diccionario


def aplica(dic_jugador,dic_accion):
    if dic_accion["TIPO"]=="CURAR":
        dic_jugador["PV"]+=dic_accion["PV"]
    elif dic_accion["TIPO"]=="ATACAR":
        posibilidad = random.randint(1,101)
        if posibilidad<=dic_accion["POSIBILIDAD"]:
            dic_jugador["PV"]-=dic_accion["PV"]
    return dic_jugador


def crear(lista,nombre,pv):
    dic = {"NOMBRE":nombre,"PV":pv}
    lista.append(dic)
    return lista