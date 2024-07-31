from datetime import date, datetime, timedelta
import pytz

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


# create a current datetime and then displays it in the format "HH:MM AM/PM"

# current_datetime = datetime.now()
# formatted_time = current_datetime.strftime("%I:%M %p")
# print("Current time:", formatted_time)


# Write a program that takes a user-entered date in the format "MM/DD/YYYY" and prints it in the format "YYYY-MM-DD".

# date_str = input("Enter a date (MM/DD/YYYY): ")
# date_obj = datetime.strptime(date_str, "%m/%d/%Y")
# formatted_date = date_obj.strftime("%Y-%m-%d")

# print("Formatted date:", formatted_date)


# Create a function that takes a datetime object as input and displays the day of the week (e.g., "Monday") using strftime().

# datetime_str = input("Enter a datetime (YYYY-MM-DD): ")
# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d")
# day_of_week = datetime_obj.strftime("%A")
# print("Day of the week:", day_of_week)


# Create a function that takes a timezone name as input and prints the current date time object in that timezone.

# timezone_name = input("Enter a timezone (e.g., 'Asia/Kolkata', 'America/New_York'): ")

# def print_current_datetime_in_timezone(timezone_name):

#     utc_now = datetime.now(pytz.utc)
#     timezone = pytz.timezone(timezone_name)
#     local_time = utc_now.astimezone(timezone)
#     print("Current datetime in", timezone_name, "is:", local_time)

# print_current_datetime_in_timezone(timezone_name)


# Write a program that converts a given date time (tz aware) string from one timezone to another.

# datetime_str = input("Enter the datetime (e.g., '2023-08-26 15:30:00'): ")
# from_timezone = input("Enter the source timezone (e.g., 'Asia/Kolkata'): ")
# to_timezone = input("Enter the target timezone (e.g., 'America/New_York'): ")

# datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

# source_tz = pytz.timezone(from_timezone)
# localized_datetime = source_tz.localize(datetime_obj)

# target_tz = pytz.timezone(to_timezone)
# converted_datetime = localized_datetime.astimezone(target_tz)

# print("Converted datetime in", to_timezone, "is:", converted_datetime)


# Write a program that takes a datetime object (naive) and a timezone name as input, and returns a localized datetime object in the specified timezone.

# datetime_str = input("Enter the naive datetime (e.g., '2023-08-26 15:30:00'): ")
# timezone_name = input("Enter the timezone (e.g., 'Asia/Kolkata'): ")

# naive_datetime = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
# timezone = pytz.timezone(timezone_name)

# localized_datetime = timezone.localize(naive_datetime)

# print("Localized datetime in", timezone_name, "is:", localized_datetime)


# Create a function that takes a timezone name and a number of hours as input, and prints the current time plus the specified hours in that timezone

# timezone_name = input("Enter a timezone (e.g., 'Asia/Kolkata'): ")
# hours = int(input("Enter the number of hours to add: "))

# def print_future_time_in_timezone(timezone_name, hours):
#     utc_now = datetime.now(pytz.utc)

#     timezone = pytz.timezone(timezone_name)
#     local_time = utc_now.astimezone(timezone)

#     future_time = local_time + timedelta(hours=hours)

#     print(f"Current time plus {hours} hours in {timezone_name} is: {future_time}")

# print_future_time_in_timezone(timezone_name, hours)


# Write a program that calculates the date and time of the daylight saving start in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

# timezone = pytz.timezone("US/Pacific")

# start_date_str = "2022-01-01 00:00:00"
# start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")

# start_date = timezone.localize(start_date)

# def find_dst_start(year):
#     date = datetime(year, 1, 1, 0, 0, 0, tzinfo=timezone)
#     while date.year == year:
#         if bool(date.dst()) == True:
#             return date
#         date += timedelta(days=1)
#         date = timezone.localize(date)
#     return None

# dst_start = find_dst_start(2022)

# if dst_start:
#     print(f"Daylight Saving Time starts on: {dst_start.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
# else:
#     print("Daylight Saving Time does not start in 2022.")


# Write a program that calculates the date and time of the daylight saving end in the year 2022.
# take timezone "US/Pacific"
# take string date as "2022-01-01 00:00:00"
# hint: use
# bool(tz_aware_dt.dst()) == True # dst activated
# bool(tz_aware_dt.dst()) == False # dst not activated

