from funciones import resultado_final
import pytest

def test_resultado_final():
    assert resultado_final({"1":4,"2":4},{"1":6,"2":6})=={"1":2,"2":2}
    assert resultado_final({"1": 4,}, {"1": 6, "2": 6}) == {"1": 2}