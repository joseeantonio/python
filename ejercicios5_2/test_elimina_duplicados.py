from funciones import elimina_duplicados
import pytest

def test_elimina_duplicados():
    assert elimina_duplicados([3,1,2,4,3,1]) == [1,3]
