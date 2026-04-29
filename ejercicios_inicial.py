"""
Ejercicios iniciales de Python
Formato para correccion: cada ejercicio incluye consigna y respuesta.
"""


# --------------------------------------------------
# Ejercicio 1: Saludo personalizado
# Consigna:
# Crear una funcion saludar_usuario(nombre) que reciba un nombre
# como parametro y muestre un saludo personalizado.
# Respuesta:
def saludar_usuario(nombre):
    print(f"Hola, {nombre}!")


# --------------------------------------------------
# Ejercicio 2: Contador de letras
# Consigna:
# Crear una funcion contar_letras(palabra) que reciba una palabra
# y devuelva la cantidad de letras que tiene.
# Respuesta:
def contar_letras(palabra):
    return len(palabra)


# --------------------------------------------------
# Ejercicio 3: Mayor de edad
# Consigna:
# Crear una funcion es_mayor(edad) que reciba una edad y devuelva
# True si es mayor de edad (>= 18) o False en caso contrario.
# Respuesta:
def es_mayor(edad):
    return edad >= 18


# --------------------------------------------------
# Ejercicio 4: Validacion de contrasena simple
# Consigna:
# Crear una funcion verificar_contrasena(contrasena) que verifique
# si una contrasena tiene al menos 8 caracteres.
# Respuesta:
def verificar_contrasena(contrasena):
    return len(contrasena) >= 8


# --------------------------------------------------
# Ejercicio 5: Invertir palabra
# Consigna:
# Crear una funcion invertir_palabra(palabra) que reciba una palabra
# y devuelva la misma escrita al reves.
# Respuesta:
def invertir_palabra(palabra):
    return palabra[::-1]


# --------------------------------------------------
# Ejercicio 6: Contador de vocales
# Consigna:
# Crear una funcion contar_vocales(palabra) que cuente cuantas vocales
# contiene una palabra usando un bucle for.
# Respuesta:
def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador


# --------------------------------------------------
# Ejercicio 7: Menu de opciones
# Consigna:
# Crear una funcion mostrar_menu() que imprima un menu con tres opciones
# (por ejemplo: 1) Saludar, 2) Sumar numeros, 3) Salir).
# Respuesta:
def mostrar_menu():
    print("Menu de opciones:")
    print("1) Saludar")
    print("2) Sumar numeros")
    print("3) Salir")


# --------------------------------------------------
# Ejercicio 8: Repetir mensaje
# Consigna:
# Crear una funcion repetir_mensaje(mensaje, veces) que imprima un mensaje
# la cantidad de veces indicada usando un bucle for.
# Respuesta:
def repetir_mensaje(mensaje, veces):
    for _ in range(veces):
        print(mensaje)


# --------------------------------------------------
# Ejercicio 9: Encontrar palabra
# Consigna:
# Crear una funcion buscar_palabra(frase, palabra) que devuelva True
# si la palabra se encuentra en la frase, o False si no.
# Respuesta:
def buscar_palabra(frase, palabra):
    return palabra.lower() in frase.lower()


# --------------------------------------------------
# Ejercicio 10: Sumar numeros ingresados
# Consigna:
# Crear una funcion sumar_numeros() que pida al usuario ingresar 5 numeros
# y devuelva la suma total.
# Respuesta:
def sumar_numeros():
    total = 0
    for i in range(1, 6):
        numero = float(input(f"Ingrese el numero {i}: "))
        total += numero
    return total


def mostrar_demostracion():
    """Muestra ejemplos de salida para facilitar la correccion del profesor."""
    print("\n=== DEMOSTRACION DE EJERCICIOS ===")
    print("\nEjercicio 1:")
    saludar_usuario("Ana")

    print("\nEjercicio 2:", contar_letras("python"))
    print("Ejercicio 3:", es_mayor(20))
    print("Ejercicio 4:", verificar_contrasena("abc12345"))
    print("Ejercicio 5:", invertir_palabra("programar"))
    print("Ejercicio 6:", contar_vocales("murcielago"))

    print("\nEjercicio 7:")
    mostrar_menu()

    print("\nEjercicio 8:")
    repetir_mensaje("Hola profe", 2)

    print("\nEjercicio 9:", buscar_palabra("Me gusta Python", "python"))
    print("\nEjercicio 10: ejecutar manualmente llamando a sumar_numeros()")


if __name__ == "__main__":
    mostrar_demostracion()



