from funciones import existe_tlf
import pytest

def test_existe_tlf():
    assert existe_tlf({"Pedro": "123456789", "Lucia": "123456123"}, "123456789") == True
    assert existe_tlf({"Pedro": "123456789", "Lucia": "123456123"}, "987654321") == False