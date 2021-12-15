import pytest
from funciones_4_2 import central

def test_central():
    assert central(1,2,3)==2
    assert central(2,1,3)==2
    assert central(3,1,2)==2