"""
Ejercicios avanzados de Python
Formato para correccion: Consigna + Respuesta
"""


# ==================================================
# Ejercicio 1: Palindromo
# Consigna:
# Crear una funcion es_palindromo(cadena) que determine si una cadena
# es un palindromo ignorando mayusculas y espacios.
# Respuesta:
def es_palindromo(cadena):
    texto = cadena.lower().replace(" ", "")
    return texto == texto[::-1]


# ==================================================
# Ejercicio 2: Contador de vocales y consonantes
# Consigna:
# Crear una funcion contar_vocales_consonantes(cadena) que retorne
# la cantidad de vocales y consonantes en una cadena, ignorando
# espacios y caracteres no alfabeticos.
# Respuesta:
def contar_vocales_consonantes(cadena):
    vocales = "aeiou"
    contador_vocales = 0
    contador_consonantes = 0

    for caracter in cadena.lower():
        if caracter in vocales:
            contador_vocales += 1
        elif caracter.isalpha():
            contador_consonantes += 1

    return contador_vocales, contador_consonantes


# ==================================================
# Ejercicio 3: Invertir cadena sin slicing
# Consigna:
# Implementar una funcion invertir_cadena(cadena) que devuelva la
# cadena invertida sin usar slicing ([::-1]). Usar un bucle for o while.
# Respuesta:
def invertir_cadena(cadena):
    resultado = ""
    for caracter in cadena:
        resultado = caracter + resultado
    return resultado


# ==================================================
# Ejercicio 4: Validacion de contrasena compleja
# Consigna:
# Crear una funcion validar_contrasena(contrasena) que verifique si
# una contrasena cumple con:
# - Al menos 8 caracteres.
# - Contiene mayusculas, minusculas, numeros y un caracter especial (!@#$%^&*).
# Respuesta:
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False

    tiene_mayuscula = any(caracter.isupper() for caracter in contrasena)
    tiene_minuscula = any(caracter.islower() for caracter in contrasena)
    tiene_numero = any(caracter.isdigit() for caracter in contrasena)
    tiene_especial = any(caracter in "!@#$%^&*" for caracter in contrasena)

    return tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_especial


# ==================================================
# Ejercicio 5: Contar palabra en frase
# Consigna:
# Crear una funcion contar_palabra(frase, palabra) que cuente cuantas
# veces aparece una palabra especifica en una frase, ignorando mayusculas.
# Respuesta:
def contar_palabra(frase, palabra):
    palabras = frase.lower().split()
    objetivo = palabra.lower()
    return sum(1 for p in palabras if p == objetivo)


# ==================================================
# Ejercicio 6: Sumar digitos en cadena
# Consigna:
# Crear una funcion sumar_digitos(cadena) que sume todos los digitos
# presentes en una cadena usando isdigit() y un bucle.
# Respuesta:
def sumar_digitos(cadena):
    suma = 0
    for caracter in cadena:
        if caracter.isdigit():
            suma += int(caracter)
    return suma


# ==================================================
# Ejercicio 7: Validar email complejo
# Consigna:
# Crear una funcion validar_email(email) que valide si un email contiene
# un unico '@', un dominio despues del punto (por ejemplo: .com)
# y no tiene espacios.
# Respuesta:
def validar_email(email):
    if " " in email:
        return False

    partes = email.split("@")
    if len(partes) != 2:
        return False

    dominio = partes[1]
    if "." not in dominio:
        return False

    return True


# ==================================================
# Ejercicio 8: Generar acronimo
# Consigna:
# Crear una funcion generar_acronimo(frase) que genere un acronimo
# con las primeras letras de cada palabra en una frase.
# Respuesta:
def generar_acronimo(frase):
    primeras_letras = [palabra[0].upper() for palabra in frase.split() if palabra]
    return "".join(primeras_letras)


# ==================================================
# Ejercicio 9: Cifrado Cesar
# Consigna:
# Crear una funcion cifrar_cesar(cadena, clave) que desplace cada letra
# por clave posiciones en el alfabeto, manteniendo mayusculas/minusculas.
# Respuesta:
def cifrar_cesar(cadena, clave):
    resultado = ""

    for letra in cadena:
        if letra.isalpha():
            base = ord("a") if letra.islower() else ord("A")
            resultado += chr((ord(letra) - base + clave) % 26 + base)
        else:
            resultado += letra

    return resultado


# ==================================================
# Ejercicio 10: Palabra mas larga en frase
# Consigna:
# Crear una funcion palabra_mas_larga(frase) que encuentre y devuelva
# la palabra mas larga en una frase. Si hay empate, devolver la primera.
# Respuesta:
def palabra_mas_larga(frase):
    palabras = frase.split()
    mas_larga = ""

    for palabra in palabras:
        if len(palabra) > len(mas_larga):
            mas_larga = palabra

    return mas_larga


def mostrar_demostracion():
    print("=== DEMOSTRACION DE EJERCICIOS AVANZADOS ===")
    print("Ejercicio 1:", es_palindromo("Anita lava la tina"))
    print("Ejercicio 2:", contar_vocales_consonantes("Python 3.14"))
    print("Ejercicio 3:", invertir_cadena("Programacion"))
    print("Ejercicio 4:", validar_contrasena("Clave123!"))
    print("Ejercicio 5:", contar_palabra("hola Hola HOLA mundo", "hola"))
    print("Ejercicio 6:", sumar_digitos("a1b2c3"))
    print("Ejercicio 7:", validar_email("alumno@escuela.com"))
    print("Ejercicio 8:", generar_acronimo("Universidad Tecnologica Nacional"))
    print("Ejercicio 9:", cifrar_cesar("Hola Mundo", 3))
    print("Ejercicio 10:", palabra_mas_larga("python es muy poderoso"))


if __name__ == "__main__":
    mostrar_demostracion()





