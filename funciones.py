""" Definiendo y llamando a funciones """

# Definir a una función simple
def my_function ():
    print("Esto es una función")
# Llamar a una función simple
my_function ()

# Definir a una función con parametros
def my_second_function (first_number, second_number):
    print(first_number + second_number)
# Llamar a una función con parametros
my_second_function (2,3)

# Definir a una función con parametros especificandole el tipo de dato
def my_second_function (first_number: int, second_number: int): # No sirve de nada colocar int por ser un tipado debil 
    print(first_number + second_number)
# Llamar a una función con parametros especificandole el tipo de dato
my_second_function (2,3)

# Dinir una fuunción con parametros y que retorne un resultado 
def sumando_valores (first_value, second_value):
    return first_value + second_value
valor_retornado = sumando_valores(1,2) # Almacenar el valor que retorna en una variable 
print(valor_retornado)

# Definir una funcion donde imprima el nombre y el surname
def nombre_completo (name,surname):
    print(f"{name} {surname}")
nombre_completo("Federico", "Moreira")

# Definir una funcion donde imprima el nombre, el surname y el alias en caso de corresponder
def nombre_completo (name,surname, alias = "sin alias"):
    print(f"{name} {surname} {alias}")
nombre_completo("Federico", "Moreira")

# Definir una funcion donde se pueda imprimir la cantidad de palabras que un usuario quiera
def words (*word):
    print(word)
words("Hola", "Me", "Llamo", "Federico")