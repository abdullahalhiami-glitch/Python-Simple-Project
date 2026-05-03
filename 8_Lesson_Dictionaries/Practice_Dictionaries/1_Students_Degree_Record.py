'''
Docstring for 8_Lesson_Dictionaries.Practice_Dictionaries.1_Students_Degree_Record
'''
#Boolean Value for the while loop
Exit = True

#While loop checks the following 
            #if the name has numbers it doesn't accept it
            #if the degrees greater than 100 it rejects them and to the student to enter the information again
while Exit:
    # Program Inputs Student Name And Three Degrees of three Subjects
    Stu_NameInput = input("Enter the student name right here: ")
   #handling errors
    if Stu_NameInput.isalpha():
        Stu_English_Degree = input("Enter your English degree here: ")
        Stu_Arabic_Degree = input("Enter your Arabic degree here: ")
        Stu_Math_Degree = input("Enter your Math degree here: ")
        #handling errors
        if Stu_English_Degree.isdigit() and Stu_Arabic_Degree.isdigit() and Stu_Math_Degree.isdigit():
            Stu_English_Degree = float(Stu_English_Degree)
            Stu_Arabic_Degree = float(Stu_Arabic_Degree)
            Stu_Math_Degree = float(Stu_Math_Degree)
            # Declaring out input into the dictionary
            StudentDegreeRecord = {
                "Stu_Name": Stu_NameInput,
                "Stu_Degrees": {
                    "English": Stu_English_Degree,
                    "Arabic": Stu_Arabic_Degree,
                    "Math": Stu_Math_Degree
                    }
                }

            # the sumation of all three degrees
            Sum = StudentDegreeRecord["Stu_Degrees"]["English"] + StudentDegreeRecord["Stu_Degrees"]["Arabic"] + StudentDegreeRecord["Stu_Degrees"]["Math"]

            #calculating the average of the three degrees
            Average_Degrees = Sum / len(StudentDegreeRecord["Stu_Degrees"])

            #outputing the final answear 
            print("------------------- Welcome Student -------------------")
            print(f"1.Your name is {StudentDegreeRecord['Stu_Name']}.")
            print(f"1.Your English Degree is {StudentDegreeRecord['Stu_Degrees']["English"]}.")
            print(f"1.Your Arabic Degree is {StudentDegreeRecord['Stu_Degrees']["Arabic"]}.")
            print(f"1.Your Math Degree is {StudentDegreeRecord['Stu_Degrees']["Math"]}.")
            print(f"5.The Average Of Your Degrees is {Average_Degrees}.")
            print(f"------------------- Goodbye Studnet {StudentDegreeRecord['Stu_Name']}.")
        else:
            print("Sorry, degrees can't be characters!")
    else:
        print("Sorry, vaild name!.")
    Exit = input("Do you want to Exit the program (yes/no): ").lower() == 'no'
print("------------------Goodbye------------------")


