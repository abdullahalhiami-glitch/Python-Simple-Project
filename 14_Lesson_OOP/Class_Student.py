class Student:
    @classmethod
    def printClassStudentInfo(cls):# we can call this using the object its the name of the class Student.printClassStudentInfo() and this ensures that we don't call any function of this class using the @classmethod
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
        print(f'The {self.CourseName} course was created sucessfully')
    
    def enrollToCourse(self, StudentObject):
        if len(self.StudentName)<self.Capcity:
            self.StudentName.append(StudentObject)
            print('Student enrolled sucessfully')
        else:
            print("Sorry, you can't enroll to this course.")


    def showStudent(self):
        print("---------------- Student ----------------")
        for student in self.StudentName:
            # print(student.printStudent())# all the values of the list that you are printing must be the same values weather if they were objects or strings all of them must be one single data type
            print(student.printStudent())
            #or this of the objects of the class Course were string
            # print(student)
        print("-----------------------------------------")

python_course = Course('Python',3)


Student1 = Student("ِAbdullah", 45)
Student2 = Student("ِAli", 98)

# python_course.enrollToCourse('Abdullah')
# python_course.enrollToCourse('Mohammen')
python_course.enrollToCourse(Student2)
python_course.enrollToCourse(Student1)
Student1.printStudent()
Student2.printStudent()

print(Student1.Sname)
print(Student1.Sage)
print(Student.name)
print(Student.printClassStudentInfo())
python_course.showStudent()

    

