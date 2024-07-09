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


#Jab File exist nhi karti hogi tu excution ka error ata hai 
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

