import datetime
birthdate = datetime.date(2004, 9, 6)
today = datetime.date.today()
age = today.year - birthdate.year
if(today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1
print("Your Age is:", age)
