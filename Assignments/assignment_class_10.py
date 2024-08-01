from datetime import datetime, date

# Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.

# class Person:

#     def __init__(self, name, country, dob):
#         self.name = name
#         self.country = country
#         self.dob = dob

#     def calulate_age(self):
#         dob_obj = date.fromisoformat(self.dob)
#         return date.today().year - dob_obj.year

# aliyan = Person("Aliyan", "Pakistan", "1992-08-25")
# print(aliyan.name)
# print(aliyan.calulate_age())


# Write a Python program to create a calculator class. Include methods for basic arithmetic operations

# class Calculator:
#     def add(self, a, b):
#         return a + b

#     def subtract(self, a, b):
#         return a - b

#     def multiply(self, a, b):
#         return a * b

#     def divide(self, a, b):
#         return a / b


# calc = Calculator()

# print("Addition: 10 + 5 =", calc.add(10, 5))
# print("Subtraction: 10 - 5 =", calc.subtract(10, 5))
# print("Multiplication: 10 x 5 =", calc.multiply(10, 5))
# print("Division: 10 / 5 =", calc.divide(10, 5))


# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.

# class ShoppingCart:
#     def __init__(self):
#         self.items = []

#     def add_item(self, name, price, quantity=1):
#         self.items.append({"name": name, "price": price, "quantity": quantity})

#     def remove_item(self, name):
#         self.items = [item for item in self.items if item["name"] != name]

#     def calculate_total(self):
#         total = sum(item["price"] * item["quantity"] for item in self.items)
#         return total

#     def __str__(self):
#         cart_contents = "\n".join(
#             [f'{item["quantity"]}x {item["name"]}: ${item["price"] * item["quantity"]:.2f}' for item in self.items]
#         )
#         return f"Shopping Cart:\n{cart_contents}\nTotal: ${self.calculate_total():.2f}"

# cart = ShoppingCart()
# cart.add_item("Apple", 0.99, 3)
# cart.add_item("Banana", 0.50, 5)
# cart.add_item("Orange", 1.25, 2)

# print(cart)

# cart.remove_item("Banana")

# print("\nAfter removing bananas:")
# print(cart)


# Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.

# class Bank:
#     def __init__(self):
#         self.customers = {}

#     def add_customer(self, name):
#         if name in self.customers:
#             print(f"Customer {name} already exists.")
#         else:
#             self.customers[name] = 0.0
#             print(f"Customer {name} added.")

#     def deposit(self, name, amount):
#         if name in self.customers:
#             if amount > 0:
#                 self.customers[name] += amount
#                 print(f"Deposited ${amount:.2f} to {name}'s account.")
#             else:
#                 print("Deposit amount must be positive.")
#         else:
#             print(f"Customer {name} does not exist.")

#     def withdraw(self, name, amount):
#         if name in self.customers:
#             if amount > 0:
#                 if self.customers[name] >= amount:
#                     self.customers[name] -= amount
#                     print(f"Withdrew ${amount:.2f} from {name}'s account.")
#                 else:
#                     print(f"Insufficient funds in {name}'s account.")
#             else:
#                 print("Withdrawal amount must be positive.")
#         else:
#             print(f"Customer {name} does not exist.")

#     def check_balance(self, name):
#         if name in self.customers:
#             balance = self.customers[name]
#             print(f"{name}'s account balance: ${balance:.2f}")
#         else:
#             print(f"Customer {name} does not exist.")

# bank = Bank()

# bank.add_customer("Aliyan")
# bank.deposit("Aliyan", 1000)
# bank.withdraw("Aliyan", 200)
# bank.check_balance("Aliyan")
