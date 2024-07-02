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
