""" Definiendo sets """
# Primer forma de definir sets
my_first_set = set()
# Segunda forma de definir sets, es identico a definir diccionarios 
my_second_set = {}

""" Practicando con sets """
# Definir un set de elementos 
my_first_set = {"Federico", "Moreira", 2023}
print(type(my_first_set))
# Acceder a una posicion del set, es imposible
# print(my_first_set[1]) # Esto no esta permitido
# Buscar un elemento si existe en el set
print("Federico" in my_first_set)
my_first_set.remove(2023)
print(my_first_set)
# Definir el segundo set 
my_second_set = {"Dia", "Noche"}
print(my_second_set)
# Concatenar dos set
my_final_set = my_first_set.union(my_second_set)
print(my_final_set)