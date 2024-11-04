from IPython.lib.pretty import Printable
from jedi.api.helpers import CompletionParts


#
# class Student:
#     def __init__(self):
#         print("Adding new student in Database...")
#     name = input("Enter the name: ")
#     age = int(input("Enter age: "))
#
# s1 = Student()
# print(s1.name)
# print(s1.age)

# class Car:
#     color = input("enter the car color: ")
#     brand = input("Enter the car brand: ")
#     price = int(input("Enter the car price: "))
#
# car1 = Car()
# print(car1.color)
# print(car1.brand)
# print(car1.price)

class Computer:
    def config(self):
        print("Mac M3 pro 512SSD ")

com1 = Computer()
com2 = Computer()
Computer.config(com1)
Computer.config(com2)
com1.config()
com2.config()
