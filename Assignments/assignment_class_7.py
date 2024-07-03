# loop
# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]

# list = [100, 200, 300, 400, 500]
# for item in range(len(list)):
#     print(item, list[item])


# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

# l1 = ['a', 'b', 'c', 'd']
# l2 = ['e', 'b', 'g', 'd', 'f', 'h']

# common_counts = {}
# combined_list = l1 + l2

# for item in combined_list:
#     count = 0
#     for element in l1:
#         if item == element:
#             count += 1
#     for element in l2:
#         if item == element:
#             count += 1
#     common_counts[item] = count
# print(common_counts)


# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

# x = 2783
# count = 0

# while x != 0:
#     count += 1
#     x //= 10
# print("Total number of digit", count)


# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

# while True:
#     inp = input("Enter a value (if you want to stop enter 0) ")

#     if inp == "0":
#         break
#     print("your Value", inp)

# print("Program Closed")


# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

# list = []
# count = 0

# while count < 5:
#     inp = int(input("Enter a number "))
#     list.append(inp)
#     count += 1

# total = sum(list)
# # print(list)
# print("Total Calculate is:",total)


# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

# while True:
#     name = input("Enter a name (You want to end the program so please enter 'End') " )
#     if name == "End":
#         break

#     print(name)
# print("I am done")


# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

# l1 = [11, 33, 50]
# string = ""
# for item in l1:
#     string += str(item)
# print(string)


# consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

# animal = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# for item in animal:
#     if len(item) > 5:
#         print(item)


# functions

# Write a program to create a function that takes two arguments, name and age. print them inside function.

# def Detail(name, age):

#     print("Name is:", name)
#     print("Age is:", age)

# Detail("Aliyan", 23)


# It should accept the employee’s name and salary and display both.
# If the salary is missing in the function call then assign default value 9000 to salary

# def Epmloye_Detail(name , salary = 9000):
#      print("Employee Name is:", name , "Employee salary is:", salary)

# Epmloye_Detail("Aliyan",5000)
# Epmloye_Detail("Basit")


# Write function that accepts different values as parameters and returns a list
# consider the below varables
# a = 4
# b = 8
# c = 10
# d = 12
# pass above values to the function and return the list
# output: [4, 8, 10, 12]

# a = 4
# b = 8
# c = 10
# d = 12

# def why(*arg):
#     return list(arg)

# result = why(a, b, c, d)
# print(result)


# Write a function called km_to_miles that takes kilometers as a parameter, converts it into miles and returns the result.

# def Kilometer(kilo):

#     mile = kilo * 0.621371
#     return mile

# kilo = 6
# result = Kilometer(kilo)
# print(kilo,"Kilometer is equal to",result, "Miles")


# Write a function called is_divisable_by_11 that takes an integer as an parameter and returns whether it is divisible by 11 or not.

# def Divi(num):
#     if num % 11 == 0:
#         return True
#     else:
#         return False

# result = Divi(21)
# print(result)


# Write a function called get_highest that takes 2 numbers as parameters and returns the highest of the 2 numbers.

# def Highest(num1, num2):
#     high = max(num1, num2)
#     return high

# result = Highest(21, 33)
# print("Highest Number is:", result)


# Write a function called fuel_cost that takes 2 numbers as parameter "distance" as required arg
# and "fuel_per_liter" as optional arg that has default value to 280.
# The function should return the cost in Rs.

# def Price(distance, fuel=280):
#     cal = distance*fuel
#     return cal

# dist = 10
# fuel = 290
# result = Price(dist, fuel)
# print("Total Distance is:", dist, "Fuel Price per Liter",fuel, "Total Cost is:", result)


# Write a function called is_valid_email  that takes an email address as an argument and returns True/False depending on whether it is a valid email address.
# Check rules:
# Must contain at least 1 character before the at symbol
# Must contain an @ symbol
# Must have at-least 1 character after the @ symbol and before the period(.)
# Must contain at least 1 character after the last period(.).
# Maximum 256 characters
# Must start with a letter or a number

