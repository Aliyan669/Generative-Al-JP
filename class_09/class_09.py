from datetime import date, datetime

# why we need date module
# dt = "07-07-2024"

# dt_parts = dt.split("-")
# dt_parts[1] = "08"

# dta = "-".join(dt_parts) 
# print(dta) 


# current date

# today = date.today()
# print(today , type(today))
# print(today.year)
# print(today.month)
# print(today.day)


# current date with time

# dt_now = datetime.now()
# print(dt_now, type(dt_now))
# print(dt_now.date())
# print(dt_now.hour)
# print(dt_now.minute)
# print(dt_now.second)


# create date from string

# dt = "2024-07-06" # ISO format date  mean (year-month-day)
# dt = date.fromisoformat(dt)
# print(dt, type(dt))

# dt = "06-07-2024"
# dt = date.fromisoformat(dt) # it will raise error because date format is not ISO
# print(dt, type(dt))

# dt = "03-07-aliyan-2024" 
# dt = datetime.strptime(dt, "%d-%m-aliyan-%Y")  #Isko hum batadenge ke humne kis format me date likhi hai hai wo phir iso format me change kardega
# print(dt, type(dt))
# print(dt.date())


# create date from int

# dt = date( month= 1, year= 2022, day= 6)
# print(dt)
# dt = date(1, 2024, 6) # it will raise error
# print(dt)


# datetime strptime

# dt_n = "2024-07-06 12:38:00"
# dt_obj = datetime.strptime(dt_n, "%Y-%m-%d %H:%M:%S")
# print(dt_obj)


# convert date object to string

# dt = datetime.now()
# pak_dt = dt.strftime("%m-%d-%Y")  #ye string type return karta hai orr jo format ap denge us format me kardeta hai 
# print(pak_dt, type(pak_dt))

# dt_str = "2024-07-06 10:10:00"
# dt_obj = datetime.fromisoformat(dt_str)
# # print(dt_obj, type(dt_obj))
# pak_dt = dt_obj.strftime("%d-%m-%Y %I:%M:%S %p")
# print(pak_dt, type(pak_dt))


# string     -> dateobject # strptime
# dateobject -> string # strftime


# def greeting(username, greeting_type):
#     print(username, greeting_type)

# greeting(greeting_type="hi", username="aliyan")
# greeting("hi", "aliyan")
# greeting("aliyan", "hi")

"""
** Class Task:**
1. Write a function `parse_iso_date(iso_str)` that takes an ISO format date string 
(e.g., '2023-07-06T12:34:56') and returns a `datetime` object.
"""

# def parse_iso_date(iso_str):
#     return datetime.fromisoformat(iso_str)

# data = parse_iso_date("2023-07-06T12:34:56")
# print(data)