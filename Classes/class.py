# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says Woof!")
    
#     def info(self):
#         print(f"Name: {self.name}, Age: {self.age}")

# my_dog = Dog("Rex", 3)
# my_dog.bark()
# my_dog.info()

#creating multiple objects

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def bark(self):
#         print(f"{self.name} says Woof!")

# dog1 = Dog("Rex", 3)
# dog2 = Dog("Buddy", 5)
# dog3 = Dog("Max", 1)

# dog1.bark()  # Rex says Woof!
# dog2.bark()  # Buddy says Woof!
# dog3.bark()  # Max says Woof!

# print(dog1.name)  # Rex
# print(dog2.age)   # 5

# class Car:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year
#     def start(self):
#         return f"Car started!"
#     def info(self):
#         return f"Brand : {self.brand}, Model : {self.model}, Year : {self.year}"

# my_car = Car("BMW", "i3", 2026)
# print(my_car.start())
# print(my_car.info())


#class atribute

# class Dog:
#     species = "Canis familiaris"  # ← class attribute (hammaga bir xil)
    
#     def __init__(self, name, age):
#         self.name = name   # ← instance attribute (har biriga o'z)
#         self.age = age
    
#     def __str__(self):
#         return f"Name is {self.name}, age is {self.age}"

# dog1 = Dog("Rex", 3)
# dog2 = Dog("Buddy", 5)

# print(dog1.species)  # Canis familiaris
# print(dog2.species)  # Canis familiaris
# print(dog1.name)     # Rex
# print(dog2.name)     # Buddy

# print(dog2)

# class Animal:
#     def __init__(self, name):
#         self.name = name

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # ← Parent __init__ ni chaqiradi
#         self.breed = breed      # ← o'ziga xos qo'shadi

# dog = Dog("Rex", "Labrador")
# print(dog.name)   # Rex ← Animal dan
# print(dog.breed)  # Labrador ← Dog dan

#encapsulation

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # ← __ (private)
    
    def deposit(self, amount):
        self.__balance += amount
    
    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # 1500
