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


class Employee:
    bonus_amount = 10

    def __init__(self, _id, _name, _salary):
        # Instance Attributes
        self.id = _id
        self.name = _name
        self.salary = _salary

    def get_tax_amount(self):
        return float(self.salary) * 0.1

    # behavour
    def get_salary(self):
        tax_amount = self.get_tax_amount()
        return self.salary - tax_amount


taha_info = Employee(1, "Taha", 20000)
aliyan_info = Employee(1, "Aliyan", 30000)

print(taha_info.name)
print(taha_info.bonus_amount)

# Employee.bonus_amount = 20
# print(taha_info.bonus_amount)

# print(taha_info.get_salary(), taha_info.salary)
# print(aliyan_info.get_salary(), aliyan_info.salary)
