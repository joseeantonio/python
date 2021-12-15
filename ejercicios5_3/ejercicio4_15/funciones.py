

def validar_tlf(entrada):
    lista_espacios = entrada.split(" ")
    if len(lista_espacios) == 1:
        if len(lista_espacios[0]) == 9:
            if lista_espacios[0].isdigit():
                return True
        return False
    elif len(lista_espacios)>2:
        if 2 <= len(lista_espacios[0]) <= 5:
            if lista_espacios[0][0] == "+":
                for x in lista_espacios[1:-1]:
                    if not x.isdigit():
                        return False
                return True
            else:
                numero = entrada.replace(" ","")
                if numero.isdigit():
                    return True
        return False
    else:
        return False

def validar_nombre(entrada):
    if entrada[0].isalpha():
        return True
    return False

def existe_nombre(diccionario,nombre):
    for x in diccionario.keys():
        if x==nombre:
            return True
    return False


def existe_tlf(diccionario,tlf):
    for x in diccionario.values():
        if x==tlf:
            return True
    return False

def mostrar_tlf(diccionario,nombre):
    for nombre_dic,tlf in diccionario.items():
        if nombre==nombre_dic:
            return tlf


def mostrar_nombre(diccionario,tlf):
    for nombre,tlf_dic in diccionario.items():
        if tlf_dic==tlf:
            return nombre

def busqueda(diccionario,entrada):
    lista_split = entrada.split(" ")
    diccionario_busqueda = {}
    for nombre,telefono in diccionario.items():
        if lista_split[1] in nombre:
            diccionario_busqueda[nombre] = telefono
    return diccionario_busqueda

def validar_busqueda(entrada):
    lista_split = entrada.split(" ")
    if lista_split[0]=="filtra":
        return True
    return False