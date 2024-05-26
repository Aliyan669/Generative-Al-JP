# Python Vs code Extensions

"""
Extensions:
1. Python (by microsoft)
2. Code Runner
3. Kite AutoComplete AI Code
4. Python Snippets
5. Python Indent
"""

# Arithmatic operator

# Exponention  (**)
 
# print(2 ** 3) # 2 * 2 * 2 
# print(2 ** 4) # 2 * 2 * 2 * 2


# Modulus (%)

# print(10 % 4) 

# Even 
# print(10 % 2)
#  10 - 2 = 8
#  8 - 2 = 6
#  6 - 2 = 4
#  4 - 2 = 2
#  2 - 2 = 0

# Odd 
# print(5 % 2)
#  5 - 2 = 3
#  3 - 2 = 1


# Cyclic Rotation

# print("0 % 2 = ", (0 % 2)) 
# print("1 % 2 = ", (1 % 2)) 
# print("2 % 2 = ", (2 % 2)) 
# print("3 % 2 = ", (3 % 2)) 
# print("4 % 2 = ", (4 % 2)) 
# print("5 % 2 = ", (5 % 2)) 
# print("6 % 2 = ", (6 % 2)) 
# print("7 % 2 = ", (7 % 2)) 


# Find the last Digit

# a = 324
# print(a % 10) 


# Assignment Operator

# a = 50   
# a += 100
# print(a)


# Comparison Operators

# ==  (Equal to)
# != (Not Equal to)
# >  (Greater than)
# <  (Less than)
# >= (Equal to Greater than)
# <= (Equal to Less than)

# ==  (Equal to)
# a = 50
# b = 50
# print(a == b) # true

# a = "100"
# b = 100
# print(a == b)  #Type not match str and int

# a = "100"
# b = "100"
# print(a == b) #true

# != (Not Equal to)
# a = 50
# b = 10
# print(a != b) #true

# >  (Greater than)
# a = 50
# b = 10
# print(a > b) #true

# <  (Less than)
# a = 50
# b = 10
# print(a < b) #false

# >= (Equal to Greater than)
# <= (Equal to Less than)
# a = 50
# b = 50
# print(a >= b)
# print(a <= b)


# Logical Operators

# and  (dono contdition true hogi jab hi true ayega)
# or   (dono contdition true hogi ya ek bhi true hogi jab hi true ayega)

# a= 20
# b= 10
# c= 50

#and
# print( a > b and a > c) # False
# print( a > b and a < c) # true

#or
# print( a > b or a > c) # true
# print( a > b or a < c) # true

# print((a > b and a > c) or b < a) # False, True

# print(a < b and (a > c or b < a)) # False and True


# Task
# a = True
# b = True
# c = False
# d = False

# print(a and b) # true
# print(a or b) # true
# print(a or c) # true
# print(a and d) # false
# print((a and b )or c) # true
# print((a or b) and c) # false   


# if Statement Syntax 

# if condition: # which should evaluate to True/False. Only work with comparison operators
#     print("true") # if body
    
# a = 10
# b = 10
# if a == b:
#     print("Successfull")

# a = 10
# b = 20
# if a > b:
#     print("b is greater than a")
# else:
#     print("a is less than b")
    

# Write a program to check the number is positive.

# a = 50000

# a = int(input("Please Enter a number "))
# if a > 0:
#     print("Number is Positive ")
# else:
#      print("Number is Negative ") 
    
    
# Write a program to check whether a person is eligible to vote or not?

# age = 18

# age = int(input("Please Enter your age "))
# if age >= 18:
#    print("You are eligible to vote")
# else:
#    print("You are not eligible to vote") 


# Write a program to check whether a number is odd or even? Use Modulus Operator

# a = 8

# a = int(input("Please Enter a Number "))
# if a % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")


# elif Example

# marks = 90
# if marks >= 80:
#     print("A+")
# elif marks >= 70:
#     print("A")
# elif marks >= 60:
#     print("B")
# elif marks >= 50:
#     print("C")
# else:
#     print("no grading")


# Write a program to check char is vowel or not. - elif

# vowel chars are
# 1. a
# 2. e
# 3. i
# 4. o
# 5. u

# char = input("Enter a Vowel Number ")

# if char == "a":
#     print("Vowel")
# elif char == "e":
#     print("Vowel")
# elif char == "i":
#     print("Vowel")
# elif char == "o":
#     print("Vowel")
# elif char == "u":
#     print("Vowel")
# else:
#     print("Not Vowel")


# Second Method

# char = input("Enter a Vowel Number ")

# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
#     print("Vowel")
# else:
#     print("Not Vowel")
    
    





