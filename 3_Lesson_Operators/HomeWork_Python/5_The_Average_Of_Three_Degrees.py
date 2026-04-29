'''
Docstring for 3_Lesson_Operators.HomeWork_Python.5_The_Average_Of_Three_Degrees
This program demonstrates the following
            1. Asks for three degrees from the user 
            2. calculate the average of the three degrees
'''
# asks the user for three input degrees using float numbers
mathDegree = float(input("Enter your Math degree here: "))
englishDegree = float(input("Enter your English degree here: "))
programmingDegree = float(input("Enter your programming degree here: "))

# Calculate the average degree of the three degrees
averageDegree = (mathDegree + englishDegree + programmingDegree) / 3

#the output degrees
print(f" Your Math degree is {mathDegree}.\n Your English degree is {englishDegree}.\n Your Programming degree is {programmingDegree}.")
print("-----------------------------------------------------")
print(f"-The Average of these degrees is {averageDegree}.  -")
print("-----------------------------------------------------")

