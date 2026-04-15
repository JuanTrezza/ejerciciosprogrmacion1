import math


def ejercicio_1():
	print("El área del rectángulo es:", 5 * 3)


def ejercicio_2():
	celsius = float(input("Ingresa la temperatura en Celsius: "))
	fahrenheit = (celsius * 9 / 5) + 32
	print("La temperatura en Fahrenheit es:", fahrenheit)


def ejercicio_3():
	nombre = "Juan"
	edad = "25"
	informacion = nombre + " " + edad
	print(informacion)
	print("El tipo de dato de la variable informacion es:", type(informacion))


def ejercicio_4():
	radio = 4
	area_circulo = math.pi * radio ** 2
	print("El área del círculo es:", area_circulo)


def ejercicio_5():
	# OBSERVACION: la division no contempla el caso numero2 == 0.
	# El enunciado no lo exige, pero si el usuario ingresa 0 el programa
	# cortara con ZeroDivisionError. Conviene agregar una validacion.  --->> igual todavia no vimos manejo de errores, asi que lo dejamos asi por ahora.
	numero1 = float(input("Ingresa el primer número: "))
	numero2 = float(input("Ingresa el segundo número: "))

	suma = numero1 + numero2
	resta = numero1 - numero2
	multiplicacion = numero1 * numero2
	division = numero1 / numero2

	print("Suma:", suma)
	print("Resta:", resta)
	print("Multiplicación:", multiplicacion)
	print("División:", division)


def ejercicio_6():
	resultado = (5 + 3) * (10 - 2) / 4
	print("El resultado de la operación es:", resultado)
	print("El tipo de dato del resultado es:", type(resultado))


def ejercicio_7():
	alumno_aprobado = True
	print("¿El alumno ha aprobado el examen?", alumno_aprobado)


def ejercicio_8():
	perimetro_triangulo = 3 * 6
	print("El perímetro del triángulo equilátero es:", perimetro_triangulo)


def ejercicio_9():
	# OBSERVACION: al convertir edad con int(), se pierde la nocion de que
	# input() siempre devuelve str. Si el objetivo didactico del ejercicio es
	# mostrar los tipos de dato "crudos" que entrega input(), conviene dejar
	# edad como string. Si se quiere trabajar con numero, la conversion es valida.
	nombre = input("Ingresa tu nombre: ")
	edad = int(input("Ingresa tu edad: "))
	ciudad = input("Ingresa tu ciudad de residencia: ")

	print("Nombre:", nombre, "Tipo de dato:", type(nombre))
	print("Edad:", edad, "Tipo de dato:", type(edad))
	print("Ciudad:", ciudad, "Tipo de dato:", type(ciudad))


def ejercicio_10():
	operacion = (10 + 5) * 3 - 4
	print("El resultado de la operación es:", operacion)
	print("El tipo de dato del resultado es:", type(operacion))


TITULOS_EJERCICIOS = {
	"1": "Area de un rectangulo",
	"2": "Conversion de Celsius a Fahrenheit",
	"3": "Concatenacion de nombre y edad",
	"4": "Area de un circulo",
	"5": "Operaciones basicas entre dos numeros",
	"6": "Operacion compuesta y tipo de dato",
	"7": "Variable booleana de aprobado",
	"8": "Perimetro de triangulo equilatero",
	"9": "Ingreso de datos personales y tipos",
	"10": "Operacion aritmetica y tipo de dato",
}


ejercicios = {
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
}


def main():
	print("Unidad 2 - Ejercicios resueltos")
	for numero, titulo in TITULOS_EJERCICIOS.items():
		print(f"{numero}. {titulo}")

	opcion = input("Ingresa el número del ejercicio que quieres ejecutar: ")

	if opcion in ejercicios:
		print(f"\nEjercicio {opcion}: {TITULOS_EJERCICIOS[opcion]}")
		ejercicios[opcion]()
	else:
		print("Opción inválida. Debes ingresar un número del 1 al 10.")


if __name__ == "__main__":
	main()