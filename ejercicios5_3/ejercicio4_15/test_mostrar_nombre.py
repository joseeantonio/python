from funciones import mostrar_nombre
import pytest

def test_mostrar_nombre():
    assert mostrar_nombre({"Juan":"123456789","Maria":"987654321"},"987654321") == "Maria"
    assert mostrar_nombre({"Juan": "123456789", "Maria": "987654321"},"123467890") == None