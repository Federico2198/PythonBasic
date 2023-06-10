""" Definiendo listas """
# My first list
my_first_list = list()
# My second list
my_second_list = []

""" Agregando elementos a la lista """
# Agregar elementos a la lista llamada my_first_list
my_first_list = [1,2,3,4,5,6]
# Imprimiendo los elementos de my_first_list
print(my_first_list)
# Mostrar la longitud de my_fisrt_list
print(len(my_first_list))
# Mostrar el tipo de dato de my_first_list
print(type(my_first_list))

""" Accediendo a la primer posicion de la lista """
print(my_first_list[0])

""" Funciones internas de una lista """
print(my_first_list.count(1))

""" Asignar variables y valores a la lista """
# Definir la lista de valores
student = ["Juan", "Garcia", 30, "Uruguay", 10]
# Definir la lista con los atributos correspondientes, aunque hay que colocar los atributos primeros seguido de student
name, surname, age, country, note = student
print(note)

""" Concatenando listas """
# Definir la primer lista 
first_list = [1,2,3]
# Definir la primer lista 
second_list = [4,5,6]
# Imprimir concatenacion de listas 
print(first_list + second_list)

""" Agregar elementos a lista """
# Agregar un elemento al final de la lista
list_new = [1,2,3,4,5,6,7,8,9]
list_new.append(5)
print(list_new)
# Agregar un elemento en determinada posicion de la lista, por ejemplo agregar el numero 1.5 en la posicion 1
list_new.insert(1, 1.5)
print(list_new)
# Modificar el valorde la posicion 1
list_new[1] = 1.6
print(list_new)

""" Eliminar elementos de una lista """
# Eliminar un elemento de la lista por el valor del dato
list_new = [1,2,3,4,9]
list_new.remove(9)
print(list_new)
# Eliminar el último elemento de la lista
list_new.pop
print(list_new)
# Eliminar el elemento que quiero quitar de la lista por la posicion
print(list_new.pop(2))
print(list_new)
# Almacenar en una variable el valor que desapilamos 
list_final = list_new.pop(2)
print(list_final)
# Eliminar un elemento segun su valor
lista = [1,2,3,4]
del lista[1]
print(lista)
#Mantener estado de lista hasta este punto 
listastate = lista.copy()
# Eliminar todos los elementos que contiene una lista
lista.clear()
print(lista)
# Imprimir lista guardada en listaState
print(listastate)
# Imprimir una lista de forma inversa
listastate.reverse()
print(listastate)
# Imprimir la lista de menor a mayor
listastate.sort()
print(listastate)

"""Definiendo sub-listas """
# Definir cierta lista
listacompleta = [1,2,3,4,5,6,7,8,9]
print(listacompleta)
# Imprimir sub-lista a partir de la lista
print(listacompleta[1:3])
