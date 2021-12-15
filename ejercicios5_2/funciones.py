def eliminar_extremos(lista):
    lista.pop(0)
    lista.pop(len(lista)-1)
    return lista

def en_orden_ascendente(lista):
    if lista==sorted(lista):
        return True
    return False

def esta_ordenada(lista):
    ascendente = sorted(lista)
    descendente = list(reversed(ascendente))
    if lista==ascendente or lista==descendente:
        return True
    return False


def hay_duplicados(lista):
    for x in lista:
        if lista.count(x)>1:
            return True
    return False


def elimina_duplicados(lista1):
    lista1 = sorted(lista1)
    lista2 = []
    for x in lista1[:]:
        if lista1.count(x)>1:
            lista1.pop(x)
            lista2.append(x)
    return lista2



def palindromos(lista):
    for palabra in lista[:]:
        if not palabra == palabra[::-1]:
            lista.remove(palabra)
    return lista