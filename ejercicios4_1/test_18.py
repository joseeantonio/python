import pytest
from funciones import factores

def test_factores():
    assert factores(36)==['2*18', ', 3*12', ', 4*9', ', 6*6', ', 9*4', ', 12*3', ', 18*2']
    assert factores(50)==['2*25', ', 5*10', ', 10*5', ', 25*2']