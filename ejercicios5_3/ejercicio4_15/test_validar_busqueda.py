from funciones import validar_busqueda
import pytest

def test_validar_busqueda():
    assert validar_busqueda("filtra xxx")==True
    assert validar_busqueda("Jose Antonio")==False