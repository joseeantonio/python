from funciones import validar_contraseña
import pytest

def test_validar_contraseña():
    assert validar_contraseña("1-2","t","jtjn")==True
    assert  validar_contraseña("3-4","e","ygkhb")==False