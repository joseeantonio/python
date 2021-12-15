from funciones_4_2 import alturas_alumnos

def test_alturas_alumnos():
    assert alturas_alumnos((1.80,1.40,1.60))==(1,0,1,1)