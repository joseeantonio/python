from funciones import validar_nombre
import pytest


def testvalidar_nombre():
    assert validar_nombre("f-*+27hwhañe+") == True
    assert validar_nombre("2uwbcebc") == False
