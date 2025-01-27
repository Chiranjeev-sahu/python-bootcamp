#    Object-Oriented Programming (OOP) in  

#  Object-Oriented Programming (OOP)  is a programming paradigm that organizes software design around  objects  rather than functions or logic. Objects are instances of  classes , which are blueprints for creating objects. OOP allows for encapsulation, inheritance, polymorphism, and abstraction.

# 

#    Key Concepts in OOP: 

# 1.  Class :
#    - A class is a blueprint for creating objects (a collection of attributes and methods).
#    - It defines the structure and behavior of an object.

#     
#    class Car:
#        def __init__(self, brand, model):
#            self.brand = brand
#            self.model = model
       
#        def start_engine(self):
#            print(f"{self.brand} {self.model} engine started.")
#     

# 2.  Object :
#    - An object is an instance of a class.
#    - Objects are created based on the class blueprint.

#     
#    my_car = Car("Toyota", "Corolla")  # Object creation
#     

# 3.  Encapsulation :
#    - Encapsulation is the concept of bundling the data (attributes) and methods (functions) that operate on the data within a single unit or class.
#    - It also refers to controlling access to the data by using private and public access modifiers.

#     
#    class BankAccount:
#        def __init__(self, balance):
#            self.__balance = balance  # Private variable
   
#        def deposit(self, amount):
#            self.__balance += amount
   
#        def get_balance(self):
#            return self.__balance
#     

# 4.  Inheritance :
#    - Inheritance allows a class to inherit attributes and methods from another class, promoting code reuse.
#    - The new class (child class) inherits the properties and methods of an existing class (parent class).

#     
#    class ElectricCar(Car):  # Inheriting from Car class
#        def __init__(self, brand, model, battery_capacity):
#            super().__init__(brand, model)  # Calling the parent constructor
#            self.battery_capacity = battery_capacity
       
#        def charge(self):
#            print(f"{self.brand} {self.model} is charging.")
#     

# 5.  Polymorphism :
#    - Polymorphism allows different classes to be treated as instances of the same class through inheritance. It enables the same method name to behave differently depending on the object.
   
#     
#    class Animal:
#        def speak(self):
#            print("Animal speaks")
   
#    class Dog(Animal):
#        def speak(self):
#            print("Dog barks")
   
#    class Cat(Animal):
#        def speak(self):
#            print("Cat meows")
   
#    # Polymorphism in action
#    def animal_speak(animal):
#        animal.speak()

#    dog = Dog()
#    cat = Cat()
#    animal_speak(dog)  # Outputs: Dog barks
#    animal_speak(cat)  # Outputs: Cat meows
#     

# 6.  Abstraction :
#    - Abstraction involves hiding the complex implementation details of a system and providing a simplified interface.
#    - In , abstraction is achieved through  abstract classes  and  abstract methods  using the `abc` module.

#     
#    from abc import ABC, abstractmethod
   
#    class Animal(ABC):
#        @abstractmethod
#        def sound(self):
#            pass
   
#    class Dog(Animal):
#        def sound(self):
#            print("Woof")
#     

# 

