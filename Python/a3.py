# Simple Age Calculator

# Import necessary libs
from datetime import datetime

# Gets Inputs
birthdate_str1 = input("Enter your birthday day (Example: 25): ")
birthdate_str2 = input("Enter your birthday month (Example: 12): ")
birthdate_str3 = input("Enter your birthday year (Example: 2005): ")

# Compounds The Inputs
birthdate_str = birthdate_str2 + " " + birthdate_str1 + " " + birthdate_str3

# Convert the user input to a Object
birthdate = datetime.strptime(birthdate_str, "%m %d %Y")

# Calculate the age in years, months, and days
current_date = datetime.now()
age = current_date - birthdate
years = age.days // 365
months = (age.days % 365) // 30
days = (age.days % 365) % 30

print("You are {} years, {} months, and {} days old.".format(years, months, days))
