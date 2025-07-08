# test_funciones.py

from funciones import saludar, sumar

# ===== Pruebas para saludar =====
assert saludar("Jimmy") == "¡Hola, Jimmy! ¡Qué bueno tenerte aquí!", "Error en saludo para Jimmy"
assert saludar("Ana") == "¡Hola, Ana! ¡Qué bueno tenerte aquí!", "Error en saludo para Ana"

# ===== Pruebas para sumar =====
assert sumar(5, 5) == 10, "Error en suma 5 + 5"
assert sumar(-2, 2) == 0, "Error en suma -2 + 2"

print("✅ Todas las pruebas pasaron exitosamente.")

# ⚠️ Puedes ejecutar este archivo directamente para validar que todo funciona.