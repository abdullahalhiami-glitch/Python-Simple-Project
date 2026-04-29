'''
Docstring for 3_Lesson_Operators.HomeWork_Python.10_Operator_Or
This program asks for a text day from the user and checks if the day if it's friday or sunday to tell the user it's a day off or not
'''

#input the text day from user
textDay = input("Enter the day by only using the name of it: ")

#check Day 
checkDay = textDay == "Friday" or textDay == "Sunday"

#output the result
print(checkDay)