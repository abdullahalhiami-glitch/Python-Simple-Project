'''
Docstring for 4_Lesson_Coditions.Calculator
'''
#Variable For the loop
exit = True

def sum(num1,num2):
    return num1+num2
def sub(num1,num2): 
    return num1-num2    
def div(num1,num2):
    if num2==0:
        return "Division By zero not possible."
    else:
        return num1/num2
def mul(num1,num2):
    return num1*num2

def calculator():
    #varaibles Declaration
    num1 = float(input("please enter the first number : "))
    num2 = float(input("please enter the second number : "))
    operator = input(" Enter An Operator it must be one of the following operators\n\" + , - , / , * \" : ")
    if operator == "+":
        print(num1, "+", num2, "=", sum(num1, num2))
    elif operator == "-":
        print(num1, "-", num2, "=", sub(num1, num2))
    elif operator == "/":
        print(num1, "/", num2, "=", div(num1, num2))
    elif operator == "*":
        print(num1, "*", num2, "=", mul(num1, num2))
    else:
        print("********** Please Check Your Operator And Try Again ***********")
#check varaibles
while exit:
    #varaibles Declaration
    num1 = float(input("please enter the first number : "))
    num2 = float(input("please enter the second number : "))
    operator = input(" Enter An Operator it must be one of the following operators\n\" + , - , / , * \" : ")
    if operator == "+":
        print(num1, "+", num2, "=", sum(num1, num2))
    elif operator == "-":
        print(num1, "-", num2, "=", sub(num1, num2))
    elif operator == "/":
        print(num1, "/", num2, "=", div(num1, num2))
    elif operator == "*":
        print(num1, "*", num2, "=", mul(num1, num2))
    else:
        print("********** Please Check Your Operator And Try Again ***********")
    exit= input("Do you want to exit (yes/no): ").upper == "no"


    