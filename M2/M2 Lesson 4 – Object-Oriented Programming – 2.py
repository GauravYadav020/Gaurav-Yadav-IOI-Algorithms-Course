# Activity 1 - Instance Method
class Student:
    def greet(self):
        print("Welcome Student")

s = Student()
s.greet()

# Activity 2 - Class Method Example
class Math:
    def add(self,a,b):
        print(a+b)

m = Math()
m.add(5,7)

# Activity 3 - Object Interaction
class Dog:
    def speak(self):
        print("Bark")

d = Dog()
d.speak()