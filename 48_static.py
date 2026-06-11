class animal:
    def __init__(self,name):
        self.name = name

    def speak(self):
        pass

    @staticmethod
    def create_animal(name,animal_type):
        if animal_type == "dog":
            return Dog(name)
        elif animal_type == "cat":
            return Cat(name)
        else:
            raise ValueError("Invalid animal type")

class Dog(animal):
    def speak(self):
        return 'Woof!'

class Cat(animal):
    def speak(self):
        return 'Meow!'

my_dog = animal.create_animal(name = "Lobby", animal_type = "dog")
my_cat = animal.create_animal(name = "Garfield", animal_type = "cat")

#Value errror
#random = Animal.create_animal(name='Random', animal_type='random')

print(my_dog.speak())
print(my_cat.speak())