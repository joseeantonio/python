from funciones_5_1 import funcion_consonantes,funcion_vocales,vocales_mayusculas

def test_funcion_consonantes():
    assert funcion_consonantes("Programacion")=="Prgrmcn"
    assert funcion_consonantes("telefono")=="tlfn"

def test_funcion_vocales():
    assert funcion_vocales("Programacion")=="oaaio"
    assert funcion_vocales("borde")=="oe"

def test_vocales_mayusculas():
    assert vocales_mayusculas("Programacion")=="PrOgrAmAcIOn"
    assert vocales_mayusculas("borde")=="bOrdE"