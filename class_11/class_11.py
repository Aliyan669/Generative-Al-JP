# class MyClass:
#     pass

# instance_1 = MyClass()
# instance_1.xyz = "xyz_value"
# print(instance_1.xyz) # xyz_value

# instance_2 = MyClass()
# instance_2.xyz = "xyz_2_value"
# print(instance_2.xyz) # xyz_value

# instance_3 = MyClass()
# instance_3.abc = "abc_value"
# print(instance_3.xyz) # xyz_value


# class JawanPakAdmissionForm:
#     # class attribute
#     course = "Python Backend Course"
#     duration = "6 months"
#     contact = "0302"
#     website = "jawan.pk"

#     def __init__(self, name, dob, nic):
#     # Instance attribute
#         self.name = name
#         self.dob = dob
#         self.nic = nic
#         print(self)

# aliyan_form = JawanPakAdmissionForm("aliyan", "1998", "192")
# print(aliyan_form.__dict__)

# print(JawanPakAdmissionForm.name)
# print(JawanPakAdmissionForm.dob)

# aliyan_form = JawanPakAdmissionForm()
# abdullah_form = JawanPakAdmissionForm()

# aliyan_form.name = "aliyan"
# abdullah_form.name = "abdullah"

# print(aliyan_form.name)
# print(abdullah_form.name)

# JawanPakAdmissionForm.contact = "+92320"
# print(aliyan_form.contact)


# class MyClass:
#     pass

# obj = MyClass()
# print(obj.__dict__)

# obj.name = "aliyan"
# print(obj.__dict__)


# class JawanPakAdmissionForm:
#     # class attribute
#     course = "Python Backend Course"
#     duration = "6 months"
#     contact = "0302"
#     website = "jawan.pk"
#     name = "jawan"
#     __private_key = "&&%^&&^@@@!"

#     def __init__(self, name, dob, nic):
#         self.name = name
#         self.dob = dob
#         self.nic = nic

# def get_all_detail(self):
#     print("get_all_detail", self.__dict__)
#     return self.name + " "+ self.dob

# @classmethod
# def get_all_detail(cls):
#     print("get_all_detail", cls.__dict__)
#     return cls.name

# @classmethod
# def create_object(cls, param_4, param_5):
#     obj = Class_A()

#     cls(obj.xyz, "param 2", "para 3", param_4, param_5)

# @classmethod
# def get_private_key(cls):
#     return cls.__private_key


# aliyan_form = JawanPakAdmissionForm("aliyan", "1999", "192")
# aliyan_form.get_all_detail()

# abdullah_form = JawanPakAdmissionForm("abdullah", "1994", "192")
# print(aliyan_form.contact)

# JawanPakAdmissionForm.contact = "+92"
# print(aliyan_form.contact)

# aliyan_form.contact = "6543431"
# print(aliyan_form.contact)

# print(JawanPakAdmissionForm.contact)

# print(aliyan_form.__dict__)
# print(abdullah_form.__dict__)

# print(JawanPakAdmissionForm.__dict__)

# print(JawanPakAdmissionForm.__private_key)
# print(JawanPakAdmissionForm.get_private_key())

# print(JawanPakAdmissionForm._JawanPakAdmissionForm__private_key)


# OOP 4 pillars   (Inheritance, Polymorphism, Encapsulation, and Abstraction.)

# sub class
# inheritance

# class Employee:
#     def __init__(self, fname, lname, gender, nic, dob, salary, joining_date):
#         self.fname = fname
#         self.lname = lname
#         self.gender = gender
#         self.nic = nic
#         self.dob = dob
#         self.salary = salary
#         self.joining_date = joining_date

#     def get_salary(self):
#         return self.salary

# class Driver(Employee):
#     def __init__(self, fname, lname, gender, nic, dob, salary, joining_date, dln):
#         super().__init__(fname, lname, gender, nic, dob, salary, joining_date)

#         self.driving_licence_number = dln

#     def get_salary_15_days():
#         pass

#     def get_salary(self, *args):
#         if len(args) == 1:
#             get_salary_15_days()
#         return (int(self.salary) // 30) * 15


# # Employee()
# obj = Driver("muhammad", "danish", "male", "123",
#              "1994", "100", "2020", "100000")
# print(obj.lname)

# print(obj.get_salary())


# from abc import ABC, abstractmethod

# class Animal(ABC):
#     def __init__(self, name):
#         self.name = name

#     def eat(self):
#         print(self.name, "eating meal")

#     def sleep(self):
#         print(self.name, "sleeping ZzzZzZzz")

#     @abstractmethod
#     def move(self):
#         pass


# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def play_with_stick(self):
#         print(self.name, "bringing stick")

#     def move(self):
#         print(self.name, "walking in 4 legs")


# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def climb(self):
#         print(self.name, "climbing the tree")

#     def move(self):
#         print(self.name, "walking in 4 legs")


# class Fish(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def move(self):
#         print(self.name, "swiming")


# class Bird(Animal):
#     def __init__(self, name):
#         super().__init__(name)


# dog = Dog("dog")
# dog.eat()
# dog.sleep()
# # dog.climb()
# dog.play_with_stick()
# dog.move()


# cat = Cat("cat")
# cat.eat()
# cat.climb()
# # cat.play_with_stick()
# cat.move()


# fish = Fish("Fish")
# fish.move()


# bird = Bird("bird")
# bird.move()
