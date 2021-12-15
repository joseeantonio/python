from funciones_5_1 import validar_contra

def test_validar_contra():
    assert validar_contra("1wFffffhgede")==True
    assert validar_contra("2whdfcrhjgferc")==False