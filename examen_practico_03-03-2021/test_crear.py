from funciones import crear
import pytest

def test_crear():
    assert crear([],"juan",100)==[{"NOMBRE":"juan","PV":100}]
    assert crear([{"NOMBRE": "juan", "PV": 100}], "maria", 90) == [{"NOMBRE": "juan", "PV": 100},{"NOMBRE": "maria", "PV": 90}]