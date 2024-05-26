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
a = True
b = True
c = False
d = False

print(a and b) # true
# print(a or b) # true
# print(a or c) # true
# print(a and d) # false
# print((a and b )or c) # true
# print((a or b) and c) # false