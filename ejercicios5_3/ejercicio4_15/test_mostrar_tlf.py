from funciones import mostrar_tlf
import pytest

def test_mostrar_tlf():
    assert mostrar_tlf({"Pedro":"123456789","Maria":"654839281"},"Pedro") == "123456789"
    assert mostrar_tlf({"Pedro": "123456789", "Maria": "654839281"}, "Juan") == None