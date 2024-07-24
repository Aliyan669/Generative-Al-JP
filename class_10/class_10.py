# local vs global variable

# x = 100   #Global

# def sum():
#     y  = 200  #Local
#     print(y)

# print(y)


# def increment():
#     counter = 0
#     counter += 1
#     print(counter)

# increment()


# counter = 100
# def increment():
#     counter = 300
#     print(counter)


# counter = 0
# def increament():
#     global counter
#     counter += 1
#     print(counter)

# increament()
# increament()
# increament()


# Object Oriented Programming  (OOPS)
# ek dusra method program Likhna ka


# Class Syntax in Python OOP
# class MyClass: #passcal case
#     pass
# x = MyClass()


# class ColdDrink:
#     height= 100
#     color = "Black"
#     taste = "Salty"    # this is Class Attributes  (Shared Attributes)
#     body = "Plastic"
# print(ColdDrink.taste)


# pepsi = ColdDrink() # this is product
# print(pepsi.color)

# sprite = ColdDrink() # this is product
# print(sprite.color)
# sprite.color = "White"
# print(sprite.color)


# class Employee:
#     bonus_amount = 10

#     def __init__(self, _id, _name, _salary):
#         # Instance Attributes
#         self.id = _id
#         self.name = _name
#         self.salary = _salary

#     def get_tax_amount(self):
#         return float(self.salary) * 0.1

#     # behavour
#     def get_salary(self):
#         tax_amount = self.get_tax_amount()
#         return self.salary - tax_amount


# taha_info = Employee(1, "Taha", 20000)
# aliyan_info = Employee(1, "Aliyan", 30000)

# print(taha_info.name)
# print(taha_info.bonus_amount)

# Employee.bonus_amount = 20
# print(taha_info.bonus_amount)

# print(taha_info.get_salary(), taha_info.salary)
# print(aliyan_info.get_salary(), aliyan_info.salary)


"""
Write a Python program to create a person class. 
Include attributes like name, country and date of birth. 
Implement a method to determine the person's age.
"""

# from datetime import datetime, date

# class Person:
#     _dob = "1995-01-01"
#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob

# instance method

# def calulate_age(self):
#     dob_obj = date.fromisoformat(self.dob)
#     return date.today().year - dob_obj.year

# class method

# @classmethod
# def calulate_age(cls, dob):
#     dob_obj = date.fromisoformat(dob)
#     return date.today().year - dob_obj.year

# aliyan = Person("dansh", "Pakistan", "1992-08-25")
# fahad = Person("fahad", "Pakistan", "1990-08-25")

# instance method

# print(aliyan.name)
# print(aliyan.calulate_age())
# print(fahad.calulate_age())


# class method

# print(Person._dob)
# print(Person.calulate_age(aliyan._dob))
# print(Person.calulate_age(fahad._dob))


# lifecycle of the object

# class MyClass:

#     def __new__(cls):
#          print("Creating instance")
#          return super(MyClass, cls).__new__(cls)

#     def __init__(self):
#         print("Init is called")

#     def __str__(self):
#         return f"MyClass id:{self.id}"

#     # destructor
#     def __del__(self):
#         print("Deleting the object")

# obj = MyClass()

# obj.id = 100
# print(obj)
