class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return f'{self.name} says woof!'
    
    def display(self):
        return f'{self.name} is of {self.breed} breed.'
    
dog1 = Dog('Buudy', 'Beagle')
dog2 = Dog('Bruce', 'Chiwawa')
           
print(dog1.bark())
print(dog1.display())

print(dog2.bark())
print(dog2.display())

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance
    

account = BankAccount(15000)
account.deposit(8000)

print(account.get_balance())

    
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):

    def speak(self):
        return f'{self.name} says woof!'
    
class Cat(Animal):
     def speak(self):
        return f'{self.name} says meoew!'
     
dog = Dog('Simba')
cat = Cat('Biddy')

print(cat.speak())
print(dog.speak())