# def is_valid_email(email):
#     if len(email) > 256:
#         return False

#     if "@" not in email:
#         return False

#     local_part, domain_part = email.split('@', 1)

#     if not local_part or not domain_part:
#         return False

#     if not local_part[0].isalnum():
#         return False

#     domain_sections = domain_part.split('.')

#     if len(domain_sections) < 2 or not all(domain_sections):
#         return False

#     return True

# # Example usage
# emails = [
#     "example@example.com",
#     "user.name@domain.co",
#     "username@domain.com.",
#     "@example.com",
#     "user@.com",
#     "user@domain.c",
#     "user@domain..com",
#     "user@domain.comextracharactersbecauseitisalongemailaddressandisnotvalid",
#     "user@domain.c0m",
#     "userdomain.com",
#     "user@domaincom"
# ]

# email_results = {email: is_valid_email(email) for email in emails}
# print(email_results)


# Take a variable store i.e
# Store = {“name”: “my store”, “inventory”: [], “orders”: []}

# Add 5 items in the inventory using a function “add_item”
# id, name, price and quantity

# Store = {
#     "name": "my store",
#     "inventory": [],
#     "orders": []
# }

# def add_item(store, item_id, name, price, quantity):
#     list = {
#         "id": item_id,
#         "name": name,
#         "price": price,
#         "quantity": quantity
#     }
#     store["inventory"].append(list)

# add_item(Store, 1, "Apple", 0.5, 100)
# add_item(Store, 2, "Banana", 0.3, 150)
# add_item(Store, 3, "Orange", 0.7, 120)
# add_item(Store, 4, "Mango", 1.2, 80)
# add_item(Store, 5, "Grapes", 2.0, 200)

# print(Store)


# Take user input unless it says “done”
# Display user updated inventory items every time
# Ask user to type id of the item to purchase or type “done” to checkout
# Each time only 1 quantity will by subtracted from the item
# Functions: add_item_in_inventory, add_item_in_basket(), checkout()
# On checkout, print “{quantity} {item} sold in {store}”

# Define the Store dictionary
# Store = {
#     "name": "my store",
#     "inventory": [],
#     "orders": []
# }

# # Define the add_item function
# def add_item(store, item_id, name, price, quantity):
#     item = {
#         "id": item_id,
#         "name": name,
#         "price": price,
#         "quantity": quantity
#     }
#     store["inventory"].append(item)

# # Function to display the current inventory
# def display_inventory(store):
#     print("Current Inventory:")
#     for item in store["inventory"]:
#         print(f"ID: {item['id']}, Name: {item['name']}, Price: {item['price']}, Quantity: {item['quantity']}")

# # Function to purchase an item
# def purchase_item(store, item_id):
#     for item in store["inventory"]:
#         if item["id"] == item_id:
#             if item["quantity"] > 0:
#                 item["quantity"] -= 1
#                 store["orders"].append(item)
#                 print(f"Purchased 1 {item['name']}.")
#             else:
#                 print(f"{item['name']} is out of stock.")
#             break
#     else:
#         print("Invalid item ID.")

# # Adding items to the inventory
# print("Add items to the inventory. Type 'done' to finish.")
# while True:
#     item_id = input("Enter item ID: ")
#     if item_id.lower() == "done":
#         break
#     name = input("Enter item name: ")
#     price = float(input("Enter item price: "))
#     quantity = int(input("Enter item quantity: "))
#     add_item(Store, int(item_id), name, price, quantity)

# # Display the inventory
# display_inventory(Store)

# # Purchase items
# print("Type the item ID to purchase an item, or 'done' to checkout.")
# while True:
#     user_input = input("Enter item ID to purchase or 'done' to checkout: ")
#     if user_input.lower() == "done":
#         break
#     purchase_item(Store, int(user_input))
#     display_inventory(Store)

# print("Checkout complete. Thank you for your purchase!")
