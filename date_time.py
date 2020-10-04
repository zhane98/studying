import datetime

today = datetime.datetime.now()
print(today)

day = today.day
month = today.month
year = today.year

print("Day: " + str(day))
print("Month: " + str(month))
print("Year: " + str(year))

future = datetime.datetime(2021, 4, 9) #creating a future day, and can be printed in the same way.

print(future.strftime("%A"))