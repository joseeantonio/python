import pytest
from funciones_4_2 import raiz_cuadrada

def test_raiz_cuadrada():
    assert raiz_cuadrada(30) == 5
    assert raiz_cuadrada(66) == 8
    assert raiz_cuadrada(49) == 7