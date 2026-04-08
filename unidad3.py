def ejercicio_1():
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Hola, {nombre}. Tienes {edad} años.")


def ejercicio_2():
    print("Figura 1:")
    print("+***************+")
    print("*               *")
    print("*               *")
    print("*               *")
    print("+***************+")

    print("\nFigura 2:")
    print("+---+")
    print("|   |")
    print("|   |")
    print("|   |")
    print("+---+")

    print("\nFigura 3:")
    print("###################################")
    print("###################################")
    print("##                               ##")
    print("##                               ##")
    print("##                               ##")
    print("###################################")
    print("###################################")


def ejercicio_3():
    numero1 = int(input("Ingresa el primer numero entero: "))
    numero2 = int(input("Ingresa el segundo numero entero: "))

    if numero2 == 0:
        print("No se puede dividir por cero.")
        return

    resultado = float(numero1) / float(numero2)
    print(f"El resultado de la division es: {resultado}")


def ejercicio_4():
    cadena_numero = input("Ingresa un numero entero como texto: ")
    numero_entero = int(cadena_numero)
    resultado = numero_entero + 10
    print(f"Resultado: {resultado}")


def ejercicio_5():
    numero = float(input("Ingresa un numero: "))

    if numero > 10:
        print("El numero es mayor que 10")
    elif numero == 10:
        print("El numero es igual a 10")
    else:
        print("El numero es menor que 10")


def ejercicio_6():
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))

    if numero1 == numero2:
        print("Los numeros son iguales")
    else:
        print("Los numeros son diferentes")


def ejercicio_7():
    edad = int(input("Ingresa tu edad: "))

    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")


def ejercicio_8():
    temperatura_celsius = float(input("Ingresa una temperatura en Celsius: "))

    if temperatura_celsius >= 100:
        print("El agua esta hirviendo")
    elif temperatura_celsius <= 0:
        print("El agua esta congelada")
    else:
        print("El agua esta en estado liquido")


def ejercicio_9():
    numero = float(input("Ingresa un numero: "))

    if numero > 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es negativo")
    else:
        print("El numero es cero")


def ejercicio_10():
    numero_dia = int(input("Ingresa un numero del 1 al 7: "))

    if numero_dia == 1:
        print("Lunes")
    elif numero_dia == 2:
        print("Martes")
    elif numero_dia == 3:
        print("Miercoles")
    elif numero_dia == 4:
        print("Jueves")
    elif numero_dia == 5:
        print("Viernes")
    elif numero_dia == 6:
        print("Sabado")
    elif numero_dia == 7:
        print("Domingo")
    else:
        print("Numero de dia no valido")


def ejercicio_11():
    numero1 = float(input("Ingresa el primer numero: "))
    numero2 = float(input("Ingresa el segundo numero: "))

    print(f"Suma: {numero1 + numero2}")
    print(f"Resta: {numero1 - numero2}")
    print(f"Multiplicacion: {numero1 * numero2}")

    if numero2 != 0:
        print(f"Division: {numero1 / numero2}")
    else:
        print("Division: No se puede dividir por cero")


def ejercicio_12():
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))

    if altura <= 0:
        print("La altura debe ser mayor que cero.")
        return

    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

    if imc < 18.5:
        print("Bajo peso")
    elif imc < 25:
        print("Peso normal")
    elif imc < 30:
        print("Sobrepeso")
    else:
        print("Obesidad")


def ejercicio_13():
    temperatura_celsius = float(input("Ingresa la temperatura en Celsius: "))
    temperatura_fahrenheit = (temperatura_celsius * 9 / 5) + 32
    print(f"La temperatura en Fahrenheit es: {temperatura_fahrenheit:.2f}")


def ejercicio_14():
    numero_objetivo = 7
    adivinanza = int(input("Adivina un numero entre 1 y 10: "))

    if adivinanza == numero_objetivo:
        print("Correcto, adivinaste el numero.")
    elif adivinanza < numero_objetivo:
        print("Incorrecto. El numero es mayor.")
    else:
        print("Incorrecto. El numero es menor.")


def ejercicio_15():
    entrada = input("Ingresa un dato: ").strip()

    if entrada.startswith("-") and entrada[1:].isdigit():
        print("El dato representa un numero entero negativo")
    elif entrada.isdigit():
        print("El dato representa un numero entero")
    elif entrada.count(".") == 1:
        izquierda, derecha = entrada.split(".")
        if izquierda.startswith("-"):
            izquierda = izquierda[1:]
        if izquierda.isdigit() and derecha.isdigit():
            print("El dato representa un numero flotante")
        else:
            print("El dato representa una cadena de texto")
    else:
        print("El dato representa una cadena de texto")


def ejercicio_16():
    nota1 = float(input("Ingresa la calificacion de la materia 1: "))
    nota2 = float(input("Ingresa la calificacion de la materia 2: "))
    nota3 = float(input("Ingresa la calificacion de la materia 3: "))

    promedio = (nota1 + nota2 + nota3) / 3
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 6:
        print("Aprobado")
    else:
        print("Desaprobado")


def ejercicio_17():
    nombre = input("Ingresa tu nombre: ")
    color = input("Ingresa tu color favorito: ")
    print(f"Hola {nombre}, tu color favorito es {color}")


TITULOS_EJERCICIOS = {
    "1": "Saludo con nombre y edad",
    "2": "Impresion de figuras geometricas",
    "3": "Division entre enteros convertidos a float",
    "4": "Conversion de cadena a entero y suma",
    "5": "Comparacion con el numero 10",
    "6": "Comparacion de dos numeros",
    "7": "Mayor o menor de edad",
    "8": "Estado del agua segun temperatura",
    "9": "Numero positivo, negativo o cero",
    "10": "Dia de la semana segun numero",
    "11": "Calculadora basica",
    "12": "Calculador de IMC",
    "13": "Conversion de Celsius a Fahrenheit",
    "14": "Juego de adivinanza",
    "15": "Identificacion del tipo de dato",
    "16": "Promedio de tres calificaciones",
    "17": "Concatenacion de strings",
}


EJERCICIOS = {
    "1": ejercicio_1,
    "2": ejercicio_2,
    "3": ejercicio_3,
    "4": ejercicio_4,
    "5": ejercicio_5,
    "6": ejercicio_6,
    "7": ejercicio_7,
    "8": ejercicio_8,
    "9": ejercicio_9,
    "10": ejercicio_10,
    "11": ejercicio_11,
    "12": ejercicio_12,
    "13": ejercicio_13,
    "14": ejercicio_14,
    "15": ejercicio_15,
    "16": ejercicio_16,
    "17": ejercicio_17,
}


def main():
    print("Unidad 3 - Ejercicios resueltos")
    for numero, titulo in TITULOS_EJERCICIOS.items():
        print(f"{numero}. {titulo}")

    opcion = input("\nIngresa el numero del ejercicio que quieres ejecutar: ")

    if opcion in EJERCICIOS:
        print(f"\nEjercicio {opcion}: {TITULOS_EJERCICIOS[opcion]}")
        EJERCICIOS[opcion]()
    else:
        print("Opcion invalida. Ingresa un numero del 1 al 17.")


if __name__ == "__main__":
    main()
