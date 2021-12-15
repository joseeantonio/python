from funciones import crear_cambiar
import pytest

def test_crear_cambiar():
    assert crear_cambiar({"1":4,"2":5,"4":7},"1","3")=={"1":3,"2":5,"4":7}
    assert crear_cambiar({"1":4,"2":5,"4":7},"3","2")=={"1":4,"2":5,"4":7,"3":2}