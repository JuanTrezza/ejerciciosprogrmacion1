"""
EJERCICIO 6 — Conversor de Unidades con Módulo
################################################

Desarrollá un programa que convierta unidades de distancia y peso.

El programa debe mostrar un menú al usuario y permitirle elegir qué conversión
realizar. Debe seguir mostrando el menú hasta que el usuario elija salir.

Menú:
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir

Fórmulas:
    - 1 kilómetro = 0.621371 millas
    - 1 kilogramo = 2.20462 libras

Requisitos:
- Las funciones de conversión deben estar en un módulo separado llamado `conversiones.py`.
- Cada función debe tener un docstring de una línea que explique qué hace.
  Ver formato: https://peps.python.org/pep-0257/#one-line-docstrings
- El menú y la lógica principal deben estar en este archivo (ejercicio_06.py).
- Si el usuario ingresa una opción inválida, mostrar "Opción no válida. Intente nuevamente."
- Validar que el valor ingresado para convertir sea un número positivo.

Ejemplo de ejecución:

    ¿Qué desea convertir?
    1. Kilómetros a Millas
    2. Kilogramos a Libras
    3. Salir
    Ingrese una opción: 1
    Ingrese los kilómetros: 10
    10 km = 6.21 millas

    Ingrese una opción: 2
    Ingrese los kilogramos: 70
    70 kg = 154.32 libras

    Ingrese una opción: 3
    ¡Hasta luego!

Mostrá los resultados redondeados a 2 decimales (por ejemplo, `f"{valor:.2f}"`).

"""

from conversiones import kilogramos_a_libras, kilometros_a_millas


def pedir_numero_positivo(mensaje):
    while True:
        entrada = input(mensaje)
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("El valor debe ser un numero positivo.")
        except ValueError:
            print("Entrada invalida. Ingrese un numero.")


def mostrar_menu():
    print("\nQue desea convertir?")
    print("1. Kilometros a Millas")
    print("2. Kilogramos a Libras")
    print("3. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion: ")

        if opcion == "1":
            kilometros = pedir_numero_positivo("Ingrese los kilometros: ")
            millas = kilometros_a_millas(kilometros)
            print(f"{kilometros:g} km = {millas:.2f} millas")
        elif opcion == "2":
            kilogramos = pedir_numero_positivo("Ingrese los kilogramos: ")
            libras = kilogramos_a_libras(kilogramos)
            print(f"{kilogramos:g} kg = {libras:.2f} libras")
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()










