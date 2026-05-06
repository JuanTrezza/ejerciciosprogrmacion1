
"""Unidad 7: Listas

Este archivo contiene 14 ejercicios sobre listas en Python.
Esta organizado en dos niveles: Medio y Superior.
Cada ejercicio incluye la consigna y su resolucion.
Se puede ejecutar completo con: python unidad7.py
"""


# ============================================================
# NIVEL MEDIO
# ============================================================


# Ejercicio 1
# Consigna:
# Pedir al usuario 5 numeros enteros, guardarlos en una lista
# e imprimir la lista resultante.

numeros = []

for i in range(5):
    num = int(input("Ingrese un numero entero:"))
    numeros.append(num)
print("Lista de numeros ingresados:", numeros)


# ------------------------------------------------------------
# Ejercicio 2
# Consigna:
# Crear una lista con nombres de companeros de clase.
# Imprimir la lista, ordenarla alfabeticamente e imprimirla otra vez.


lista_companeros = ["Juan", "Emiliano", "Mica", "Federico", "Sofia"]
print("Lista original:", lista_companeros)
lista_companeros.sort()
print("Lista ordenada:", lista_companeros)


# ------------------------------------------------------------
# Ejercicio 3
# Consigna:
# Crear una funcion que reciba una lista de numeros y devuelva
# una nueva lista con los primeros 10 numeros pares que encuentre.


lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
def primeros_pares(lista):
    nueva_lista = []
    for num in lista:
        if num % 2 == 0:
            nueva_lista.append(num)
        if len(nueva_lista) == 10:
            break
    return nueva_lista
print("Primeros 10 pares:", primeros_pares(lista_numeros))

# ------------------------------------------------------------
# Ejercicio 4
# Consigna:
# Pedir al usuario palabras separadas por comas, convertir ese texto
# en una lista e imprimir el resultado.

palabra = input("Ingrese palabras separadas por comas:")
lista_palabras = palabra.split(",")
print("Lista de palabras:", lista_palabras)



# ------------------------------------------------------------
# Ejercicio 5
# Consigna:
# Crear una lista con los numeros del 1 al 10.
# Recorrerla, elevar cada numero al cuadrado y guardar los resultados
# en una nueva lista. Luego, imprimir esa nueva lista.


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cuadrados = []
for num in numeros:
    cuadrados.append(num ** 2)
print("Lista de cuadrados:", cuadrados)


# ------------------------------------------------------------
# Ejercicio 6
# Consigna:
# Eliminar los elementos duplicados de una lista e imprimir
# la lista sin repetidos.

eliminar_duplicados = [1, 2, 3, 1, 2, 4]
sin_duplicados = list(set(eliminar_duplicados))
print("Lista sin duplicados:", sin_duplicados)



# ------------------------------------------------------------
# Ejercicio 7
# Consigna:
# Crear una funcion que busque un elemento especifico dentro de una lista.
# Debe devolver el indice si lo encuentra o un mensaje si no esta.
# Ejemplo: en [1, 2, 3, 4, 5], si buscas 3, devuelve 2.


busqueda_elemento = [1, 2, 3, 4, 5]
def buscar_elemento(lista, elemento):
    if elemento in lista:
        return lista.index(elemento)
    else:
        return "El elemento no se encuentra en la lista."
print(buscar_elemento(busqueda_elemento, 3))  # Devuelve 2
print(buscar_elemento(busqueda_elemento, 6))  # Devuelve mensaje

# ------------------------------------------------------------
# Ejercicio 8
# Consigna:
# Extraer una sublista indicando el indice inicial y el indice final,
# o bien la longitud de la sublista.
# Ejemplo: de [1, 2, 3, 4, 5, 6], desde indice 2 hasta el final,
# el resultado es [3, 4, 5, 6].


extraccion_sublista = [1, 2, 3, 4, 5, 6]
def extraer_sublista(lista, indice_inicial, indice_final=None):
    if indice_final is None:
        return lista[indice_inicial:]
    else:
        return lista[indice_inicial:indice_final]
