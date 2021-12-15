import pytest
from funciones import eliminar_extremos

def test_eliminar_extremos():
    assert eliminar_extremos([2, 3, 4, 1, 8, 7, 6, 5]) == [3, 4, 1, 8, 7, 6]