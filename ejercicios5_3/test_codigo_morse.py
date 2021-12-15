import pytest
from funciones import codigo_morse

def test_codigo_morse():
    assert codigo_morse("Hola") == {"H":"....","O":"---","L":".-..","A":".-"}