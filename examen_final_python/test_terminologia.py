from funciones import terminologia
import pytest

def test_terminologia():
    assert terminologia(4,6)=="eagle"
    assert terminologia(5,6) == "birdie"
    assert terminologia(6, 6) == "par"
    assert terminologia(7, 6) == "bogey"
    assert terminologia(8, 6) == "doble bogey"