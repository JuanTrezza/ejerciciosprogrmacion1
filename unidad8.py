"""
Unidad 8: Tuplas y diccionarios

Guia de ejercicios solo con consignas.
Este archivo esta en formato Python valido para evitar errores en el editor.
"""


# ============================================================
# EJERCICIOS SIMPLES
# ============================================================


# Ejercicio 1
# Crear una tupla llamada mis_datos con tu nombre, tu edad y tu ciudad.
# Luego, imprimir la tupla completa.


# ------------------------------------------------------------
# Ejercicio 2
# Dada la tupla colores = ("rojo", "verde", "azul"), imprimir:
# - el primer color usando un indice positivo
# - el ultimo color usando un indice negativo


# ------------------------------------------------------------
# Ejercicio 3
# Recorrer la tupla colores con un bucle for e imprimir cada elemento
# en mayusculas usando el metodo .upper().


# ------------------------------------------------------------
# Ejercicio 4
# Dadas las tuplas tupla1 = (1, 2, 3) y tupla2 = (4, 5, 6):
# - concatenar ambas en una nueva tupla llamada tupla_unida
# - multiplicar tupla1 por 2 y guardar el resultado en tupla_doble
# - imprimir ambas tuplas


# ------------------------------------------------------------
# Ejercicio 5
# Dada la tupla numeros = (10, 20, 30, 40, 50), verificar si el numero 30
# esta dentro y mostrar un mensaje distinto segun el caso usando in e if/else.


# ------------------------------------------------------------
# Ejercicio 6
# Crear un diccionario llamado mi_perfil con las claves:
# "nombre", "apellido", "edad" y "ciudad".
# Asignar tus datos como valores e imprimir el diccionario completo.


# ------------------------------------------------------------
# Ejercicio 7
# Usando el diccionario anterior, imprimir unicamente el valor de la clave
# "ciudad".


# ------------------------------------------------------------
# Ejercicio 8
# Cambiar el valor asociado a "edad" en mi_perfil y mostrar el diccionario
# actualizado.


# ------------------------------------------------------------
# Ejercicio 9
# Agregar la clave "correo" con un mail ficticio e imprimir el resultado.


# ------------------------------------------------------------
# Ejercicio 10
# Eliminar la clave "apellido" del diccionario mi_perfil y mostrar el
# resultado final.


# ------------------------------------------------------------
# Ejercicio 11
# Crear un diccionario llamado coordenadas donde las claves sean nombres de
# ciudades y los valores sean tuplas con (latitud, longitud).
# Luego, imprimir las coordenadas de una ciudad especifica.


# ------------------------------------------------------------
# Ejercicio 12
# Recorrer el diccionario coordenadas con un for y mostrar cada ciudad con el
# siguiente formato:
# Ciudad: Buenos Aires -> Latitud: -34.6037, Longitud: -58.3816


# ------------------------------------------------------------
# Ejercicio 13
# Dado un diccionario de productos con nombre y precio:
# - recorrer las claves usando .keys() y mostrarlas
# - recorrer los valores usando .values() y mostrarlos
# - recorrer los pares usando .items() con el formato:
#   Producto: manzana -> Precio: $1.5


# ============================================================
# EJERCICIOS AVANZADOS
# ============================================================


# Ejercicio 14
# A partir de una lista de frases, construir un diccionario donde:
# - las claves sean las palabras unicas
# - los valores sean la cantidad de veces que aparece cada palabra
# Requisitos:
# - dividir cada frase con split()
# - convertir todas las palabras a minusculas
# - ignorar los signos de puntuacion . , ! ?
# - mostrar el diccionario final ordenado alfabeticamente por clave


# ------------------------------------------------------------
# Ejercicio 15
# Dado un diccionario donde la clave es el nombre del producto y el valor es
# una tupla con las ventas mensuales, escribir un programa que:
# 1. calcule el total de ventas de cada producto
# 2. determine cual producto vendio mas en total
# 3. imprima un ranking de productos ordenado de mayor a menor


# ------------------------------------------------------------
# Ejercicio 16
# Usar un diccionario de coordenadas de ciudades e implementar una funcion
# distancia(ciudad_a, ciudad_b) que calcule la distancia euclidiana
# simplificada entre ambas.
# Luego, pedir dos ciudades por nombre y mostrar la distancia resultante.


# ------------------------------------------------------------
# Ejercicio 17
# Construir un programa para gestionar un registro de estudiantes.
# Usar un diccionario donde la clave sea el ID del estudiante y el valor una
# tupla (nombre, edad, promedio).
# El programa debe mostrar este menu en bucle hasta elegir salir:
# 1. Agregar estudiante
# 2. Listar todos los estudiantes
# 3. Buscar estudiante por ID
# 4. Eliminar estudiante por ID
# 5. Salir


# ------------------------------------------------------------
# Ejercicio 18
# Dado un diccionario donde cada valor es una lista de calificaciones,
# calcular:
# 1. el promedio de cada curso
# 2. el curso con el mejor promedio
# 3. el curso con el peor promedio


# ------------------------------------------------------------
# Ejercicio 19
# Hacer un juego tipo trivia usando una lista de tuplas con esta forma:
# (pregunta, opciones, respuesta_correcta)
# Requisitos:
# - recorrer las preguntas con for
# - mostrar las opciones numeradas y leer la respuesta del usuario
# - llevar un contador de aciertos
# - al finalizar, mostrar el puntaje total


# ------------------------------------------------------------
# Ejercicio 20
# Dado un inventario donde la clave es el codigo del producto y el valor es
# una tupla (nombre, precio, stock), implementar un menu que permita:
# 1. listar todo el inventario
# 2. buscar productos por nombre
# 3. filtrar productos por rango de precio
# 4. actualizar el stock de un producto
# 5. eliminar un producto
# Nota: como las tuplas son inmutables, para actualizar el stock hay que
# reemplazar la tupla completa por una nueva.
