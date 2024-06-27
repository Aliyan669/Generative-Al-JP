# Extracting Sublist from a List of Temperatures
# Objective: Given a list of daily temperatures for a month, extract the temperatures for a specific week (e.g., week 2).

# temperatures = [22, 24, 20, 25, 23, 26, 24, 25, 27, 29, 30, 28, 26, 27, 24, 23, 22, 21, 25, 24, 26, 27, 29, 28, 26, 25, 24, 23, 22, 21]
# print("Week 2 Temperture: ",temperatures[7:14])


# Extracting a Substring from a Sentence
# Objective: Given a sentence, extract and print a specific word using string slicing.
# sentence = "The quick brown fox jumps over the lazy dog"

# word = sentence.split()
# print("Third word is",word[2])


# Extracting a Sublist of Favorite Colors
# Objective: Given a list of favorite colors, extract a sublist of the first three colors using list slicing.
# favorite_colors = ["Red", "Blue", "Green", "Yellow", "Purple", "Orange"]
# extract first three colors

# print("First three colors: ",favorite_colors[0:3])


# Write a Python program to check if a list is empty or not.

# list = [1,2,3]

# if not list:
#         print("This list is empty.")
# else:
#         print("This list is not empty.")


# 1. output the numbers from 1 to 10 using range function and for loop
# output should be like
# 1
# 2
# 3
# etc

# for i in range(1,11):
#     print(i)


# 2. output the numbers from 35 to 50 using range function and for loop
# output should be like
# 35
# 36
# 37
# etc

# for i in range(35,51):
#     print(i)


# 3. output the numbers from -15 to -25 using range function and for loop
# output should be like
# -15
# -16
# -17
# etc

# for i in range(-15,-26,-1):
#     print(i)


# 4. output the numbers from 5 to -10 using range function and for loop
# output should be like
# 5
# 4
# 3
# etc

# for i in range(5,-11,-1):
#     print(i)


# 5. output the numbers from 0 to 50 incremented by 3 using range function and for loop
# output should be like
# 0
# 3
# 6
# 9
# etc

# for i in range(0,11,3):
#     print(i)


# 6.  Write a program to Generate Multiplication Table of 2 using range function and for loop
# output format should be like
# 2 x 1 = 2
# 2 x 2 = 4
# etc

# for i in range(1,11):
#     print(2,"x",i,"=",2*i)


# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop increment the value of x with the local variable of loop
# x += i

# list = [3, 5, 2, 1, 4]
# x= 0

# for item in list:
#     x += item
# print(x)


# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5
# hint:
# create a variable x outside the loop and assign the value 0
# inside the loop compare the variable x with the local variable of loop

# list =  [3, 5, 2, 1, 4]
# x = 0

# for item in list:
#     if item > x:
#         x = item
# print("Largest Number is", x)


# Exercise 1: Sum of Elements in a List
# Objective: Write a Python program that calculates the sum of all elements in a given list.
# Example list

# numbers = [10, 20, 30, 40, 50]
# total= 0
# for item in numbers:
#     total += item

# print("Total Number is",total)


# Count Even and Odd Numbers in a List
# Objective: Write a Python program that counts the number of even and odd numbers in a given list.
# Example list

# numbers = [12, 7, 9, 24, 18, 5, 3, 20]

# even_number = 0
# odd_number = 0

# for item in numbers:
#     if item % 2 == 0:
#         even_number += 1
#     else:
#         odd_number += 1
# print("Even Number ", even_number)
# print("Odd Number ", odd_number)


# Print List Elements with Their Indexes
# Objective: Write a Python program that prints each element of a list along with its index.
# Example list
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# output should like
# "Index: 0 Element: apple"
# "Index: 1 Element: banana"
# "Index: 2 Element: cherry"

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# for item in range(len(fruits)):
#     print("Index:",item, "Elements:", fruits[item])


# Create a List of Even Numbers from 1 to 20
# Objective: Write a Python program that creates a list of all even numbers from 1 to 20.

# for item in range(0,21,2):
#     print("Even Numbers", item)


# Find Common Elements Between Two Lists
# Objective: Write a Python program that finds and prints the common elements between two lists.
# Example lists

# list_1 = [1, 2, 3, 4, 5]
# list_2 = [4, 5, 6, 7, 8]

# for item_1 in list_1:
#     for item_2 in list_2:
#         if item_1 == item_2:
#             print("Common Number", item_1)


# Find the Length of Each String in a List
# Objective: Write a Python program that finds and prints the length of each string in a given list.
# Example list

# strings = ["apple", "banana", "cherry", "date"]
# for item in strings:
#     print(item , "Length is", len(item))


# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360
# hint: use a variable x outside the loop and assign the first value of list
# inside the loop * the value of x with the local variable of loop
# x *=

# list=[3, 5, 2, 1, 4]
# total= 3

# for item in list:
#     total *= item

# print("Total Calculation is",total)


# 2. create a list from 0 to 100 using range function and iterate over the list
# display the number that satisfied following conditions
# The number must be divisible by 5
# If the number is greater than 30 and less than 50 then skip it
# If the number is greater than 80, then stop the loop

# for item in range(101):
#     if item > 80:
#         break

#     if 30 < item < 50:
#         continue

#     if item % 5 == 0:
#         print(item)


# 3. consider the following list ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# display the word that contains character longer than 5
# the output should be freedeom and popcorn

# animal = ['cat', 'dog', 'hand', 'freedom', 'jump', 'frog', 'happy', 'popcorn', 'tiger']
# for item in animal:
#     if len(item) > 5:
#         print(item)


# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

# color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# for item in range(len(color)):
#     if item not in [0,4,5]:
#         print(color[item])


# 5. Write a program to display odd numbers only. odd number upto 100
# hint use for loop and range function

# for item in range(1,101,2):
#     print(item)


# 6. List contains 30 elements. Display first 5 and last 5 elements

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
# list= list(range(1,31))  # Second Method
# print("First 5 Elements",list[:5],"Last 5 Elements",list[-5:])


# 7. Display output: helloworld from the list ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
# output should be 'helloworld' in one line

# list = ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd']
# print( "".join(list))


# 8. Write a Python program to append a list to the second list.
# consider l1 is [1, 2, 3, 4, 5] and l2 is []
# using loop add items of l1 in l2

# list_1 = [1, 2, 3, 4, 5]
# list_2 = []

# for item in list_1:
#     list_2.append(item)
# print(list_2)


# 9. consider the list ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# use for loop and find the count that how many times the word "hi" present in list.
# output should be 3

# list =  ['hi', 'hello', 'hi', 'good morning', 'hi', 'bye']
# count = 0
# for item in list:
#     if item == 'hi':
#         count += 1
# print("Hi count",count)