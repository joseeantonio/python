import pytest
from funciones import hay_duplicados

def test_hay_duplicados():
    assert hay_duplicados([1,3,5,4,1,2,9]) == True
    assert hay_duplicados([1,3,5,33,7,4]) == False