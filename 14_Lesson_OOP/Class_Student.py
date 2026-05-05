class Student:
    @classmethod
    def printClassStudentInfo(cls):
        print("This Class For Register Student Information.")
    name = "Abdullah"
    def __init__(self,name,age):
        self.Sname = name
        self.Sage = age

    def printStudent(self):
        print(f"The student name is {self.Sname} and \n The student age is {self.Sage}")

class Course:
    def __init__(self,Cname,Cap):
        self.CourseName =  Cname
        self.Capcity = Cap
        self.StudentName = []
    def showStudent(self):
        print("---------------- Student ----------------")
        for student in self.StudentName:
            print(student)
        print("-----------------------------------------")


Student1 = Student("ِAbdullah", 45)
Student2 = Student("ِAli", 98)

Student1.printStudent()
Student2.printStudent()

print(Student1.Sname)
print(Student1.Sage)
print(Student.name)
print(Student.printClassStudentInfo())

        