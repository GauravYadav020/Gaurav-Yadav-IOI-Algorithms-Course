# Activity 1 - Polymorphism
class Cat:
    def sound(self):
        print("Meow")

class Dog:
    def sound(self):
        print("Bark")

for animal in [Cat(), Dog()]:
    animal.sound()

# Activity 2 - Encapsulation
class Student:
    def __init__(self):
        self.__marks = 90

    def show_marks(self):
        print(self.__marks)

s = Student()
s.show_marks()

# Activity 3 - Getter Method
class Employee:
    def __init__(self,salary):
        self.__salary = salary

    def get_salary(self):
        return self.__salary

e = Employee(50000)
print(e.get_salary())