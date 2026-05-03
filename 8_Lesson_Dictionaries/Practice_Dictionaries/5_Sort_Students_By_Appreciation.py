'''
Docstring for 8_Lesson_Dictionaries.Practice_Dictionaries.5_Sort_Students_By_Appreciation
'''

student = {
    "Excellent":[],
    "Great":[],
    "Good":[],
    "Weak":[],
    "Pass":[],
    "Fail":[]
}

Stu_name = input("Enter your name here: ")
Stu_grade = input("Enter your grade here choose one\n Excellent, Great, Good, Weak, Pass, or Fial : ")

if Stu_grade in student:
    student[Stu_grade].append(Stu_name)
else:
    print("Invalid Grade!.")

print(student)