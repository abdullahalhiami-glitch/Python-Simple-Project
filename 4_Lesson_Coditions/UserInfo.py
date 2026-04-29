'''
Docstring for 4_Lesson_Coditions.UserInfo
'''

userName = "@abdullah"
password = 123456789

newUserName = input("Enter your user name : ")
newPassword = input("Enter your user password : ")

if newUserName == userName and newPassword == password:
    print("Login successfuly.")
else:
    print("Try again.")