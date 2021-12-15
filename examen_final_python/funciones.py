import operator
#hoyo_par = {"1":5,"2":8}
#hoyo_golpes = {"1":6,"2":10}


def crear_cambiar(diccionario,hoyo,par):
    diccionario[hoyo]=int(par)
    return diccionario


def resultados(diccionario,hoyo,golpes):
    diccionario[hoyo]=int(golpes)
    return diccionario

def existe_par(diccionario,hoyo):
    if hoyo in diccionario.keys():
        return True
    return False

def listado(diccionario_par,diccionario_golpes):
    lista_final = []
    for hoyo_par,par in diccionario_par.items():
        for hoyo_golpes, golpes in diccionario_golpes.items():
            diccionario = {}
            if hoyo_par == hoyo_golpes:
                diccionario["HOYO"]=hoyo_par
                diccionario["GOLPES"]=golpes
                diccionario["Par"]=par
                lista_final.append(diccionario)
    return lista_final

def terminologia(golpes,par):
    if golpes==par:
        return "par"
    elif golpes+1==par:
        return "birdie"
    elif golpes-1==par:
        return "bogey"
    elif golpes+2==par:
        return "eagle"
    elif golpes-2==par:
        return "doble bogey"

def resultado_final(diccionario_golpe,diccionario_par):
    diccionario = {}
    for hoyo1,golpe in diccionario_golpe.items():
        for hoyo2,par in diccionario_par.items():
            if hoyo1==hoyo2:
                if golpe > par:
                    nota = golpe-par
                elif golpe < par:
                    nota = par-golpe
                diccionario[hoyo1]=nota
    return diccionario