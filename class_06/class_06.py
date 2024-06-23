# class task before starting Dict + loop class


# print multiplication table of 3

# num = 3 
# for i in range(1,11):
#     print(num , "x" , i , "=" , num*i )


# Iterate over the list and print "var index:{inddex}, item: {item}"

# list = ["a", "b", "c"]
# for i  in range(len(list)):
#     print(i ,list[i] ) 


#check if pakola is there. if found print "pakola is there"

# cold_drink = ["Pepsi", "Pakola", "Marinda","7up","Sprit", "Dew"]

# for i  in cold_drink:
#    if i == "Pepsi":
#     print("Pepsi is There")

# x = 1
# print("2 x 1 =", (2 * x))
# print("2 x 2 =", (2 * (x + 1)))
# print("2 x 3 =", (2 * (x + 2)))
# print("2 x 4 =", (2 * (x + 3)))
# print("2 x 5 =", (2 * (x + 4)))

# for i in range(1, 21, 2):
#     print("2 x", i,"=", 2 * i)

# arr = ["sofa", "chair", "table", "bed"]
# print(arr[0])
# print(arr[1])
# print(arr[2])
# print(arr[3])

arr = ["sofa", "chair", "table", "bed"]
# i = 0
# print(arr[i]) # sofa

# i += 1
# print(arr[i]) # chair

# i +=1
# print(arr[i]) # table


# for i in range(0, len(arr), 1):
#     print(arr[i])
    
# explicit vs implicit

# for i in range(len(arr)):
#     print(arr[i])
    

# for item in arr:
#     print(item)


# cold_drinks = ["pepsi", "marinda", "pakola", "7up", "sprit", "dew"]
#check if pakola is there. if found print "pakola is there"

# print("starting main code")
# for item in cold_drinks:
#     print("finding pakola")
#     if item == "pakola":
#         print("pakola is present")
#         break          # Condition is match statemnet is break 
# print("running the main code")

# finding pakola
# pakola is present


# arr = [1, 2, 3, 4, 5, 6, 7, 8]
# for item in arr:
#     if item  == 2 or item == 6 or item == 8:
#         continue

#     print(item)


emails = ["user_1@gmail.com", "user_2@gmail.com", "user_3", "user_4@gmail.com", "admin@gmail.com","user_5", "user_6@gmail.com"]

# send email to all users who has valid email
# send email to only admin


# for item in emails:
#     if "@" not in item: #item.find("@") == -1:
#         continue
#     print("Sending email to this user" , item)

# for item in emails:
#     if item.find("admin") > -1:
#         print("Sending email to this admin" ,item)
#         break


# Data Structure Dictionary

# student = ["Aliyan", 10, True, 40.5, None]    #List

# student_data = {       #Dictionary
#   #key  :  #Value               
#  "name" : "Aliyan",
#  "age" : 10 ,
#  "is_employed" : True,
#  "weight": 40.6,
#  "student" : None
# }

# print(student_data)

# print("Age is",student_data["age"])
# print(student_data["student"])

# student_data['weight'] = 70   #Update Value
# print(student_data)

# student_data["height"] = "5ft"   #Add New Value
# print(student_data)


#Nested Dictionary

# data = {
#  "name" : "Aliyan",
#  "age" : 10 ,
#  "is_employed" : True,
#  "weight": 40.6,
#  "sudent" : None,
#  "Siblings" : ["fahad","ahmed","umar"],
#  "employe_detail":{
#     "id": 100,
#     "salary": 40000,
#     "department": "IT",
#     "manager_of": ["Aliyan","Abdullah","Basit"]
#  }


# print(data["Siblings"][1])
# print(data["employe_detail"]["salary"])
# print(data["employe_detail"]["manager_of"][1])