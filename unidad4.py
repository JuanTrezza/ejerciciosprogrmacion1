import math


def pedir_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un numero entero valido.")


def pedir_flotante(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Por favor, ingresa un numero valido.")


def ejercicio_1():
    referencial_minimo = 20
    referencial_maximo = 500

    numero = pedir_entero("Ingrese un numero: ")

    if numero < referencial_minimo:
        print("VALOR BAJO")
    elif numero > referencial_maximo:
        print("VALOR ALTO")
    else:
        print("VALOR MEDIO")


def ejercicio_2():
    anio = pedir_entero("Ingrese un año: ")

    if (anio % 4 == 0 and anio % 100 != 0) or anio % 400 == 0:
        print(f"El año {anio} es bisiesto.")
    else:
        print(f"El año {anio} no es bisiesto.")


def ejercicio_3():
    while True:
        inicio = pedir_entero("Ingrese un numero de inicio del bucle: ")
        fin = pedir_entero("Ingrese un numero de fin del bucle: ")

        if inicio < fin:
            break

        print("El numero de inicio debe ser menor al numero de fin.")

    for numero in range(inicio, fin + 1):
        print(f"Este es el bucle numero {numero}")

    print("---")
    print("Fin del programa.")


def ejercicio_4():
    notas = []

    for indice in range(1, 5):
        nota = pedir_flotante(f"Ingrese la nota del examen {indice}: ")
        notas.append(nota)

    promedio = sum(notas) / len(notas)
    print(f"Promedio: {promedio:.2f}")

    if promedio >= 6:
        print("El alumno tiene aprobada la cursada.")
        nota_final = pedir_flotante("Ingrese la nota del examen final: ")

        if nota_final >= 6:
            print("El alumno aprobo la materia.")
        else:
            print("El alumno no aprobo el final de la materia y puede rendir recuperatorio.")
    else:
        print("El alumno no tiene aprobada la cursada.")


def ejercicio_5():
    print("ECUACION A X + B = 0")
    coeficiente_a = pedir_flotante("Escriba el valor del coeficiente a: ")
    coeficiente_b = pedir_flotante("Escriba el valor del coeficiente b: ")

    if coeficiente_a != 0:
        solucion = -coeficiente_b / coeficiente_a
        print(f"La ecuacion tiene una solucion: {solucion}")
    elif coeficiente_b != 0:
        print("La ecuacion no tiene solucion.")
    else:
        print("Todos los numeros son solucion.")


def ejercicio_6():
    print("ECUACION A X^2 + B X + C = 0")
    coeficiente_a = pedir_flotante("Escriba el valor del coeficiente a: ")
    coeficiente_b = pedir_flotante("Escriba el valor del coeficiente b: ")
    coeficiente_c = pedir_flotante("Escriba el valor del coeficiente c: ")

    if coeficiente_a == 0:
        if coeficiente_b == 0:
            if coeficiente_c == 0:
                print("Todos los numeros son solucion.")
            else:
                print("Sin solucion.")
        else:
            solucion = -coeficiente_c / coeficiente_b
            print(f"Una solucion: {solucion}")
        return

    discriminante = coeficiente_b ** 2 - 4 * coeficiente_a * coeficiente_c

    if discriminante > 0:
        solucion_1 = (-coeficiente_b + math.sqrt(discriminante)) / (2 * coeficiente_a)
        solucion_2 = (-coeficiente_b - math.sqrt(discriminante)) / (2 * coeficiente_a)
        print(f"Dos soluciones: {solucion_1} y {solucion_2}")
    elif discriminante == 0:
        solucion = -coeficiente_b / (2 * coeficiente_a)
        print(f"Una solucion: {solucion}")
    else:
        print("Sin solucion real.")


def ejercicio_7():
    opcion = input(
        "Desea calcular el area de un triangulo o de un circulo? "
        "(T para triangulo, C para circulo): "
    ).strip().lower()

    if opcion == "t":
        base = pedir_flotante("Ingrese la base del triangulo: ")
        altura = pedir_flotante("Ingrese la altura del triangulo: ")
        area_triangulo = (base * altura) / 2
        print(f"El area del triangulo es: {area_triangulo}")
    elif opcion == "c":
        radio = pedir_flotante("Ingrese el radio del circulo: ")
        area_circulo = 3.141592 * (radio ** 2)
        print(f"El area del circulo es: {area_circulo}")
    else:
        print("Opcion no valida. Ingresa T para triangulo o C para circulo.")


def ejercicio_8():
    numero_1 = pedir_flotante("Ingrese el primer numero: ")
    numero_2 = pedir_flotante("Ingrese el segundo numero: ")
    numero_3 = pedir_flotante("Ingrese el tercer numero: ")

    distancia_al_primero = abs(numero_3 - numero_1)
    distancia_al_segundo = abs(numero_3 - numero_2)

    if distancia_al_primero < distancia_al_segundo:
        print("El tercer numero esta mas cerca del primero.")
    elif distancia_al_primero > distancia_al_segundo:
        print("El tercer numero esta mas cerca del segundo.")
    else:
        print("El tercer numero esta a la misma distancia del primero y del segundo.")


TITULOS_EJERCICIOS = {
    "1": "Valor bajo, medio o alto",
    "2": "Año bisiesto",
    "3": "Bucle entre inicio y fin",
    "4": "Promedio del cuatrimestre",
    "5": "Ecuacion de primer grado",
    "6": "Ecuacion de segundo grado",
    "7": "Area de triangulo o circulo",
    "8": "Cercania entre tres numeros",
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
}


def main():
    print("Unidad 4 - Ejercicios resueltos")
    for numero, titulo in TITULOS_EJERCICIOS.items():
        print(f"{numero}. {titulo}")

    opcion = input("\nIngresa el numero del ejercicio que quieres ejecutar: ").strip()

    if opcion in EJERCICIOS:
        print(f"\nEjercicio {opcion}: {TITULOS_EJERCICIOS[opcion]}")
        EJERCICIOS[opcion]()
    else:
        print("Opcion invalida. Ingresa un numero del 1 al 8.")


if __name__ == "__main__":
    main()
