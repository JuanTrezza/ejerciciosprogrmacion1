"""
EJERCICIO 5 — Número Primo
###########################

Escribí una función llamada `es_primo(numero)` que reciba un número entero
y retorne `True` si es primo, o `False` si no lo es.

Un número es primo si es mayor a 1 y solo es divisible por 1 y por sí mismo.

Requisitos:
- Usá un bucle `while` para verificar los divisores (no uses `for`).
- Empezá a verificar desde el 2 hasta el número anterior al que se recibe.
- En cuanto encontrés un divisor, retorná `False` inmediatamente.
- Si el bucle termina sin encontrar divisores, retorná `True`.
- Si el número es menor o igual a 1, retorná `False` directamente.

Luego llamá a la función con los siguientes ejemplos e imprimí los resultados:

    print(es_primo(2))   # True
    print(es_primo(7))   # True
    print(es_primo(11))  # True
    print(es_primo(1))   # False
    print(es_primo(4))   # False
    print(es_primo(9))   # False
    print(es_primo(0))   # False

"""

def es_primo(numero):
    if numero <= 1:
        return False
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True
# Ejemplos de uso
print(es_primo(2))   # True
print(es_primo(7))   # True
print(es_primo(11))  # True
print(es_primo(1))   # False
print(es_primo(4))   # False
print(es_primo(9))   # False
print(es_primo(0))   # False 
