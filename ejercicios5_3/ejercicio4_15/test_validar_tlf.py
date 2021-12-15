from funciones import validar_tlf
import pytest

def test_validar_tlf():
    assert validar_tlf("123456789") == True
    assert validar_tlf("a5a5a55a5") == False
    assert validar_tlf("+34 765 324 123") == True
    assert validar_tlf("+34243 234243546") == False
    assert validar_tlf("+ 345 245 245") == False