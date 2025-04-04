class Animal:
    def speak(self):
        return 'Some animal sounds.'
    
class Dog(Animal):
    def speak(self):
        return 'Woof!'
    
class Cat(Animal):
    def speak(self):
        return 'Meow!'
    
class Cow(Animal):
    def speak(self):
        return 'Mooo!'
    
def animal_talk(Animal):
    print(Animal.speak())
    
dog = Dog()
cat = Cat()
cow = Cow()

animal_talk(dog)
animal_talk(cat)
animal_talk(cow)


class Vehicle:
    def sound(self):
        return 'Some vehicle sounds'
    
class Car(Vehicle):
    def sound(self):
        return 'Vrooom!'
    
class Bike(Vehicle):
    def sound(self):
        return 'Brrrr!'
    
class Truck(Vehicle):
    def sound(self):
        return ' Grrrr!'
    
def make_sound(Vehicle):
    print(Vehicle.sound())

car = Car()
bike = Bike()
truck = Truck()

make_sound(car)
make_sound(bike)
make_sound(truck)


