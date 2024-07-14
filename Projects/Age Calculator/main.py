from datetime import date

cureent_date = date.today()
user_age = input("Enter Your Date of Birth (Year-Month-Day): ")
change = date.fromisoformat(user_age)
calculate = cureent_date.year - change.year
print(f"Your Date of Birth is {user_age} and your age is {calculate}")
