""" Definiendo tuplas """
# My first tuple
my_first_tuple = tuple()
# My second tuple
my_second_tuple = ()

""" Practicando con tuplas """
# Definir una tupla
my_first_tuple = (1,2,3,3,4)
print(my_first_tuple)
# Contar la cantidad que hay de cierto elemento
print(my_first_tuple.count(3))
# Mostrar la posicion en el indice de cierto elemento 
print(my_first_tuple.index(4))
# Definir la segunda tupla
my_second_tuple = (4,5,6,1,2,0)
print(my_second_tuple)
# Concatenar primer tupla y segunda tupla, y generar una nueva tupla 
my_finish_tuple = my_first_tuple + my_second_tuple
print(my_finish_tuple)
# Imprimir un intervalo de la tupla
print(my_finish_tuple[2:5])

""" CONVERTIR DE TUPLA A LISTA """
# Pasar de una tupla a una lista
my_finish_list = list(my_finish_tuple)
print(type(my_finish_list))

""" Convertir de LISTA A TUPLA """
my_last_tuple = tuple(my_finish_list)
print(type(my_finish_tuple))