'''
Docstring for 5_Lesson_Loops.HomeWorkString.3_Check_The_Strength_Of_A_Password
'''

#input Password
newPassword = input("Enter your New Password here: ")

lengthOfPassword = len(newPassword) 

for i in newPassword:
    if lengthOfPassword > 8:
        if i.isupper:
            print("You Have a strong password.")
            break
        elif i.isdigit:
            print("You Have a strong password.")
            break
        else:
            print("You Have a weak Password!")
            break
    else:
        print("Your password must be more than 8 digits!")
        break