import pytest
from funciones import pulsaciones

def test_pulsaciones():
    assert pulsaciones("Hola") == {"H":44,"O":6666,"L":555,"A":2}