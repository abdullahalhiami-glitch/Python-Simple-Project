'''
Docstring for 12_Lesson_Module.Homework.Area_Of_The_Circle
'''

import math as m

#calculating the radius of the circle
def circumference(radius):
    p = m.pi
    result = m.pow(2,p) * radius # C = 2 * pi * radius
    return result

#inputing the radius of the circle from the user
radius_of_circle = float(input("Enter the radius of the circle: "))

#printing the circle area
circle_area = circumference(radius_of_circle)
print(f'The circle area is {circle_area}')
# print(f'The circle area is {2 * m.pi * 10}') #this is wrong because the radius is not 10, it is the user input
print(f'the circle area is {m.pow(2,m.pi) * 10}')

