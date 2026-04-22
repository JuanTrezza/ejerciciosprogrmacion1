import math
import random
import time


def pedir_entero(mensaje, minimo=None, maximo=None):
    while True:
        try:
            valor = int(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            if maximo is not None and valor > maximo:
                print(f"El valor debe ser menor o igual a {maximo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un numero entero valido.")


def pedir_flotante(mensaje, minimo=None):
    while True:
        try:
            valor = float(input(mensaje))
            if minimo is not None and valor < minimo:
                print(f"El valor debe ser mayor o igual a {minimo}.")
                continue
            return valor
        except ValueError:
            print("Ingresa un numero valido.")


def ejercicio_1_adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("Adivina el numero secreto entre 1 y 100.")

    while True:
        intento = pedir_entero("Ingresa tu intento: ", 1, 100)
        intentos += 1

        diferencia = abs(intento - numero_secreto)
        if intento < numero_secreto:
            direccion = "mayor"
        elif intento > numero_secreto:
            direccion = "menor"
        else:
            print(f"Correcto. Numero secreto: {numero_secreto}. Intentos: {intentos}.")
            break

        if diferencia >= 40:
            cercania = "muy lejos"
        elif diferencia >= 20:
            cercania = "lejos"
        elif diferencia >= 10:
            cercania = "cerca"
        else:
            cercania = "muy cerca"

        print(f"No es correcto. Estas {cercania}. El numero es {direccion}.")


def ejercicio_2_tareas_pendientes():
    tareas = []

    while True:
        print("\nGestor de tareas")
        print("1. Agregar tarea")
        print("2. Marcar tarea como completada")
        print("3. Mostrar tareas")
        print("4. Volver al menu principal")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            tarea = input("Descripcion de la tarea: ").strip()
            if tarea:
                tareas.append({"tarea": tarea, "completada": False})
                print("Tarea agregada.")
            else:
                print("La tarea no puede estar vacia.")
        elif opcion == "2":
            if not tareas:
                print("No hay tareas cargadas.")
                continue

            for indice, tarea in enumerate(tareas, start=1):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{indice}. {tarea['tarea']} - {estado}")

            indice_tarea = pedir_entero("Numero de tarea completada: ", 1, len(tareas)) - 1
            tareas[indice_tarea]["completada"] = True
            print("Tarea actualizada.")
        elif opcion == "3":
            if not tareas:
                print("No hay tareas cargadas.")
            else:
                for indice, tarea in enumerate(tareas, start=1):
                    estado = "Completada" if tarea["completada"] else "Pendiente"
                    print(f"{indice}. {tarea['tarea']} - {estado}")
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")


def ejercicio_3_calculadora_propina():
    total_cuenta = pedir_flotante("Ingresa el total de la cuenta: $", 0)
    for porcentaje in (15, 18, 20):
        propina = total_cuenta * porcentaje / 100
        total = total_cuenta + propina
        print(f"Propina {porcentaje}%: ${propina:.2f} | Total: ${total:.2f}")


def ejercicio_4_carrera_autos():
    competidores = {
        "Franco Colapinto": 0,
        "Liam Lawson": 0,
        "Charles Leclerc": 0,
        "Sergio Perez": 0,
        "Max Verstappen": 0,
    }
    meta = 100
    ronda = 1

    print("Carrera de autos. Meta: 100 unidades.")

    while True:
        print(f"\nRonda {ronda}")
        for competidor in competidores:
            avance = random.randint(5, 15)
            competidores[competidor] += avance
            print(f"{competidor}: +{avance} -> {competidores[competidor]}")

            if competidores[competidor] >= meta:
                print(f"Ganador: {competidor}")
                return

        ronda += 1
        time.sleep(0.5)


def ejercicio_5_gestor_inventario():
    inventario = {}

    while True:
        print("\nGestor de inventario")
        print("1. Agregar producto")
        print("2. Actualizar stock")
        print("3. Mostrar inventario")
        print("4. Volver al menu principal")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            producto = input("Nombre del producto: ").strip()
            if not producto:
                print("El nombre no puede estar vacio.")
                continue
            cantidad = pedir_entero("Cantidad inicial: ", 0)
            inventario[producto] = cantidad
            print("Producto agregado.")
        elif opcion == "2":
            producto = input("Producto a actualizar: ").strip()
            if producto not in inventario:
                print("El producto no existe en el inventario.")
                continue
            cantidad = pedir_entero("Nueva cantidad: ", 0)
            inventario[producto] = cantidad
            print("Stock actualizado.")
        elif opcion == "3":
            if not inventario:
                print("Inventario vacio.")
            else:
                for producto, cantidad in inventario.items():
                    print(f"{producto}: {cantidad}")
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")


def ejercicio_6_area_y_perimetro():
    while True:
        print("\nArea y perimetro")
        print("1. Circulo")
        print("2. Cuadrado")
        print("3. Triangulo")
        print("4. Volver al menu principal")

        opcion = input("Elige una opcion: ").strip()

        if opcion == "1":
            radio = pedir_flotante("Radio del circulo: ", 0)
            area = math.pi * radio**2
            perimetro = 2 * math.pi * radio
            print(f"Area: {area:.2f} | Perimetro: {perimetro:.2f}")
        elif opcion == "2":
            lado = pedir_flotante("Lado del cuadrado: ", 0)
            area = lado**2
            perimetro = 4 * lado
            print(f"Area: {area:.2f} | Perimetro: {perimetro:.2f}")
        elif opcion == "3":
            base = pedir_flotante("Base del triangulo: ", 0)
            altura = pedir_flotante("Altura del triangulo: ", 0)
            lado_1 = pedir_flotante("Lado 1: ", 0)
            lado_2 = pedir_flotante("Lado 2: ", 0)
            lado_3 = pedir_flotante("Lado 3: ", 0)
            area = 0.5 * base * altura
            perimetro = lado_1 + lado_2 + lado_3
            print(f"Area: {area:.2f} | Perimetro: {perimetro:.2f}")
        elif opcion == "4":
            break
        else:
            print("Opcion invalida.")


def ejercicio_7_contador_caracter():
    frase = input("Ingresa una frase: ")
    caracter = input("Ingresa un caracter a buscar: ")

    if not caracter:
        print("No ingresaste ningun caracter.")
        return

    buscado = caracter[0]
    cantidad = 0
    for indice in range(len(frase)):
        if frase[indice] == buscado:
            cantidad += 1

    print(f"El caracter '{buscado}' aparece {cantidad} veces.")


def ejercicio_8_detector_palindromo():
    palabra = input("Ingresa una palabra: ").replace(" ", "").lower()

    es_palindromo = True
    for indice in range(len(palabra) // 2):
        if palabra[indice] != palabra[-(indice + 1)]:
            es_palindromo = False
            break

    if es_palindromo:
        print(f"'{palabra}' es un palindromo.")
    else:
        print(f"'{palabra}' no es un palindromo.")


TITULOS_EJERCICIOS = {
    "1": "Adivinar numero secreto",
    "2": "Lista de tareas pendientes",
    "3": "Calculadora de propinas",
    "4": "Simulador de carrera de autos",
    "5": "Gestor de inventario",
    "6": "Area y perimetro de figuras",
    "7": "Contador de un caracter en frase",
    "8": "Detector de palindromos",
}


EJERCICIOS = {
    "1": ejercicio_1_adivinar_numero,
    "2": ejercicio_2_tareas_pendientes,
    "3": ejercicio_3_calculadora_propina,
    "4": ejercicio_4_carrera_autos,
    "5": ejercicio_5_gestor_inventario,
    "6": ejercicio_6_area_y_perimetro,
    "7": ejercicio_7_contador_caracter,
    "8": ejercicio_8_detector_palindromo,
}


def main():
    print("Unidad 5 - Ejercicios resueltos")
    while True:
        print("\nMenu principal")
        for numero, titulo in TITULOS_EJERCICIOS.items():
            print(f"{numero}. {titulo}")
        print("0. Salir")

        opcion = input("Elige un ejercicio: ").strip()

        if opcion == "0":
            print("Fin de la Unidad 5.")
            break

        if opcion in EJERCICIOS:
            print(f"\nEjercicio {opcion}: {TITULOS_EJERCICIOS[opcion]}")
            EJERCICIOS[opcion]()
        else:
            print("Opcion invalida. Ingresa un numero del 0 al 8.")


if __name__ == "__main__":
    main()