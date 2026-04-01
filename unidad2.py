# 1. Calcula el área de un rectángulo con base 5 y altura 3. Imprime el resultado.

print ("El área del rectángulo es:", 5 * 3)

exit()

# 2. Convierte la temperatura de Celsius a Fahrenheit. Pide al usuario ingresar la temperatura en Celsius y luego imprime la temperatura equivalente en Fahrenheit.
celsius = float(input("Ingresa la temperatura en Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("La temperatura en Fahrenheit es:", fahrenheit)
exit()

# 3. Concatena tu nombre y tu edad como strings y guárdalos en una variable. Luego imprime el tipo de dato de esa variable.
nombre = "Juan"
edad = "25"
informacion = nombre + " " + edad
print(informacion)
print("El tipo de dato de la variable información es:", type(informacion))
exit()

# 4. Calcula el área de un círculo con radio 4. Imprime el resultado.
import math
radio = 4
area_circulo = math.pi * radio ** 2
print("El área del círculo es:", area_circulo)

exit()
# 5. Pide al usuario que ingrese dos números y muestra la suma, resta, multiplicación y división de esos números.

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

exit()

# 6. Almacena el resultado de una operación aritmética compleja en una variable y luego imprime tanto el resultado como el tipo de dato de esa variable.
resultado = (5 + 3) * (10 - 2) / 4
print("El resultado de la operación es:", resultado)
print("El tipo de dato del resultado es:", type(resultado))
exit()


# 7. Crea una variable booleana que represente si un alumno ha aprobado o no un examen y luego imprime su estado.
alumno_aprobado = True
print("¿El alumno ha aprobado el examen?", alumno_aprobado)
exit()

# 8. Calcula el perímetro de un triángulo equilátero con lados de longitud 6. Imprime el resultado.

perimetro_triangulo = 3 * 6
print("El perímetro del triángulo equilátero es:", perimetro_triangulo)
exit()

# 9. Pide al usuario que ingrese su nombre, edad y ciudad de residencia y luego imprime cada uno de esos datos con su respectivo tipo de dato.
input_nombre = input("Ingresa tu nombre: ")
input_edad = int(input("Ingresa tu edad: "))
input_ciudad = input("Ingresa tu ciudad de residencia: ")

print("Nombre:", input_nombre, "Tipo de dato:", type(input_nombre))
print("Edad:", input_edad, "Tipo de dato:", type(input_edad))
print("Ciudad:", input_ciudad, "Tipo de dato:", type(input_ciudad))
exit()

# 10. Realiza una operación matemática que involucre paréntesis, multiplicación, suma y resta. Guarda el resultado en una variable y luego imprímela junto con su tipo de dato.
operacion = (10 + 5) * 3 - 4
print("El resultado de la operación es:", operacion)
print("El tipo de dato del resultado es:", type(operacion))
exit()