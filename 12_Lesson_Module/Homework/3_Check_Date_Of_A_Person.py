'''
Docstring for 12_Lesson_Module.Homework.3_Check_Date_Of_A_Person
'''

def calculate_age(age=18):
    person_age = 2026 - age
    return person_age
def totalMonthsLived(age=18):
    total_months = calculate_age(age) * 12
    return total_months
def totalWeeksLived(age=18):
    total_weeks = calculate_age(age) * 52
    return total_weeks
def totalDaysLived(age=18):
    total_days = calculate_age(age) * 365
    return total_days
def totalHoursLived(age=18):
    total_hours = calculate_age(age) * 365 * 24
    return total_hours
def totalMinutesLived(age=18):
    total_minutes = calculate_age(age) * 365 * 24 * 60
    return total_minutes
def totalSecondsLived(age=18):
    total_seconds = calculate_age(age) * 365 * 24 * 60 * 60
    return total_seconds
def totalnonscondsLived(age=18):
    total_nonsconds = calculate_age(age) * 365 * 24 * 60 * 60 * 1000
    return total_nonsconds  
#getting age from the user
userAge = int(input("Enter your birthday by only year: "))

#calculating the days a user have lived until this year
# calculateage = 2026 - userAge
# totalMonthsLived = calculateage * 12
# totalWeeksLived = calculateage * 52
# totalDaysLived = calculateage * 365
# totalHoursLived = calculateage * 365 * 24
# totalMinutesLived = calculateage * 365 * 24 * 60
# totalSecoudsLived = calculateage * 365 * 24 * 60 * 60

#output the age in years, in months, in weeks, in days, in hours, in minute, and in secounds
print(f"Your age in years with approximation:  {calculate_age(userAge)}")
print(f"Your age in months with approximation:  {totalMonthsLived(userAge)}")
print(f"Your age in weeks with approximation:  {totalWeeksLived(userAge)}")
print(f"Your age in days with approximation:  {totalDaysLived(userAge)}")
print(f"Your age in hours with approximation:  {totalHoursLived(userAge)}")
print(f"Your age in minutes with approximation:  {totalMinutesLived(userAge)}")
print(f"Your age in seconds with approximation:  {totalSecondsLived(userAge)}")
print(f"Your age in nonsconds with approximation:  {totalnonscondsLived(userAge)}")