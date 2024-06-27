# student_score = {
#     "Aliyan": 30,
#     "Nihal": 40,
#     "Taha": 10,
#     "Yasir": 60
# }
# print(student_score["Aliyan"])

# 1. Write a for loop to iterate through the student_scores dictionary and print each student's name and their score in the format: Student: [Name], Score: [Score].

# for key, val in student_score.items():
#     print("Student",key, "Score", val)


# 2. Write a for loop to calculate the average score of the students. Print the average score.
# total_score = 0
# for key, val in student_score.items():
#     total_score += val

# print("Average of Total Score is", total_score / len(student_score))


# 3. Write a for loop to assign grades based on the following criteria:
# Score >= 90: Grade A
# Score >= 80 and < 90: Grade B
# Score >= 70 and < 80: Grade C
# Score < 70: Grade D
# Store these grades in a new dictionary called student_grades.

# student_scores = {
#     "Aliyan": 70,
#     "Nihal": 80,
#     "Basit": 90,
#     "Taha": 65
# }
# student_grades = {}

# for key, val in student_scores.items():
#     if val >= 90:
#         grade = "A"
#     elif val >= 80:
#         grade = "B"
#     elif val >= 70:
#         grade = "C"
#     else:
#         grade = "D"
#     student_grades[key] = grade

# print(student_grades)


# 4. Modify the student_scores dictionary by adding 5 bonus points to each student's score.
# Print the updated student_scores dictionary.

# student_scores = {
#     "Aliyan": 70,
#     "Nihal": 80,
#     "Basit": 90,
#     "Taha": 65
# }

# for item in student_scores:
#     student_scores[item] += 5
# print(student_scores)


library_books = {
    "The Great Gatsby": 4,
    "1984": 6,
    "To Kill a Mockingbird": 3,
    "The Catcher in the Rye": 5,
    "Moby Dick": 2
}


# 1. Write a for loop to add 2 more copies to each book. Update the dictionary accordingly.

# for item in library_books:
#     library_books[item] += 2
# print(library_books)


# 2. Write a for loop to calculate the total number of books in the library. Print the total count.

# count = 0 
# for item in library_books:
#      count  += library_books[item]
# print("Total Books",count)


# consider the list of dicts
# book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]
# Write a for loop to assign one more detail "stock" based on the number of copies available:
# Copies >= 5: "Popular"
# Copies >= 3 and < 5: "Available"
# Copies < 3: "Limited"
# Store these stock categories in a same dict i.e book_list.

# book_list = [{"name": "The Great Gatsby", "quantity": 4}, {"name": "1984", "quantity": 6}, {"name": "To Kill a Mockingbird", "quantity": 3}, {"name": "Moby Dick", "quantity": 2}]

# for item in book_list:
#     quan = item["quantity"]
#     if quan >= 5:
#         item["stock"] = "Popular"
#     elif quan >= 3:
#         item["stock"] = "Available"
#     else:
#         item["stock"] = "Limited"
# print(book_list)



# Given the dict

students = {
    "Alice": {
                "Subjects": ["Math", "Science", "English"],
                "Scores": [85, 90, 78],
                "Class": 10
            },
    "Bob": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [75, 80, 88],
        "Class": 10
    },
    "Charlie": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [92, 89, 94],
        "Class": 11
    },
    "Diana": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [88, 76, 85],
        "Class": 11
    },
    "John": {
        "Subjects": ["Math", "Science", "English"],
        "Scores": [50, 60, 60],
        "Class": 11
    }
}


# 1. display Alice English Score
# 2. display Bob Class
# 3. display Charlie Math Score
# 4. display Diana's avg score
# 5. display John's all subject name and score with format: Student: [Name], Score: [Subject], Score: [Score].
# 6. Add new Student and its subject, score and class in same dict i.e students
# 7. add new subject and its score in John

# print("Alice English Score",students["Alice"]["Scores"][2])  # 1
# print("Bob Class is",students["Bob"]["Class"])  # 2
