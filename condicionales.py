""" Condicionales """
# Definir una condicional 
my_variable = 12

if my_variable > 10 and my_variable <= 20: 
    print("Se ejecuta la condicion del if debido a que el valor es mayor que 10 pero menor o igual que 20")
elif my_variable >20 and my_variable <= 30:
    print("Se ejecuta la condicion elif debido a que el valor es mayor que 20 pero menor o igual que 30")
else:
    print("Se ejecuta la condicion del else debido a que el valor es menor o igual que 10 o mayor a 30")
