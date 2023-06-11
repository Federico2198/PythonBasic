""" Definiendo clases """
class MyPerson:
    # Crear un contructor de la clase, para eso se debe usar def init self
    def __init__(self, name, surname, alias = "sin alias"):
        self.name = name
        self.surname = surname
        self.alias = alias
    # Crear una funcion de la clase
    def talk (self):
        print(f"{self.name} {self.surname} {self.alias} puede hablar")

my_person = MyPerson("Federico", "Moreira")
print(f"{my_person.name} {my_person.surname} {my_person.alias}")
my_person.talk()

