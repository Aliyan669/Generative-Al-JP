# List Datatype

#  fruit_1 = "apple"
#  first_2 = "orgage"


# list
# syntax: [ ]


# list Creation

# fruits = ["Apple","Mango", "Banana"]
# print("Fruit",fruits)

# age = [20,30,40]
# print("Age",age)

# student = ["Aaliyan", 40, True, 30.5, None, ["new_list", "item 2"]]
# print("Student",student)


# Read
# items store in the list as location 0, 1, 2, 3, .... n
# indexs: 0, 1, 2, 3, ..... n
# Static data vs Synamic data
# Declaration vs Initialization
# Python doesn't have Declaration Syntax
# Index Starting at 0


# fruits = ["Apple","Mango", "Banana"]
# print(fruits[0]) 
# print(fruits[1]) 
# print(fruits[2])
# print(fruits[3]) # It will raise error "Index out of Range"


# Find the length of list using     len()
 
# fruits = ["Apple","Mango", "Banana"]
# print(len(fruits)) 


# print(fruits[len(fruits) - 1])

# last_element = len(fruits) - 1
# print(last_element)

# print(fruits[last_element])

# print(fruits[-1])


# Update List 

# fruits = ["Apple","Mango", "Banana"]

# fruits[0] = "Kiwi"
# print(fruits)


# Delete element on List using     del()

# fruits = ["Apple","Mango", "Banana"]

# del fruits[0]
# print(fruits)


# Slice

# fruits = ["Apple","Mango", "Banana"]

# last_element_index = len(fruits) - 1
# last_element = fruits[last_element_index] # ["new_list", "item 2"]

# print(len(last_element))

# last_element = "updated_value"

# print(last_element)


# Add New Element on List using       append()

# fruits = ["Apple","Mango", "Banana"]

# fruits.append("Strawberry")
# print(fruits)


# Remove Last Element on List using      pop()

# fruits.pop()
# print(fruits)


# Extend on List using      extend()

# list_2 = []
# list_2.extend(fruits)
# print(list_2)

# list_3 = ["Aliyan", "Amir", "imran", "Nihal"]
# list_3.extend(list_2)
# print(list_3)

# print("list_3", list_3)
# print('list_2', list_2)

# list_2 = list_2 + list_3
# print(list_2)


# Sorting on List using      sort() 

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# print(names_list)

# names_list.sort()  # by default ascening order
# print(names_list)

# names_list.sort(reverse=True)
# print(names_list)


# Find Elemnet Index Number by Value on List using      index()

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# print("find by value:", names_list.index("Javed"))


# Remove Element by Value on List using      remove()

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# names_list.remove("Javed")
# print(names_list)


# Remove All Element on List using      Clear()

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# print(names_list)

# names_list.clear()
# print(names_list)


# Count Duplicate on List  using        count()

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal","Akif"]
# print("Count Duplicate", names_list.count("Akif"))


# Insert at Defined Position using       insert()

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# names_list.insert(2, "Hanif")
# print(names_list)


# Class Task

# create a list of juices, add 5 items using append
# creat a list of cars, add 3 items using insert
# remove last time from the list ["bed", "table", "chair", "sofa"] using pop and len
# remove the item "chair" from the list ["bed", "table", "chair", "sofa"] using del and remove


# create a list of juices, add 5 items using append

# juices = []

# juices.append("Apple")
# juices.append("Lemon")
# juices.append("Mango")
# juices.append("Strawberry")
# juices.append("Watermelon")

# print(juices)


# creat a list of cars, add 3 items using insert

# cars = []
# cars.insert(0, "Honda")
# cars.insert(1, "Ferarri")
# cars.insert(2, "Toyota")

# print(cars)


# Remove last time from the list ["bed", "table", "chair", "sofa"] using pop and len

# furniture = ["bed", "table", "chair", "sofa"]
# furniture.pop()
# print(furniture)

# del furniture[len(furniture) - 1]
# print(furniture)


# remove the item "chair" from the list ["bed", "table", "chair", "sofa"] using del and remove

# furniture = ["bed", "table", "chair", "sofa"]
# furniture.remove("chair")
# print(furniture)


# chair_index = furniture.index("chair")
# del furniture[chair_index]
# print(furniture)


# Slice Element Check using   (in)    and return  True/False
 
# furniture = ["bed", "chair", "table"]
# print("pepsi" in furniture)

# value in list

# print("bed" in furniture)


 # "C" != "c" # case sensitive
 
 
# slice

# syntax: varibale[start_from : till]

# Exclusive vs Inclusive


# car_list = ["corolla", "mehran", "cultus", "aqua", "civic", "vitz", "alto"]
# print(car_list)
# print(car_list[0:3])   #first Index Number Second Length


# print(car_list[:3])
# print(car_list[3:])


# x = "hello world"
# print(x[4:10])

# print("helloo" in "hello world")


# student_detail = "Aliyan, 30, 40.5, True"
# detail_list = student_detail.split(",")
# print(detail_list)


# print("--".join(detail_list))


# Loop on List 

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# print(names_list[0])
# print(names_list[1])
# print(names_list[2])
# print(names_list[3])


# for i in ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]:
#     print(i)

# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]

# for i in names_list:
#     print(i)

# print(list(range(10)))

# print(range(len(names_list)))


# for item in ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]:
#     print(item)


# names_list = ["Aliyan", "Akif","Javed","Basit","Tahir","Nihal"]
# for i in range(len(names_list)): # [0, 1, 2, 3, 4, 5]
#     print(names_list[i])


# loop over Furniture
# Check if chair exists or not

# furtniture = ["bed", "table", "chair", "sofa"]

# for item in furtniture:
#     if "chair" in item:
#         print("Chair Exists")