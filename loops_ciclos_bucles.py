""" Ciclo While """
# Definir un ciclo while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("El valor de la variable my_condition es mayor o igual a 10")

# Definir un ciclo while con un break 
my_condition_second = 0
while my_condition_second < 20:
    my_condition_second += 1
    if my_condition_second == 15:
        print("Se detiene la ejecución")
        break
    print(my_condition_second)
print("La ejecución continúa")

""" Ciclo For """
# Definir un ciclo for para una lista
my_list = [1,2]
for element in my_list:
    print(element)
else:
    print("El ciclo for para la lista ha finalizado")

# Definir un ciclo for para una tupla
my_tuple = (1,2,3)
for element in my_tuple:
    print(element)
else:
    print("El ciclo for para la tupla ha finalizado")

# Definir un ciclo for para un set
my_set = {1,2,3,4,5,6}
for element in my_set:
    print(element)
else:
    print("El ciclo for para el set ha finalizado")

# Definir un ciclo for para un diccionario donde imprime las key no el value
my_dict = {"Primer Numero":1, "Segundo Numero":2, "Tercer Numero":3, "Cuarto Numero":4}
for element in my_dict:
    print(element)
else:
    print("El ciclo for para el diccionario ha finalizado")
# Si deseamos que imprima los valores del diccionario en lugar de las key
for element in my_dict.values():
    print(element)
else:
    print("El ciclo for para el diccionario ha finalizado")
# Si deseamos que imprima los valores del diccionario en lugar de las key, 
# y a la vez se salga del ciclo for si se cumple el break
for element in my_dict.values():
    print(element)
    if element == 2:
        break
else:
    print("El ciclo for para el diccionario ha finalizado")
# Si deseamos que imprima los valores del diccionario en lugar de las key, 
# y a la vez continue el ciclo for unicamente ignorando la condicion de continue
for element in my_dict.values():
    print(element)
    if element == 3:
        continue
    print("Imprimir este mensaje mientras no sea el elemento del continue")
else:
    print("El ciclo for para el diccionario ha finalizado")