import pytest
from funciones import esta_ordenada

def test_esta_ordenada():
    assert esta_ordenada([1,4,6,8,9])==True
    assert esta_ordenada([9,6,4,2,1])==True
    assert esta_ordenada([1,4,3,6,8,9])== False