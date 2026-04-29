'''
Docstring for 3_Lesson_Operators.HomeWork_Python.9_Operater_And
This program demonstrates the following
                        1. checks if the student have a degree greater that 90
                        2. and his attendance degree greater than 95
                        3. using and only without if
'''
#input from the student
print("=============== To Receive a PartenarShip Enter the Following:")
studentDegree = float(input("1.Enter your Studying Degree Here: "))
attendanceDegree = float(input("2.Enter your Attendance Degree Here: "))

#checking
checkDegree = studentDegree > 90 and attendanceDegree > 95

#output
print(checkDegree)

