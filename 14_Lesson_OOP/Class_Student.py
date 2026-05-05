class Student:
    def __init__(self,name,age):
        self.n = name
        self.a = age

    def printStudent(self):
        print(f"The student name is {self.n} and \n The student age is {self.a}")

Student1 = Student("ِAbdullah", 45)
Student2 = Student("ِAli", 98)

Student1.printStudent()
Student2.printStudent()

print(Student1.n)
print(Student1.a)

        