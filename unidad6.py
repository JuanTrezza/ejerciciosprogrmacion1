# ==============================
# GUIA DE EJERCICIOS - UNIDAD 6
# ==============================


# Ejercicio 1: Calculadora simple
# Consigna:
# Crear funciones para sumar, restar, multiplicar y dividir dos numeros
# (enteros o flotantes). Permitir que el usuario elija la operacion.
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir por cero"
    return a / b


# Ejercicio 2: Factorial de un numero
# Consigna:
# Escribir una funcion que calcule el factorial de un numero entero dado.
def factorial(n):
    if n < 0:
        return "El factorial no esta definido para numeros negativos."
    if n == 0 or n == 1:
        return 1

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Ejercicio 3: Comprobacion de numero primo
# Consigna:
# Definir una funcion que verifique si un numero entero dado es primo o no.
def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


# Ejercicio 4: Calculo de potencia
# Consigna:
# Crear una funcion que calcule la potencia de una base entera elevada
# a un exponente entero.
def potencia(base, exponente):
    return base ** exponente


# Ejercicio 5: Contador de caracteres
# Consigna:
# Escribir una funcion que reciba una cadena y devuelva la cantidad
# de caracteres que contiene.
def contar_caracteres(cadena):
    return len(cadena)


# Ejercicio 6: Reversion de cadena
# Consigna:
# Definir una funcion que invierta una cadena dada.
def invertir_cadena(cadena):
    return cadena[::-1]


# Ejercicio 7: Secuencia Fibonacci
# Consigna:
# Crear una funcion que genere los primeros n terminos de la
# secuencia de Fibonacci.
def fibonacci(n):
    if n < 0:
        return []

    secuencia = []
    a, b = 0, 1
    for _ in range(n):
        secuencia.append(a)
        a, b = b, a + b
    return secuencia


# Ejercicio 8: Ficha de alumno (clave-valor)
# Consigna:
# Crear una funcion que reciba datos de un alumno por clave-valor.
# Debe aceptar: nombre, apellido, carrera, fecha_nacimiento, email y turno.
# Mostrar una ficha con los datos recibidos; si falta alguno, mostrar
# "sin valor" en ese campo.
def datos_alumno(**datos):
    campos = ["nombre", "apellido", "carrera", "fecha_nacimiento", "email", "turno"]

    print("----- Ficha del Alumno -----")
    for campo in campos:
        print(f"{campo.capitalize()}: {datos.get(campo, 'sin valor')}")


# Ejercicio 9: Funcion con operacion variable y n parametros
# Consigna:
# Crear una funcion que reciba n parametros:
# - El primer parametro solo puede ser "sumar" o "multiplicar".
# - Los parametros restantes deben ser numeros.
# Si algun valor no es numerico, avisar y cortar la ejecucion.
# Si todos son validos, devolver la suma o multiplicacion segun corresponda.
def operar(*args):
    if len(args) < 2:
        return "Error: faltan parametros"

    operacion = args[0]
    numeros = args[1:]

    if operacion not in ["sumar", "multiplicar"]:
        return "Error: operacion invalida"

    for valor in numeros:
        if not isinstance(valor, (int, float)):
            return f"Error: {valor} no es un numero"

    if operacion == "sumar":
        resultado = 0
        for numero in numeros:
            resultado += numero
        return resultado

    resultado = 1
    for numero in numeros:
        resultado *= numero
    return resultado


# Ejercicio 10: Verificador de palindromos
# Consigna:
# Crear una funcion que determine si una cadena es un palindromo,
# es decir, si se lee igual de izquierda a derecha y viceversa.
def es_palindromo(cadena):
    texto_limpio = cadena.lower().replace(" ", "")
    return texto_limpio == texto_limpio[::-1]


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero entero.")


def pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Entrada invalida. Debe ingresar un numero.")


def ejecutar_ejercicio_1():
    num1 = pedir_flotante("Ingrese el primer numero: ")
    num2 = pedir_flotante("Ingrese el segundo numero: ")

    print("Operaciones:")
    print("1 - Sumar")
    print("2 - Restar")
    print("3 - Multiplicar")
    print("4 - Dividir")

    opcion = input("Elija una opcion: ").strip()
    if opcion == "1":
        print("Resultado:", sumar(num1, num2))
    elif opcion == "2":
        print("Resultado:", restar(num1, num2))
    elif opcion == "3":
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == "4":
        print("Resultado:", dividir(num1, num2))
    else:
        print("Opcion invalida")


