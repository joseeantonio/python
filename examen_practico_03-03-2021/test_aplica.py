from funciones import aplica
import pytest

def test_aplica():
    assert aplica({"NOMBRE":"pepe","PV":100},{"TIPO":"ATACAR","PV":60,"POSIBILIDAD":100})=={"NOMBRE":"pepe","PV":40}
    assert aplica({"NOMBRE": "pepe", "PV": 100}, {"TIPO": "ATACAR", "PV": 60, "POSIBILIDAD": 0}) == {"NOMBRE": "pepe",
                                                                                                       "PV": 100}