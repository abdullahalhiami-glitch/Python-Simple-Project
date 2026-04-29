'''
Docstring for 3_Lesson_Operators.HomeWork_Python.4_Age_Calculated_By_Days
This program calculates all the days a person has live upto this date 2026
'''

#getting age from the user
userAge = int(input("Enter your birthday by only year: "))

#calculating the days a user have lived until this year
calculateage = 2026 - userAge
totalMonthsLived = calculateage * 12
totalWeeksLived = calculateage * 52
totalDaysLived = calculateage * 365
totalHoursLived = calculateage * 365 * 24
totalMinutesLived = calculateage * 365 * 24 * 60
totalSecoudsLived = calculateage * 365 * 24 * 60 * 60

#output the age in years, in months, in weeks, in days, in hours, in minute, and in secounds
print(f"Your age in years with approximation:  {calculateage}")
print(f"Your age in months with approximation:  {totalMonthsLived}")
print(f"Your age in weeks with approximation:  {totalWeeksLived}")
print(f"Your age in days with approximation:  {totalDaysLived}")
print(f"Your age in hours with approximation:  {totalHoursLived}")
print(f"Your age in minutes with approximation:  {totalMinutesLived}")
print(f"Your age in seconds with approximation:  {totalSecoudsLived}")