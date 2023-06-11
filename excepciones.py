""" Excepciones """

# Try-Except-else-finish
number_one = 1
number_two = 2

try:
    print(number_one + number_two)
    print("No se ha producido un error")
except:
    print("Se ha producido un error")
else:
    print("La ejecución continua correctamente porque no se ha produccido un error")
finally:
    print("La ejecución continua haya o no haya una excepción")


# Diferentes tipos de Except (ValueError, )

number_three = 3
number_four = "4"

try:
    print(number_three + number_four)
except ValueError:
    print("Se ha producido un error de tipo Value")
except TypeError:
    print("Se ha producido un error de tipo Type")
