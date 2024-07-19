# create a text file and add the below content without quotation marsk
# content = """Hi Aliyan!

# We've found the best article for you based on your interest: *title*
# Please click *here* to open the article"""

# f =  open("sample.txt", "w")
# f.write(content)

# task is to read the above file and update the placeholder i.e *user*, *title* and *here*
# and store the updated content in user_email.txt
# run program three times with different name, title and link

# f =  open("sample.txt", "r")
# data = f.read()
# print(data)

# f = open("sample.txt", "r")
# data = f.read()

# replacements = [
#     {"user": "John Doe", "title": "How to Use PET Bottles Effectively",
#         "link": "http://example.com/article1"},
#     {"user": "Jane Smith", "title": "10 Creative Uses for PET Bottles",
#         "link": "http://example.com/article2"},
#     {"user": "Alice Johnson", "title": "The Environmental Impact of PET Bottles",
#         "link": "http://example.com/article3"},
# ]

# for replacement in replacements:
#     updated_content = data.replace("*user*", replacement["user"])
#     updated_content = updated_content.replace("*title*", replacement["title"])
#     updated_content = updated_content.replace(
#         "*here*", f"<a href='{replacement['link']}'>here</a>")

#     f = open("user_email.txt", "w")
#     f.write(updated_content)


# Create a new text file named "student_records.txt" with the following initial content:

# f = open("student.txt", "w")
# f.write("""Student ID | Student Name | Grade
# 101       | Alice        | A
# 102       | Bob          | B
# 103       | Carol        | C
# """)


# Open the "student_records.txt" file in read mode ('r') and read its contents line by line. Print each line to the console.

# f =  open("student.txt", "r")
# data = f.readlines()
# for i in data:
#     print(i.strip())


# Create a new text file named "updated_records.txt" in write mode('w').
# Read the content of "student_records.txt" again and write only the lines containing students with grades 'A' or 'B' to the "updated_records.txt" file.
# Close both files.

# student_file = open("student.txt", "r")
# updated_file = open("updated_records.txt", "w")

# for item in student_file:
#     if " A" in item or " B" in item:
#         updated_file.write(item)
# student_file.close()
# updated_file.close()


# Open "updated_records.txt" in append mode('a') and add a new student record:
# Close the "updated_records.txt" file.

# updated_file = open("updated_records.txt", "a")
# updated_file.write("103        | David        | C\n")
# updated_file.close()


# Open "updated_records.txt" in read mode and print its contents to the console to verify that the new student record has been added.

# updated_file = open("updated_records.txt", "r")
# data = updated_file.read()
# print(data)


# Objective:
""" Create a password manager program that allows users to store, retrieve, and manage their passwords. 
The program will use file handling to save and read data, and it will be run in the terminal.

#### Requirements:
1. **File Handling**: Store the passwords in a file. Each entry should include the website, username, and password.
2. **Input Function**: Allow users to add new passwords, retrieve existing passwords, and delete passwords.
3. **Basic Operations**:
    - **Add a new password**: Ask for the website, username, and password. Save this information to the file.
    - **Retrieve a password**: Ask for the website and return the username and password.
    - **Delete a password**: Ask for the website and remove the corresponding entry from the file.
4. **Basic Error Handling**: Handle cases where the website is not found when retrieving or deleting a password and also when file doesn't exists

#### Program Flow:
1. Display a menu with the following options:
    - Add a new password
    - Retrieve a password
    - Delete a password
    - Exit
2. Based on the user's choice, perform the corresponding operation.
3. Repeat the menu until the user chooses to exit.

#### Detailed Instructions:
1. **Menu Display**: Create a function to display the menu and get the user's choice.
2. **Add Password**:
    - Prompt the user for the website, username, and password.
    - Write this information to a file in a structured format.
3. **Retrieve Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Display the username and password.
4. **Delete Password**:
    - Prompt the user for the website.
    - Read the file and find the entry for the given website.
    - Remove the entry and update the file.
5. **File Format**: Store each entry in a new line in the format:
    ```
    website,username,password
    ```

#### Example:
1. **Add Password**:
    ```
    Enter website: example.com
    Enter username: user1
    Enter password: pass123
    Password saved successfully!
    ```
2. **Retrieve Password**:
    ```
    Enter website: example.com
    Username: user1
    Password: pass123
    ```
3. **Delete Password**:
    ```
    Enter website: example.com
    Password deleted successfully!
    """


