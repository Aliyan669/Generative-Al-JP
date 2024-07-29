from datetime import date, datetime, timedelta

# Write a Python program that uses the date module to print the current date in the format "YYYY-MM-DD".

# current_date = date.today()
# print(current_date)


# Create a program that takes a date in the format "MM/DD/YYYY" as string and converts it to "YYYY-MM-DD".

# dt = "03-07-2024"
# dt = datetime.strptime(dt, "%d-%m-%Y")
# print(dt.date())


# Write a program that takes a birth year as input and calculates the age of a person.

# cureent_date = date.today()
# user_age = input("Enter Your Date of Birth (Year-Month-Day): ")
# change = date.fromisoformat(user_age)
# calculate = cureent_date.year - change.year
# print(f"Your Date of Birth is {user_age} and your age is {calculate}")


# Create a program that calculates and prints the number of days remaining until a person's next birthday.
# take users birth date as input

# birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
# birth_date = date.fromisoformat(birth_date_str)
# # print(birth_date)

# today = date.today()
# next_birthday = date(today.year, birth_date.month, birth_date.day)

# if next_birthday <= today:
#     next_birthday = date(today.year + 1, birth_date.month, birth_date.day)

# days_remaining = (next_birthday - today).days
# print(days_remaining)


# Write a program that calculates and displays the number of days between two given dates.

# date1_str = input("Enter the first date (YYYY-MM-DD): ")
# date2_str = input("Enter the second date (YYYY-MM-DD): ")

# date_1 = date.fromisoformat(date1_str)
# date_2 = date.fromisoformat(date2_str)
# between_days = abs((date_2 - date_1).days)

# print(between_days)


# Create a program that takes a date as string and returns the corresponding day of the week (e.g., Monday, Tuesday, etc.).

# date_str = input("Enter a date (YYYY-MM-DD): ")
# date = date.fromisoformat(date_str)

# day_of_week = date.strftime("%A")

# print("The day of the week for", date_str, "is", day_of_week)


# Create a program that takes a year and a month as input and prints the number of days in that month.
# without using calender module

# year = int(input("Enter year: "))
# month = int(input("Enter month (1-12): "))

# if month in [1, 3, 5, 7, 8, 10, 12]:
#         days = 31
# elif month in [4, 6, 9, 11]:
#         days = 30
# elif month == 2:
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             days = 29
#         else:
#             days = 28

# print(f"Number of days in {month}/{year}: {days}")


# Create a function that takes a starting date and a number of days as input, and then calculates and prints the date that is the specified number of days in the future.

# def calculate_future_date(start_date_str, days):
#     start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
#     future_date = start_date + timedelta(days=days)
#     future_date_str = future_date.strftime("%Y-%m-%d")
#     return future_date_str

# start_date_str = input("Enter the starting date (YYYY-MM-DD): ")
# days = int(input("Enter the number of days: "))
# future_date_str = calculate_future_date(start_date_str, days)

# print(f"The date {days} days from {start_date_str} is {future_date_str}")


# Write a Python program that uses the datetime module to print the current date and time.

# dt_now = datetime.now()
# print(dt_now)


# Create a function that takes a datetime in the format "MM/DD/YYYY HH:MM:SS" as string  formats it as "YYYY-MM-DD HH:MM:SS".

# dt = "07-24-2024 12:38:00"
# dt_obj = datetime.strptime(dt,"%m-%d-%Y %H:%M:%S")
# print(dt_obj)


# Write a program that calculates the time difference between two given datetime objects and displays it in hours, minutes, and seconds.

# datetime1_str = input("Enter the first datetime (YYYY-MM-DD HH:MM:SS): ")
# datetime2_str = input("Enter the second datetime (YYYY-MM-DD HH:MM:SS): ")

# datetime1 = datetime.strptime(datetime1_str, "%Y-%m-%d %H:%M:%S")
# datetime2 = datetime.strptime(datetime2_str, "%Y-%m-%d %H:%M:%S")

# difference = datetime2 - datetime1

# total_seconds = int(difference.total_seconds())
# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

# print(f"Time difference is {hours} hours, {minutes} minutes, and {seconds} seconds.")


# Create a function that takes a datetime object and a number of hours as input, then returns a new datetime object with the added hours.

# datetime_str = input("Enter a datetime (YYYY-MM-DD HH:MM:SS): ")
# hours = int(input("Enter the number of hours to add: "))

# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# new_date = datetime_obj + timedelta(hours=hours)

# print("New datetime:", new_date)


# Create a function that takes a datetime object as input and formats it as "Month Day, Year" (e.g., "August 25, 2023") using strftime().

# datetime_str = input("Enter a datetime (YYYY-MM-DD HH:MM:SS): ")
# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# format_date = datetime_obj.strftime("%B %d, %Y")

# print("Format date:", format_date)


# Create a function that takes a datetime object as input and formats it as "Day-Month-Year" (e.g., "25-August-2023") using strftime().

# datetime_str = input("Enter a datetime (YYYY-MM-DD HH:MM:SS): ")
# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# format_date = datetime_obj.strftime("%d %B, %Y")

# print("Format date:", format_date)


# create a datetime object from the string "26-08-2023 15:18:33.983780-07:00"

# datetime_str = "26-08-2023 15:18:33.983780-07:00"
# datetime_obj = datetime.strptime(datetime_str, "%d-%m-%Y %H:%M:%S.%f%z")
# print("Datetime object:", datetime_obj)


# create a datetime object from the string "08-26-2023 08:10:00 PM"

# datetime_str = "08-26-2023 08:10:00 PM"
# datetime_obj = datetime.strptime(datetime_str, "%m-%d-%Y %I:%M:%S %p")

# print("Datetime object:", datetime_obj)
