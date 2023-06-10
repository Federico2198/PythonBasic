# Formateo
name, lastname, actualyear = "Federico", "Moreira", 2023
# Haciendo uso de format 
print("Mi nombre completo es {} {} y este es el año {}".format(name, lastname, actualyear))
# Forma mas recomendable
print("Mi nombre completo es %s %s y el actual año es %d" %(name, lastname, actualyear))
# Formateando cadena de texto por medio de la inferencia de datos
print(f"Mi nombre es {name} {lastname} y el actual año es {actualyear}")
# Formateando cadena de texto de forma tradicional
print("Mi nombre es " + name + " " + lastname + " y el actual año es " + str(actualyear))

# Desempaquetando caracteres 
language = "Python"
a, b, c, d, e, f = language
print(a)
print(e)

# Imprimir un rango de caracteres de una variable, por ejemplo imprimir del caracter 1 al 4 sin incluir el 4
language_slice = language[1:4]
print(language_slice)

# Imprimir desde un valor hasta el final debemos colocar el caracter inicial sin incluir un valor final 
language_slice = language[1:]
print(language_slice)

# Imprimir la anteúltima posición de una variable
language_slice = language[-2]
print(language_slice)

# Imprimir una variable de manera reversa 
reversed_language = language[::-1]
print(reversed_language)

# Imprimir unicamente las posiciones pares de la palabra, donde 0 a 6 abarca la palabra python y 
# 2 hace referencia a los saltos comenzando a imprimir desde laposicion 0
posicion_par = language[0:6:2]
print(posicion_par)

# Imprimir la primer letra de una palabra en mayúsculas
word = "hola"
print(word.capitalize())

# Imprimir toda la palabra en mayusculas 
word = "hola"
print(word.upper())

# Imprimir la cantidad de o que contiene la palabra
word = "hola"
print(word.count("o"))

# Mostrar si la palabra es un número 
word = "hola"
print(word.isnumeric())

# Transformar una palabra a mayuscula, y luego verificar si esta en mayuscula
word = "hola"
print(word.upper().isupper())

# Verificar que una palabra comienza con determinados caracteres 
word = "hola"
print(word.startswith("ho"))