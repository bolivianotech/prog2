# test_funciones.py
from funciones import saludar, sumar

def test_saludar():
    assert saludar("Jimmy") == "¡Hola, Jimmy! ¡Qué bueno tenerte aquí!"
    assert saludar("Ana") == "¡Hola, Ana! ¡Qué bueno tenerte aquí!"

def test_sumar():
    assert sumar(3, 4) == 7
    assert sumar(-1, 1) == 0
    assert sumar(0, 0) == 0
