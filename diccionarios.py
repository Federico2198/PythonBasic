""" Definiendo diccionarios """
# Definir first_dictionary
first_dictionary = dict()
# Definir second_dictionary
second_dictionary = {}

""" Practicando con diccionarios """
# Definir un diccionario
first_dictionary = {
    "Nombre":"Federico", 
    "Apellido":"Moreira",
    "Language": {"Java", "Python", "JavaScript"}
    }
# Imprimir un diccionario
print(first_dictionary)
# Imprimir los lenguajes del diccionario 
print(first_dictionary["Language"])

# Actualizar los valores de una clave dentro del diccionario 
first_dictionary["Language"] = "Go"
print(first_dictionary["Language"])

# Agreagar una nueva clave y valor al diccionario
first_dictionary["Pais"] = "Uruguay"
print(first_dictionary)

# Eliminar un elemento del diccionario
del first_dictionary["Pais"]
print(first_dictionary)

# Buscar si una clave existe en el diccionario 
print("Nombre" in first_dictionary)

# Buscar que elementos existen dentro de una clave en el diccionario
print(first_dictionary["Nombre"])

# Listado de cada uno de los items del diccionario
print(first_dictionary.items())

# Listado de cada uno de las claves del diccionario
print(first_dictionary.keys())

# Listado de cada uno de los valores del diccionario
print(first_dictionary.values())