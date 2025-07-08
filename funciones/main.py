# main.py

from funciones import saludar, sumar

def main():
    # Llamadas a las funciones principales
    nombre = input("Ingresa tu nombre: ")
    print(saludar(nombre))

    a = int(input("Ingresa el primer número para sumar: "))
    b = int(input("Ingresa el segundo número para sumar: "))
    print(f"La suma de {a} + {b} es: {sumar(a, b)}")

if __name__ == "__main__":
    main()
