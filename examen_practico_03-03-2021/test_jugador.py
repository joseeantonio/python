from funciones import jugador
import pytest

def test_jugador():
    assert jugador([{"NOMBRE":"Pepe","PV":56},{"NOMBRE":"Maria","PV":100}],"Maria")=={"NOMBRE":"Maria","PV":100}
    assert jugador([{"NOMBRE": "Pepe", "PV": 56}, {"NOMBRE": "Maria", "PV": 100}], "Mario") == None