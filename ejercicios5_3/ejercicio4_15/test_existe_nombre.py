from funciones import existe_nombre
import pytest

def test_existe_nombre():
    assert existe_nombre({"Juan":"123456354","Maria":"123456789"},"Juan")==True
    assert existe_nombre({"Juan": "123456354", "Maria": "123456789"}, "Peri") == False