print(extraer_sublista(extraccion_sublista, 2))  
print(extraer_sublista(extraccion_sublista, 1, 4))


# ============================================================
# NIVEL SUPERIOR
# ============================================================


# Ejercicio 9
# Consigna:
# Invertir el orden de una lista.
# Primero hacerlo manualmente. Luego, crear una funcion que lo haga.
# Ejemplo: [1, 2, 3, 4, 5] pasa a ser [5, 4, 3, 2, 1].


invertir_lista = [1, 2, 3, 4, 5]
# Inversion manual
invertida_manual = []
for i in range(len(invertir_lista)-1, -1, -1):
    invertida_manual.append(invertir_lista[i])
print("Lista invertida manualmente:", invertida_manual)
# Funcion para invertir la lista
def invertir_lista_funcion(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1):
        invertida.append(lista[i])
    return invertida
print("Lista invertida con funcion:", invertir_lista_funcion(invertir_lista))

# ------------------------------------------------------------
# Ejercicio 10
# Consigna:
# Crear una funcion que elimine elementos duplicados de una lista.
# Ejemplo: [1, 2, 3, 1, 2, 4] se convierte en [1, 2, 3, 4].


def eliminar_duplicados_funcion(lista):
    sin_duplicados = []
    for elemento in lista:
        if elemento not in sin_duplicados:
            sin_duplicados.append(elemento)
    return sin_duplicados
print("Sin duplicados:", eliminar_duplicados_funcion([1, 2, 3, 1, 2, 4]))

# ------------------------------------------------------------
# Ejercicio 11
# Consigna:
# Crear una funcion que combine dos listas en una sola.
# Ejemplo: [1, 2, 3] y [4, 5, 6] se convierten en [1, 2, 3, 4, 5, 6].


def combinacion_listas(lista1, lista2):
    combinada = lista1 + lista2
    return combinada
print("Listas combinadas:", combinacion_listas([1, 2, 3], [4, 5, 6]))

# ------------------------------------------------------------
# Ejercicio 12
# Consigna:
# Crear dos funciones:
# - una para calcular la interseccion entre dos listas
# - otra para calcular la diferencia entre dos listas
# Deben funcionar con listas de cualquier longitud y tipo de elemento.


def interseccion_listas(lista1, lista2):
    interseccion = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in interseccion:
            interseccion.append(elemento)
    return interseccion

def diferencia_listas(lista1, lista2):
    diferencia = []
    for elemento in lista1:
        if elemento not in lista2 and elemento not in diferencia:
            diferencia.append(elemento)
    return diferencia
print("Interseccion:", interseccion_listas([1, 2, 3, 4], [3, 4, 5, 6]))
print("Diferencia:", diferencia_listas([1, 2, 3, 4], [3, 4, 5, 6]))


# ------------------------------------------------------------
# Ejercicio 13
# Consigna:
# Crear una funcion que genere una lista a partir de un rango definido
# por el usuario: valor inicial, valor final e incremento.


def lista_desde_rango(inicio, fin, incremento):
    lista = []
    for num in range(inicio, fin, incremento):
        lista.append(num)
    return lista
print("Lista desde rango (1, 20, 3):", lista_desde_rango(1, 20, 3))


# ------------------------------------------------------------
# Ejercicio 14
# Consigna:
# Implementar una busqueda manual en una lista ordenada.
# La funcion debe recibir la lista y el elemento a buscar.
# Debe devolver el indice si lo encuentra o un mensaje si no esta.
# No usar index() ni find().


def busqueda_manual(lista, elementoBuscar):
    for i in range(len(lista)):
        if lista[i] == elementoBuscar:
            return i
    return "El elemento no se encuentra en la lista."
print("Busqueda manual de 4:", busqueda_manual([1, 2, 3, 4, 5], 4))
print("Busqueda manual de 9:", busqueda_manual([1, 2, 3, 4, 5], 9))
