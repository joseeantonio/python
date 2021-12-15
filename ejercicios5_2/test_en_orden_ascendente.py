import pytest
from funciones import en_orden_ascendente

def test_en_orden_ascendente():
    assert en_orden_ascendente([1,2,4,5]) == True
    assert en_orden_ascendente([1,2,4,5,3,6]) == False