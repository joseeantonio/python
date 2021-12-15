import pytest
from funciones_4_2 import billete

def test_billete ():
    assert billete(401,8) == 5614
    assert billete(100,5) == 2000