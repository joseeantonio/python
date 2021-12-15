from funciones import validar_contraseña_2
import pytest

def test_validar_contraseña_2():
    assert validar_contraseña_2("1-4","n","nsswe")==True
    assert validar_contraseña_2("1-5","n","nssdnwedw")== False