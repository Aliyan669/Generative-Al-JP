# dictionary common methods

# dictt = {
#     "Aliyan": 200,
#     "Amir": 400,
#     "Basit": 600,
#     "Books": ["1", "2", "3"]
# }

# print(dictt.keys())
# print(dictt.values())
# print(dictt.items())


# for key, val in dictt.items():
#     print(key, "=>", val)


# Update the dictionary value

# dictt['Books'] = ["1", "2", "3", "4"]
# dictt.update({"Books": ["1", "2", "3", "4"]})
# print(dictt)


# loop using enumerate on list and dict

# arr = [200,100,300,400]


# for i in range(len(arr)):
#     print(i, arr[i])

# for key,val in enumerate(arr):
#     print(key , val)


# for i, (key, value) in enumerate(dictt.items()):
#     print(i, key)


# students = ["Aliyan","Ahmed","Maha"]
# scores = [60,50,20]
# dictt = {
#     "student":[],
#     "score":[]
# }

# for key,val in  enumerate(students):
#     dictt["student"]=students[key]
#     dictt["score"]=scores[key]
#     print(dictt)

# Zip function: loop over multiple list Research on Internet


# loop will run forever

# while True:
#     print("hello world")

# x = 1
# while x > 0 and x <= 10:
#     x += 1
#     print(x,"hello world")

# x = 10
# while x > 0:
#     x -= 1
#     print(x, "hello world")


# ask user input postive number and keep asking positive number and display
# terminate the program when user input negative number

# user_number = int(input("enter positive number "))
# while user_number > 0:
#     print(user_number)
#     user_number = int(input("enter positive number "))


# while True:
#     user = int(input("Please Enter the Number"))
#     if user < 0:
#      break
#      print(user)


# Find the Common Number

# list_1 = [10,20,30]
# list_2 = [40,20,50,60]
# common = []

# for item in list_1:
#    if item in list_2:
#       common.append(item)
#       print("Common Number", common)

# This solution is brootforce
# for item_1 in list_1:
#     for item_2 in list_2:
#         if item_1 == item_2:
#             print("Common Number", item_1)


# order_1_destination = "China"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# order_1_destination = "New York"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# order_1_destination = "China"

# if order_1_destination == "New York":
#     shipment_price = 10
# elif order_1_destination == "California":
#     shipment_price = 20
# elif order_1_destination == "China":
#     shipment_price = 30
# print(shipment_price)


# order_1_destination = "China"
# locations = ["New York", "California", "China"]

# shipment_price = 0
# for loc in locations:
#     if loc == order_1_destination:
#         shipment_price = 10
#     elif loc == order_1_destination:
#         shipment_price = 20
#     elif loc == order_1_destination:
#         shipment_price = 30

# print(shipment_price)


# order_1_destination = "China"
# locations = ["New York", "California", "China"]
# shipment_price = 0

# def get_shipping_price():
#     for loc in locations:
#         if loc == order_1_destination:
#             shipment_price = 10
#         elif loc == order_1_destination:
#             shipment_price = 20
#         elif loc == order_1_destination:
#             shipment_price = 30
            
# print(shipment_price)
# get_shipping_price()


# local vs global


# def multiply():
#     global x
    # print("hello world")
    # print(x * y)
   
#     x = 100
#     print(x)


# x = 2
# y = 5

# print( x * y)
# print(x)

# multiply()

# print(x)


# x  = 100
# y = 100


# x = "hello"

# def modify_string(xx): # calle
#     print(xx)
#     xx = xx + " world"
#     print(xx)
#     return xx

# x = modify_string(x) # caller
# print(x)


# Impure function vs Pure function

# def get_shippment_price(order_1_destination):
#     if order_1_destination == "New York":
#         shipment_price = 10
#     elif order_1_destination == "California":
#         shipment_price = 20
#     elif order_1_destination == "China":
#         shipment_price = 30
#     print(shipment_price)
#     return shipment_price


# def calculate_overall_order_tax(total_price, shipment_rate):
    
#     print(total_price*shipment_rate)
    
# shipment_price = get_shippment_price("China")

# calculate_overall_order_tax(100, shipment_price)


# x = 5
# y = 3

# def calculate(a,b):
#     print(a+b)
#     print(a-b)
#     print(a*b)
    
# calculate(x,y)
    
    
# def do_sum(*abc): #Multiple Arguement Get (*)
#    print(abc)
    

# do_sum(1, 2, 3, 4, 5,6 ,7 ,8)   