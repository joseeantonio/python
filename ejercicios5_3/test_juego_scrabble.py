import pytest
from funciones import juego_scrabble

def test_juego_scrabble():
    assert juego_scrabble("hola") == 7