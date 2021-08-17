
# ! Havendo dois métodos com o mesmo nome, a classe Filha irá sobreescrever. Ex: speak() 
class Animal:
    def __init__(self, name, age, pet = None):
        self.name = name
        self.age = age
        self.pet = pet
        
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old, I am a {self.pet}')
        
    def speak(self):
        print('I dont know what I say')        

class Cat(Animal):
    def __init__(self, name, age, pet, color):
        super().__init__(name, age, pet=pet)
        self.color = color
                
    def speak(self):
        print('Meowww!')
        
    def show(self):
        print(f'I am {self.name} and I am {self.age} years old, I am a {self.pet} and my color is {self.color}')
    
class Dog(Animal):
    def speak(self):
        print('Au Au')


a = Animal('Tim', 12)
a.speak()

print()

c1 = Cat('Mimo', 9, 'Gatinho', 'Black')
c1.show()                      
c1.speak()
# d1 = Dog('Lulu', 10, 'Cachorrinho')
# d1.show()
# d1.speak()
