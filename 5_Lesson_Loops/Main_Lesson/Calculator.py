'''
Docstring for 4_Lesson_Coditions.Calculator
'''

exit = True

#check varaibles
while exit:
    #varaibles Declaration
    num1 = input("please enter the first number : ")
    num2 = input("please enter the second number : ")

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
        operator = input(" Enter An Operator it must be one of the following operators\n\" + , - , / , * \" : ")
        if operator == "+":
            print(num1, "+", num2, "=", num1+num2)
        elif operator == "-":
            print(num1, "-", num2, "=", num1-num2)
        elif operator == "/":
            if num2==0:
                print("Division By zero not possible.")
            else:
                print(num1, "/", num2, "=", num1/num2)
        elif operator == "*":
            print(num1, "*", num2, "=", num1*num2)
        else:
            exit= input("Do you want to exit (yes/no): ").upper == "NO"
            print("********** Please Check Your Operator And Try Again ***********")
    else:
        print("********** Please Check Your Numbers And Try Again ***********")

print("********** Thanks For Using Our Calculator ***********")


    