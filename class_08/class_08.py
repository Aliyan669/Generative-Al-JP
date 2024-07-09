# File Handling and Error Handling

# r   (read)
# w   (write)
# a   (update)


# file Handling Common Methods

# read()         read this file only
# readlines()    read this multiple lines and retun in list
# readline()     read only first line
# write()
# writelines() # can take list of str as input
# close()
# flush()
# seek() # set pointer position
# tell() # returns current pointer position


# # reading a file

# f = open("sample.txt", "r")

# data = f.read() # get all file data
# print(data)


# Jab File exist nhi karti hogi tu excution ka error ata hai
# try:
#     f = open("sample.txt", "r")
#     data = f.read()
#     print(data)
# except Exception as e:
#     print("exception caught", e)


# readlines()

# f = open("sample.txt", "r")
# data = f.readlines()
# print(data)


# readline()

# f = open("sample.txt", "r")
# data = f.readline()
# print(data)

# data = f.readline()
# print(data)


# f = open("sample.txt", "r")
# data = f.readline()
# while data:
#     print(data)
#     data = f.readline()


# write()

# f =  open("sample.txt", "w")
# f.write("address 1\n")
# f.write("address 2")

# f =  open("sample.txt", "r")
# data = f.read()
# print(data)

# f.read()
# f.seek(0)


# Update

# f = open("sample.txt", "a")
# f.write("\nAliyan")


# write()
# close()
# flush()
# seek()
# tell()


# import traceback
# try:
#     f = open('book_1.txt')
#     s = f.readline()
#     i = int(s.strip())
#     call_the_functio_that_doesnt_exist()
# except OSError as err:
#     print("OS error danish:", err)
# except ValueError:
#     print("Could not convert data to an integer.")
# except Exception as err:
#     # print(f"Unexpected {err=}, {type(err)=}")
#     # traceback.print_exc()
#     x = traceback.format_exc()
#     print(x)
#     # raise Exception("something went wrong on server")
# finally:
#     print("finally")

# print("hellow worl 2")

# Throw error from code
# raise Exception("This is an error")


# class task

# try:
#     f = open("book_1.txt","r")
#     data = f.read()
#     print(data)
# except Exception as e:
#     print("Exception Caught", e)

# try:
#     f = open("book_1.txt","r")
#     data = f.readlines()
#     print(data)
# except Exception as e:
#     print("Exception Caught", e)

# try:
#     f = open("book_1.txt","r")
#     data = f.readline()
#     while data:
#         print(data)
#         data = f.readline()
# except Exception as e:
#     print("Exception Caught", e)


# Create a file “commentary.txt” using open function and add content
# “Over 1: The match begins with a cracking cover drive for four by the opener! The crowd is already buzzing.”

# f = open("commentary.txt","w")
# data = f.write("The match begins with a cracking cover drive for four by the opener! The crowd is already buzzing.\n")


# Read file “commentary.txt” and display its content

# f = open("commentary.txt","r")
# data = f.read()
# print(data)


# Update file “commentary.txt” and add more
# “Over 3: A brilliant outswinger from the bowler! The batsman edges it, but it falls just short of the slip fielder.”

# f = open("commentary.txt","a")
# data = f.write("A brilliant outswinger from the bowler! The batsman edges it, but it falls just short of the slip fielder.")

# Read file “commentary.txt” and using len function see if it has 2 items

# f = open("commentary.txt","r")
# data = f.readlines()
# print(len(data))


# f = open("sample.txt", "a")
# f.write("content 1\n")
# f.close()

# f = open("sample.txt", "r")
# data = f.read()
# print(data)
# f.close()


# f = open("sample.txt", "a")
# f.write("content 2")
# f.close()

# f = open("sample.txt", "r")
# data = f.readlines()
# print(data, len(data))


# import json

# employees = [
#     {
#      "name": "danish"
#     },
#     {
#         "name": "Amin"
#     },
#     {
#         "name": "Talha"
#     }
# ]

# print(employees, type(employees))
# print(employees[0]['name'])
# employee_str = json.dumps(employees)
# print(employee_str, type(employee_str))
# print(employee_str[0]['name'])

# f = open("employee.txt", "wt")   wt = write text
# f.write(employee_str)


# json file data send and get

# f = open("employee.json", "wt")
# f.write(employee_str)
# f.close()

# f = open('employee.json', "rt")
# data = f.read()
# f.close()

# print(data)
# data = json.loads(data)
# print(data[0]['name'])


# import pickle

# employees = [
#     {
#      "name": "danish"
#     },
#     {
#         "name": "Amin"
#     },
#     {
#         "name": "Talha"
#     }
# ]

# print(employees, type(employees))
# print(employees[0]['name'])
# employee_byte = pickle.dumps(employees)
# print(employee_byte, type(employee_byte))

# f = open("employee.txt", "wb")   wb = write byte
# f.write(employee_byte)


# Pickle Byte file data send and get

# f = open("employee.bin", "wb")
# f.write(employee_byte)
# f.close()

# f = open('employee.bin', "rb")
# data = f.read()
# print(data)
# f.close()

# data = pickle.loads(data)
# print(data[0]['name'])


# High level vs Low level language


#  mutable

# arr = [1, 2, 3, 4]
# print(id(arr))
# arr.append(5)
# print(id(arr))

# print(arr)


# immutable

# t = (1, 2, 3, 4)
# print(id(t))
# t = t + (5,)
# print(id(t))

# print(t)