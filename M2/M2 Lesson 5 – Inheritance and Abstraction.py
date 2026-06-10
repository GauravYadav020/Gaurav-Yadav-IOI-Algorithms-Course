from abc import ABC, abstractmethod

# Activity 1 - Single Inheritance
class Animal:
    def sound(self):
        print("Animal Sound")

class Dog(Animal):
    pass

d = Dog()
d.sound()

# Activity 2 - Method Override
class Bird:
    def fly(self):
        print("Flying")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow Flying")

Sparrow().fly()

# Activity 3 - Abstraction
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Square(Shape):
    def area(self):
        print("Area of Square")

Square().area()