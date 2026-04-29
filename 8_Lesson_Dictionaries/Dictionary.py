'''
Docstring for 8_Lesson_Dictionaries.Dictionary
'''
studentInformation = {
    'studentName': 'Abdullah',
    'studentUsername':"abdullah_alhimai",
    'studentId': 123456789,
    'studentDegree':89.3,
    'studentAge': 24,
    'subjects': ['Math','English']
    }
studentInfo = {
    'studentName': 'Abdullah',
    'studentUsername':"abdullah_alhimai",
    'studentId': 123456789,
    'studentDegree':89.3,
    'studentAge': 24,
    'subjects': ['Math','English']
    }

# print(studentInformation['studentDegree'])
# print(studentInformation['studentName'])
# print(studentInformation.items())
# print(studentInformation.keys())
# print(studentInformation.values())

for key in studentInformation.keys() & studentInfo.keys():
    print(studentInformation[key],studentInfo[key])

for key,value in studentInformation.items():
    print(f'The key is {key} and the value is {value}')

studentInformation=['myNewDegree'] = [12,56,99]
print(studentInformation)

#updating a value 
studentInformation['studentAge'] = 25
# studentInformation.update({'studentAge'}) = 26
studentInformation.update({'studentAge':56})



#deleting a value
del studentInformation['myNewDegree']
print(studentInformation)


