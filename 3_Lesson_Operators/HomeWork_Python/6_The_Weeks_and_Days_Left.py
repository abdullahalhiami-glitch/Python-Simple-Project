'''
Docstring for 3_Lesson_Operators.HomeWork_Python.6_The_Weeks_and_Days_Left
This program demonstrates the left days and weeks for a user input.
the user will input a number a days and you calculate how many weeks and how many days left
'''

#inputing the Days from the user
numberOfdays = int(input("Enter the number of days you want to turn into weeks: "))

# calculateNumberOfWeeks = numberOfdays // 7
# leftDays = numberOfdays % 7

#check if the numer of days entered by the user greater than seven
if numberOfdays < 7:
    print("Sorry, can't convert into weeks")
else:
    calculateNumberOfWeeks = numberOfdays // 7
    leftDays = numberOfdays % 7
    print(f"The weeks are : {calculateNumberOfWeeks} \nAnd the days that still left are/is {leftDays}")