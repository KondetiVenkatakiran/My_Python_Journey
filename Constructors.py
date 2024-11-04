# from psutil import cpu_percent


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#     def draw(self):
#         print("draw")
#
# point = Point(10,20)
#
# print(point.x)
# print(point.y)
#
#
#
# class Dog:
#     def __init__(self, name, age):
#         self.name = name   # Assigns the name passed to the name attribute
#         self.age = age     # Assigns the age passed to the age attribute
#
#     def bark(self):
#         print(f"{self.name} says woof!")
#
# # Creating an instance of Dog
# dog1 = Dog("Buddy", 3)
#
# # Accessing attributes
# print(dog1.name)  # Output: Buddy
# print(dog1.age)   # Output: 3
#
# # Calling a method
# dog1.bark()       # Output: Buddy says woof!
#
#
#
# class Person:
#     def __init__(self,name):
#         self.name = name
#     def talk(self):
#         print(f"Hi,I am {self.name}")
#
# k = Person("kondeti")
# # print(kiran.name)
# k.talk()
#
# v = Person("kiran")
# v.talk()



# Program without constructor
# class Faculty:
#     def putdata(self):
#         self.id=int(input("Enter faculty id: "))
#         self.name= input("Enter name: ")
#         self.salary=int(input("Enter salary: "))
#     def display(self):
#         print(f"faculty id: {self.id}")
#         print(f"faculty name: {self.name}")
#         print(f"faculty salary {self.salary}")
# a=Faculty()
# a.putdata()
# a.display()


# Program with constructor
# class Faculty:
#     def __init__(self):
#         self.id=int(input("Enter the ID: "))
#         self.name=input("Enter the name: ")
#         self.salary=input("Enter the salary: ")
#     def display(self):
#         print(f"faculty ID : {self.id}")
#         print(f"faculty name: {self.name}")
#         print(f"faculty salary: {self.salary}")
# a=Faculty()
# a.display()
#

class Computer:
    def __init__(self, CPU, RAM):
        self.cpu = CPU
        self.ram = RAM
    def config(self):
        print(f"Config is: {self.cpu} {self.ram}")
com1 = Computer('i5',16)
com2 = Computer('Ryren 3',8)

com1.config()
com2.config()
