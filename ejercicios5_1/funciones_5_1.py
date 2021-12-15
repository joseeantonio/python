def funcion_consonantes(palabra):
    vocales = "aeiouAEIOU"
    consonantes = ""
    for x in palabra:
        if not x in vocales:
            consonantes+=x
    return consonantes

def funcion_vocales(palabra):
    vocales = "aeiouAEIOU"
    resultado = ""
    for x in palabra:
        if x in vocales:
            resultado+=x
    return resultado

def vocales_mayusculas(palabra):
    vocales = "aeiouAEIOU"
    resultado = ""
    for x in palabra:
        if x in vocales:
            resultado+=x.upper()
        else:
            resultado+=x
    return resultado


from random import randint
def contrasena_aleatoria():
    contra =""
    x=randint(7,10)
    while len(contra)!=x:
        i=randint(33,126)
        contra+=chr(i)
    return contra




def validar_contra(contra):
    numeros = "123456"
    mayuscula = 0
    minuscula = 0
    numero = 0
    if len(contra)>=8:
        for x in contra:
            if not x in numeros and x==x.upper():
                mayuscula+=1
            if x==x.lower():
                minuscula+=1
            if x in numeros:
                numero+=1
    if numero>0 and mayuscula>0 and minuscula>0:
        return True
    return False




