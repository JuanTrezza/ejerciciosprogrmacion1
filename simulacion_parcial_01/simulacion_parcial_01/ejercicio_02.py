"""
EJERCICIO 2 — Combinar Dos Listas
##################################

Escribí una función llamada `combinar_listas(lista1, lista2)` que reciba dos listas
como parámetros y devuelva una nueva lista con todos los elementos de ambas,
primero los de `lista1` y luego los de `lista2`.

Importante: no uses el operador `+` entre listas ni el método `.extend()`.
Debés recorrer cada lista con un bucle y construir la nueva lista elemento por elemento.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    lista_a = [1, 2, 3]
    lista_b = [4, 5, 6]
    # Resultado esperado: [1, 2, 3, 4, 5, 6]

    lista_c = ["manzana", "pera"]
    lista_d = ["naranja", "uva", "durazno"]
    # Resultado esperado: ["manzana", "pera", "naranja", "uva", "durazno"]

"""

def combinar_lista(lista, lista2):
    nueva_lista = []

    for elemento in lista:
        nueva_lista.append(elemento)
    for elemento in lista2:
        nueva_lista.append(elemento)
    return nueva_lista

# Pruebas
lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
print(combinar_lista(lista_a, lista_b))  

lista_c = ["manzana", "pera"]
lista_d = ["naranja", "uva", "durazno"]
print(combinar_lista(lista_c, lista_d)) 