def ejecutar_ejercicio_2():
    numero = pedir_entero("Ingrese un numero entero para calcular su factorial: ")
    print("El factorial de", numero, "es:", factorial(numero))


def ejecutar_ejercicio_3():
    numero = pedir_entero("Ingrese un numero entero para verificar si es primo: ")
    if es_primo(numero):
        print(numero, "es un numero primo.")
    else:
        print(numero, "no es un numero primo.")


def ejecutar_ejercicio_4():
    base = pedir_entero("Ingrese la base (entero): ")
    exponente = pedir_entero("Ingrese el exponente (entero): ")
    print(base, "elevado a la", exponente, "es:", potencia(base, exponente))


def ejecutar_ejercicio_5():
    texto = input("Ingrese una cadena de texto: ")
    print("La cantidad de caracteres en la cadena es:", contar_caracteres(texto))


def ejecutar_ejercicio_6():
    texto = input("Ingrese una cadena de texto: ")
    print("La cadena invertida es:", invertir_cadena(texto))


def ejecutar_ejercicio_7():
    n = pedir_entero("Ingrese la cantidad de terminos de Fibonacci: ")
    print("Los primeros", n, "terminos de Fibonacci son:", fibonacci(n))


def ejecutar_ejercicio_8():
    print("Complete los datos del alumno (puede dejar vacio cualquier campo):")
    datos = {
        "nombre": input("Nombre: ").strip(),
        "apellido": input("Apellido: ").strip(),
        "carrera": input("Carrera: ").strip(),
        "fecha_nacimiento": input("Fecha de nacimiento: ").strip(),
        "email": input("Email: ").strip(),
        "turno": input("Turno: ").strip(),
    }

    datos_limpios = {k: v for k, v in datos.items() if v != ""}
    datos_alumno(**datos_limpios)


def ejecutar_ejercicio_9():
    print("Ingrese la operacion (sumar o multiplicar):")
    operacion = input("Operacion: ").strip().lower()
    cantidad = pedir_entero("Cuantos numeros desea ingresar?: ")

    if cantidad <= 0:
        print("Debe ingresar al menos un numero.")
        return

    numeros = []
    for i in range(cantidad):
        numero = pedir_flotante(f"Numero {i + 1}: ")
        numeros.append(numero)

    print("Resultado:", operar(operacion, *numeros))


def ejecutar_ejercicio_10():
    texto = input("Ingrese una cadena de texto: ")
    if es_palindromo(texto):
        print("La cadena es un palindromo.")
    else:
        print("La cadena no es un palindromo.")


def mostrar_menu():
    print("\n===== UNIDAD 6 - MENU DE EJERCICIOS =====")
    print("1. Calculadora simple")
    print("2. Factorial")
    print("3. Numero primo")
    print("4. Potencia")
    print("5. Contador de caracteres")
    print("6. Reversion de cadena")
    print("7. Fibonacci")
    print("8. Ficha de alumno")
    print("9. Operacion con n parametros")
    print("10. Palindromos")
    print("0. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione un ejercicio: ").strip()

        if opcion == "1":
            ejecutar_ejercicio_1()
        elif opcion == "2":
            ejecutar_ejercicio_2()
        elif opcion == "3":
            ejecutar_ejercicio_3()
        elif opcion == "4":
            ejecutar_ejercicio_4()
        elif opcion == "5":
            ejecutar_ejercicio_5()
        elif opcion == "6":
            ejecutar_ejercicio_6()
        elif opcion == "7":
            ejecutar_ejercicio_7()
        elif opcion == "8":
            ejecutar_ejercicio_8()
        elif opcion == "9":
            ejecutar_ejercicio_9()
        elif opcion == "10":
            ejecutar_ejercicio_10()
        elif opcion == "0":
            print("Fin de la practica de Unidad 6.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


if __name__ == "__main__":
    main()
