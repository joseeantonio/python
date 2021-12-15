from funciones import existe_par
import pytest

def test_existe_par():
    assert existe_par({"1":3},"2")==False
    assert existe_par({"1":3},"1")==True