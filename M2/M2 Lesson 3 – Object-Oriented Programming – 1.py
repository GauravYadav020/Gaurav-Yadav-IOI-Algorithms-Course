# Activity 1 - Create Class
class Student:
    pass

s1 = Student()
print("Object Created")

# Activity 2 - Class with Attributes
class Car:
    brand = "Toyota"

c = Car()
print(c.brand)

# Activity 3 - Constructor
class Person:
    def __init__(self,name):
        self.name = name

p = Person("Gaurav")
print(p.name)