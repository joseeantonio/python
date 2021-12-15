from funciones import busqueda
import pytest

def test_busqueda():
    assert busqueda({"Juanito":"123456789","Lucia":"987654321","Maria":"123123123"},"filtra a") == {"Juanito":
                    "123456789","Lucia":"987654321","Maria":"123123123"}
    assert busqueda({"Juanito":"123456789","Lucia":"987654321","Maria":"123123123"},"filtra ia") == {"Lucia":"987654321"
        ,"Maria":"123123123"}