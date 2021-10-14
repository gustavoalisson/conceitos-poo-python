class Person:
    # * Não é específico da instância
    # * Especifico da classe
    number_of_people = 0
    
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1
    
p1 = Person('Alisson')
p2 = Person('Jamilly')
p3 = Person('José')
p4 = Person('Carlos')

print(Person.number_of_people)                 