# timezone = pytz.timezone("US/Pacific")

# start_date_str = "2022-01-01 00:00:00"
# start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")

# start_date = timezone.localize(start_date)

# def find_dst_end(year):
#     date = datetime(year, 1, 1, 0, 0, 0, tzinfo=timezone)
#     date = timezone.localize(date)
#     in_dst = bool(date.dst())

#     while date.year == year:
#         date += timedelta(days=1)
#         date = timezone.localize(date)
#         if bool(date.dst()) != in_dst:
#             if not in_dst:
#                 return date
#             in_dst = not in_dst
#     return None

# dst_end = find_dst_end(2022)

# if dst_end:
#     print(f"Daylight Saving Time ends on: {dst_end.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")
# else:
#     print("Daylight Saving Time does not end in 2022.")


# Design a program that helps schedule a meeting across different timezones. The program should take the meeting time in one timezone and display the corresponding times in other timezones.
# consider three countries: UK, US, Saudi Arab and Pakistan
# consider the meeting time is: 30 August 2023 at 2 PM Pakistan time

# timezones = {
#     'Pakistan': 'Asia/Karachi',
#     'UK': 'Europe/London',
#     'US (New York)': 'America/New_York',
#     'Saudi Arabia': 'Asia/Riyadh'
# }

# meeting_time_str = "2023-08-30 14:00:00"
# pakistan_tz = pytz.timezone(timezones['Pakistan'])
# meeting_time = datetime.strptime(meeting_time_str, "%Y-%m-%d %H:%M:%S")

# meeting_time_pakistan = pakistan_tz.localize(meeting_time)

# for country, tz_name in timezones.items():
#     tz = pytz.timezone(tz_name)
#     meeting_time_in_timezone = meeting_time_pakistan.astimezone(tz)
#     print(f"Meeting time in {country}: {meeting_time_in_timezone.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")


# Booking System
# Design a booking system where users specify a start datetime, end datetime, and timezone. Implement a function that checks whether a specified time slot is available.
# if timeslot is available then store the start_date and end_date in the list of objects i.e
"""
booking_storage = [
  {
    "start_date": "",
    "end_date": ""
  }
]
"""
# hint 1: store dates in booking_storage in UTC format i.e pytz.utc
# hint 2: use for loop, the loop should run 5 times. ask user input inside the loop

# instruction to test your program:
# first iteration of loop
# give input "2023-08-26 18:00:00" as start_date and "2023-08-26 19:00:00" as end_date and "Asia/Karachi" as timezone

# second iteration of loop
# give input "2023-08-26 16:00:00" as start_date and "2023-08-26 17:00:00" as end_date and "Asia/Riyadh" as timezone
# above program should not accept this booking as the slot is already booked by the first iteration

booking_storage = []


def is_slot_available(start_date, end_date):
    start_date_utc = start_date.astimezone(pytz.utc)
    end_date_utc = end_date.astimezone(pytz.utc)

    for booking in booking_storage:
        booked_start = booking["start_date"]
        booked_end = booking["end_date"]

        if (start_date_utc < booked_end) and (end_date_utc > booked_start):
            return False
    return True


def add_booking(start_date, end_date):
    if is_slot_available(start_date, end_date):
        booking_storage.append({
            "start_date": start_date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z%z'),
            "end_date": end_date.astimezone(pytz.utc).strftime('%Y-%m-%d %H:%M:%S %Z%z')
        })
        print("Booking confirmed!")
    else:
        print("Time slot is not available.")


for _ in range(5):
    start_date_str = input("Enter start date (YYYY-MM-DD HH:MM:SS): ")
    end_date_str = input("Enter end date (YYYY-MM-DD HH:MM:SS): ")
    timezone_str = input("Enter timezone (e.g., Asia/Karachi): ")

    timezone = pytz.timezone(timezone_str)
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d %H:%M:%S")
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d %H:%M:%S")

    start_date = timezone.localize(start_date)
    end_date = timezone.localize(end_date)

    add_booking(start_date, end_date)

print("Booking storage:")
for booking in booking_storage:
    print(booking)
