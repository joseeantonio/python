from funciones import palindromos
import pytest

def test_palindromos():
    assert palindromos(["oso","eje","palabra"]) == ["oso","eje"]