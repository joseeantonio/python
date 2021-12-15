import pytest
from funciones import numeros_perfectos

def test_numeros_perfectos():
    assert numeros_perfectos(7)==[6]
    assert numeros_perfectos(9999)==[6,28,496,8128]