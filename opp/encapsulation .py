class Bankaccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance
    
account = Bankaccount(5000)
account.deposit(1000)
print(account.get_balance())

print('___________________________________________________________________________________________________________________')

class BankAccount:
    def __init__(self, acc_number, balance):
        self.acc_number = acc_number
        self.__balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Dposit of Ksh {amount} is successful.')
        else:
            print('Invalid amount')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Ksh. {amount} withdrawn succssfully.')
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self.__balance

account = BankAccount(12345632, 4000)
account.deposit(8000)
account.withdraw(3000)
print(f'Current balance is {account.get_balance()}')

print('___________________________________________________________________________________________________________________')
class Student:
    def __init__(self, name):
        self.name = name
        self.__grade = None

    def set_grade(self, grade):
        if 0 <= grade <= 100:
            self.__grade = grade
        else:
            print('Invalid grade. Must be 0–100')

    def get_grade(self):
        return self.__grade
std1 = Student('Miriam')
std1.set_grade(80)
std2 = Student('Aaron')
std2.set_grade(34)
print(f'{std1.name} attained a  grade of {std1.get_grade()}')
print(f'{std2.name} attained a grade of {std2.get_grade()}')

print('___________________________________________________________________________________________________________________')
class Car:
    def __init__(self):
        self.__speed = 0

    def accelarate(self):
        self.__speed += 20

    def brake(self):
        if self.__speed >= 20:
            self.__speed -= 20

    def get_speed(self):
        return self.__speed        

car = Car()
car.accelarate()
car.accelarate()
car.accelarate()
car.brake()
print(car.get_speed())

print('___________________________________________________________________________________________________________________')

class Thermostat:
    def __init__(self):
        self.__temp = 10


    def set_temp(self):
        if 10 >= self.__temp  <= 30:
            print('Out of range.')
        else:
            print('Very good')
        
    def get_temp(self):
        return self.__temp
    
t = Thermostat()
t.set_temp(45)
print(t.get_temp())


    
