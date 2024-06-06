# Write a program to check whether a person is eligible to vote or not?

# age = 18

# age = int(input("Please Enter your age "))
# if age >= 18:
#    print("You are eligible to vote")
# else:
#    print("You are not eligible to vote") 



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



# Write a program to check the number is positive or negative. User input.

# a = int(input("Please Enter a number "))
# if a > 0:
#     print("Number is Positive ")
# else:
#      print("Number is Negative ") 



# Write a program to check whether a number is odd or even? Use Modulus Operator

# a = 8

# a = int(input("Please Enter a Number "))
# if a % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")



# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

# marks = 90

# marks = int(input("Please Enter Obtained Marks"))
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



# Write a program to check whether a number is divisible by 7

# num = int(input("Please Enter Your Number "))
# if num % 7 == 0:
#     print (num, "is divisible by 7 " )
# else:
#     print (num, "is not divisible by 7 " )



# Write a program to check if year is leap year.

# year = int(input("Please Enter Year "))
# if year % 4 == 0:
#     print ("Leap Year" )
# else:
#     print ("Not Leap Year" )


# Write a program to ask user its name and check whether name consists of 5 or more letters

# name = input("Please Enter Your Name ")

# if len(name) >= 5:
#     print ("Your Name consists of 5 or more letters" )
# else:
#     print ("Name Not Consists of 5 Letter" )



# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. 

# firstNumber = int(input("Enter you First Value "));
# secondNumber = int(input("Enter you Second Value "));
# operator = input("Enter you Opreate ex. Addition, Subtraction, Multiplication, Division ");

# if operator == "addition" or operator == "+" :
#     print(firstNumber + secondNumber);

# elif operator == "subtraction" or operator == "subtract" or operator == "-": 
#     print(firstNumber - secondNumber);

# elif operator == "multiplication" or operator == "multipliy" or operator == "x":
#     print(firstNumber * secondNumber)

# elif operator == "division" or operator == "divide" or operator == "÷": 
#     print(firstNumber / secondNumber);

# else:
#     print("Please select a valid operators")


# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# num = int(input("Please Enter Your Number "))

# if num % 2 == 0 and num % 3 == 0:
#     print (num, "is divisible by 2 & 3 " )
    
# elif num % 2 == 0:
#     print (num, "is divisible by 2 " )
    
# elif num % 3 == 0:
#     print (num, "is divisible by 3 " )
    
# else:
#     print (num, "is not divisible by 2 and 3 " )



# Write a program that accepts 2 inputs from user and check which number is largest.

# num1 = int(input("Please Enter Your Number "))
# num2 = int(input("Please Enter Your Number "))

# if num1 > num2:
#     print (num1, "is larger than " , num2 )

# elif num2 > num1:
#     print (num2, "is larger than " , num1 )
    
# else:
#     print (num1,"Both numbers are equal" , num2 )



# Write a program that accepts 3 input from user and check which number is largest.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if num1 >= num2 and num1 >= num3:
#     print("The largest number ",num1)
    
# elif num2 >= num1 and num2 >= num3:
#      print("The largest number ",num2)
     
# else:
#      print("The largest number ",num3)



# Write a program that accepts 3 input from user and check the second largest.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number: "))

# if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
#     print("The Second largest number is ",num1)
    
# elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
#      print("The Second largest number is ",num2)
     
# else:
#      print("The Second largest number is ",num3)
    

    
# Write a python program that accept user an input. The valid input should be of following

# user = input("Please Enter Your Color ").lower()
# print(user)

# if user == "green":
#     print("Car is allowed to go")
    
# elif user == "yellow":
#     print("Car has to Wait")
    
# elif user == "red":
#     print("Car has to Stop")
     
# else:
#      print("Invalid Input")



# Write a program that takes two numbers as input and prints:

# firstNumber = int(input("Please Enter Your First Number "))
# secondNumber = int(input("Please Enter Your Second Number "))

# if firstNumber > secondNumber:
#     print ( "First Number is Greater than Second Number"  )

# elif secondNumber > firstNumber:
#      print ( "Second Number is Greater than First Number"  )
    
# else:
#     print ("Both numbers are equal" )



# Write a program that takes a password as input and checks its strength:

# password = input("Please Enter Your Password  ")

# if len(password) < 6:
#     print ("Weak password" )
    
# elif len(password) >= 7 or len(password) <= 12 :
#     print ("Moderate password" )
    
# else:
#     print ("Strong password" )

    
# Write a program that takes an employee's salary and years of service as input. Calculate the bonus as follows:

# years= int(input("Enter year"))
# amount = 120000

# if years < 5: 
#     print("No Bonus")
    
# elif years >= 5 and  years < 10: 
#     print("Your Salary is",amount , "Your Bonus is 10% :", 0.10*amount, "Total Amount is", amount+ (0.10*amount))

# elif years >= 10 : 
#     print("Your Salary is",amount , "Your Bonus is 20% :", 0.20*amount ,"Total Amount is", amount+ (0.20*amount))



# Write a program that takes the total amount of a purchase as input and applies a discount:

# item = int(input("Enter purchase items amount"))

# if item < 100: 
#     print("No Discount ")
    
# elif item >= 100 and  item < 500: 
#     print("Your Items Price is",item , "Your Discount is 10% : " ,0.10*item ," Total Amount is", item- (0.10*item))

# elif item >= 500 : 
#     print("Your Items Price is",item , "Your Discount is 20%:  ",0.20*item, " Total Amount is", item- (0.20*item))



# Write a program that takes a person's age as input and prints the age group they belong to:


# age = int(input("Enter Your Age : "))

# if age < 13: 
#     print("Child")
    
# elif age >= 13 and  age <= 19: 
#     print("Teenager")

# elif age >= 20 : 
#    if age < 65: 
#     print("Adult")
#    elif age >= 65: 
#     print("Senior")



# Write a program that checks if a customer is eligible for a discount based on their membership status and purchase amount:
#  ?????