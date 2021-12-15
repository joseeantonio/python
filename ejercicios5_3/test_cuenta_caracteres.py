import pytest
from funciones import cuenta_caracteres

def test_cuenta_caracteres():
    assert cuenta_caracteres("Programacion") == {"P":1,"r":2,"o":2,"g":1,"a":2,"m":1,"c":1,"i":1,"n":1}