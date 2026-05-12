
"""
SIMULACION DE PARCIAL - GUIA DE PRACTICA

Esta simulacion no es para entregar.
Objetivo: practicar el tipo de ejercicios que pueden aparecer en el parcial.

Si tenes dudas:
- Consultar en clase.
- O escribir a juan.pablo.sosa@istea.com.ar

---

COMO USAR ESTA GUIA

1. Lee la consigna completa antes de programar.
2. Escribi un mini plan (3 a 5 pasos).
3. Resolve primero una version simple que funcione.
4. Mejora nombres de variables y funciones.
5. Proba con casos normales y casos borde.

Sugerencia: no saltees validaciones de entrada cuando el ejercicio las pide.

---

EJERCICIOS

Ejercicio 1 - Validar Contrasena
Consigna:
- Crear una funcion que reciba un string.
- Debe devolver True si cumple todas las condiciones de seguridad.
- Debe devolver False si falla al menos una condicion.

Validaciones esperadas:
- Longitud minima.
- Al menos una mayuscula.
- Al menos una minuscula.
- Al menos un digito.
- Sin espacios.

Ejercicio 2 - Combinar Dos Listas
Consigna:
- Crear una funcion que una dos listas en una nueva lista.
- Recorrer con bucles.
- No usar + ni .extend().

Punto clave:
- Mantener el orden original de ambas listas.

Ejercicio 3 - Eliminar Duplicados
Consigna:
- Crear una funcion que quite elementos repetidos.
- Conservar el orden de primera aparicion.
- No usar set().

Punto clave:
- Revisar elemento por elemento antes de agregar al resultado.

Ejercicio 4 - Contar Apariciones
Consigna:
- Crear una funcion para contar cuantas veces aparece un elemento.
- Crear otra funcion para mostrar el conteo de todos los elementos unicos.
- No usar .count().

Punto clave:
- Separar bien responsabilidades entre funciones.

Ejercicio 5 - Numero Primo
Consigna:
- Crear una funcion que indique si un numero es primo.
- Usar bucle while para verificar divisores.

Punto clave:
- Cortar la verificacion apenas encuentres un divisor.

Ejercicio 6 - Conversor de Unidades con Modulo
Consigna:
- Crear un conversor de kilometros a millas y de kilogramos a libras.
- Usar menu interactivo.
- Dejar las funciones de conversion en un modulo separado llamado conversiones.py.
- Incluir docstrings en las funciones de conversion.

Punto clave:
- Validar opciones de menu y valores numericos positivos.

---

CRITERIOS QUE TE CONVIENE CUMPLIR EN TODOS

- Codigo legible y ordenado.
- Funciones chicas, cada una con una sola responsabilidad.
- Nombres claros para variables y funciones.
- Evitar funciones o metodos prohibidos por consigna.
- Mensajes de error claros para el usuario cuando corresponda.

---

CHECKLIST FINAL ANTES DE DARLO POR TERMINADO

- La solucion cumple exactamente lo pedido en la consigna.
- No use herramientas prohibidas en el ejercicio.
- Probe casos normales.
- Probe casos borde (entradas vacias, invalidas o extremas).
- El codigo se entiende al leerlo.

---

Importante:
Esta guia no incluye resoluciones. Solo organiza y aclara las consignas para practicar mejor.
"""

# Ejericio 1 - Validar Contrasena

def validar_contrasena(contrasena):
    """Valida si una contrasena cumple con los requisitos de seguridad."""
    if len(contrasena) < 8:
        return False
    if not any(c.isupper() for c in contrasena):
        return False
    if not any(c.islower() for c in contrasena):
        return False
    if not any(c.isdigit() for c in contrasena):
        return False
    if ' ' in contrasena:
        return False
    return True

# Ejercicio 2 - Combinar Dos Listas

def combinar_listas(lista1, lista2):

    resultado = []

    for item in lista1:
        resultado.append(item)

    for item in lista2:
        resultado.append(item)

    return resultado

# Ejercicio 3 - Eliminar Duplicados
def eliminar_duplicados(lista):
    resultado = []
    for item in lista:
        if item not in resultado:
            resultado.append(item)
    return resultado

# Ejercicio 4 - Contar Apariciones

def contar_apariciones(lista,elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

# Ejercicio 5 - Numero Primo

def es_numero_primo(numero):
    if numero < 2:
        return False
    divisor = 2
    while divisor < numero:
        if numero % divisor == 0:
            return False
        divisor += 1
    return True
  