# import getpass
# file_path = "passwords.txt"

# def add_password():
#     website = input("Enter the website name: ")
#     username = input("Enter the username: ")
#     password = getpass.getpass("Enter the password: ")

#     f = open(file_path, "a")
#     f.write(f"{website} | {username} | {password}\n")

#     print("Password added successfully.")


# def retrieve_password():
#     website = input("Enter the website name: ")
#     f = open(file_path, "r")
#     found = False
#     for item in f:
#         stored_website, stored_username, stored_password = item.strip().split(" | ")
#         if stored_website == website:
#             print(f"website: {stored_website}\nUsername: {
#                   stored_username}\nPassword: {stored_password}")
#             found = True
#             break

#     if not found:
#         print("No password found for this website.")


# def list_passwords():
#     f = open(file_path, "r")
#     for item in f:
#         stored_website, stored_username, stored_password = item.strip().split(" | ")
#         print(f"website: {stored_website}\nUsername: {
#               stored_username}\nPassword: {stored_password}")


# def delete_password():
#     website = input("Enter the website name: ")

#     lines = []
#     f = open(file_path, "r")
#     for item in f:
#         stored_website, stored_username, stored_password = item.strip().split(" | ")
#         if stored_website != website:
#             lines.append(item)

#     f = open(file_path, "w")
#     for item in lines:
#         f.write(item)

#     print("Password deleted successfully.")


# def main():
#     while True:
#         print("\nPassword Manager")
#         print("1. Add Password")
#         print("2. Retrieve Password")
#         print("3. List All Passwords")
#         print("4. Delete Password")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_password()
#         elif choice == '2':
#             retrieve_password()
#         elif choice == '3':
#             list_passwords()
#         elif choice == '4':
#             delete_password()
#         elif choice == '5':
#             print("Exiting Password Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# main()


"""
create the same program again but this time file data should be stored in json
"""

# import json
# import getpass

# file_path = "passwords.json"

# def load_passwords():
#     try:
#         f = open(file_path, "r")
#         return json.load(f)
#     except FileNotFoundError:
#         return {}
#     except json.JSONDecodeError:
#         return {}

# def save_passwords(passwords):
#         f = open(file_path, "w")
#         json.dump(passwords, f, indent=4)

# def add_password(passwords):
#     service = input("Enter the service name: ")
#     username = input("Enter the username: ")
#     password = getpass.getpass("Enter the password: ")

#     passwords[service] = {"username": username, "password": password}
#     save_passwords(passwords)
#     print("Password added successfully.")

# def retrieve_password(passwords):
#     service = input("Enter the service name: ")

#     if service in passwords:
#         print(f"Service: {service}\nUsername: {passwords[service]['username']}\nPassword: {passwords[service]['password']}")
#     else:
#         print("No password found for this service.")

# def list_passwords(passwords):
#     for service, details in passwords.items():
#         print(f"Service: {service}\nUsername: {details['username']}\nPassword: {details['password']}")
#         print("-" * 30)

# def delete_password(passwords):
#     service = input("Enter the service name: ")

#     if service in passwords:
#         del passwords[service]
#         save_passwords(passwords)
#         print("Password deleted successfully.")
#     else:
#         print("No password found for this service.")

# def main():
#     passwords = load_passwords()

#     while True:
#         print("\nPassword Manager")
#         print("1. Add Password")
#         print("2. Retrieve Password")
#         print("3. List All Passwords")
#         print("4. Delete Password")
#         print("5. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             add_password(passwords)
#         elif choice == '2':
#             retrieve_password(passwords)
#         elif choice == '3':
#             list_passwords(passwords)
#         elif choice == '4':
#             delete_password(passwords)
#         elif choice == '5':
#             print("Exiting Password Manager.")
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()
