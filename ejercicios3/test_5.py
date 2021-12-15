import pytest

from ej_5 import validar_fecha

def test_validar_fecha():
    assert validar_fecha(1,1,2002)==True
    assert validar_fecha(1,32,2002)==False
    assert validar_fecha(29,2,2024)==True
    assert validar_fecha(29,2,2002)==False
    assert validar_fecha(28,2,2002)==True
    assert validar_fecha(31,6,2002)==False
    assert validar_fecha(30,6,2002)==True
    assert validar_fecha(1,13,2002)==False