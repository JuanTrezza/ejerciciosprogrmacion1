"""
EJERCICIO 4 — Contar Apariciones en una Lista
###############################################

Escribí una función llamada `contar_apariciones(lista, elemento)` que reciba
una lista y un elemento, y devuelva cuántas veces aparece ese elemento en la lista.

Importante: no uses el método `.count()` de las listas.
Debés recorrer la lista con un bucle y contar manualmente.

Luego escribí otra función llamada `contar_todos(lista)` que reciba una lista
y devuelva un resumen de cuántas veces aparece cada elemento único.
El resultado debe imprimirse de esta forma (un elemento por línea):

    "manzana" aparece 3 veces
    "pera" aparece 1 vez
    "naranja" aparece 2 veces

Probá las funciones con los siguientes ejemplos:

    frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]

    print(contar_apariciones(frutas, "manzana"))  # 3
    print(contar_apariciones(frutas, "pera"))     # 1
    print(contar_apariciones(frutas, "uva"))      # 0

    contar_todos(frutas)
    # manzana aparece 3 veces
    # pera aparece 1 vez
    # naranja aparece 2 veces

Nota: para `contar_todos` podés apoyarte en la función `eliminar_duplicados`
del ejercicio anterior, o resolverlo de otra manera.

"""

from simulacion_parcial_01.simulacion_parcial_01.ejercicio_03 import eliminar_duplicados


def contar_apariciones(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

def contar_todos(lista):
    elementos_unicos = eliminar_duplicados(lista)
    for elemento in elementos_unicos:
        cantidad = contar_apariciones(lista, elemento)
        if cantidad == 1:
            print(f'"{elemento}" aparece {cantidad} vez')
        else:
            print(f'"{elemento}" aparece {cantidad} veces')

# Ejemplos de uso
frutas = ["manzana", "pera", "manzana", "naranja", "manzana", "naranja"]
print(contar_apariciones(frutas, "manzana"))  # 3
print(contar_apariciones(frutas, "pera"))     # 1
print(contar_apariciones(frutas, "uva"))      # 0   
