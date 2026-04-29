'''
Docstring for 4_Lesson_Coditions.Calculator
'''
#Variable For the loop
exit = True

# Functions for the arthimatic operations
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
def power(num1,num2):
    return num1**num2
def mod(num1,num2):
    return num1%num2
def intDiv(num1,num2):
    return num1//num2

# Function to calculate and check the operations
def calculator(num1,num2,operator):
    if operator == "+":
        print(num1, "+", num2, "=", sum(num1, num2))
    elif operator == "-":
        print(num1, "-", num2, "=", sub(num1, num2))
    elif operator == "/":
        print(num1, "/", num2, "=", div(num1, num2))
    elif operator == "*":
        print(num1, "*", num2, "=", mul(num1, num2))
    elif operator == "**":
        print(num1, "**", num2, "=", power(num1, num2))
    elif operator == "//":
        print(num1, "//", num2, "=", intDiv(num1, num2))
    elif operator == "%":
        print(num1, "%", num2, "=", mod(num1, num2))
    else:
        print("********** Please Check Your Operator And Try Again ***********")


#check varaibles
while exit:
    #varaibles Declaration
    num1 = input("please enter the first number : ")
    num2 = input("please enter the second number : ")

    if num1.isnumeric() and num2.isnumeric():
        num1 = float(num1)
        num2 = float(num2)
        operator = input(" Enter An Operator it must be one of the following operators\n\"-------------- + , - , / , // , * , ** , % --------------\" : ")
        calculator(num1,num2,operator)
    else:
        print("********** Please Check Your Numbers And Try Again ***********")
    exit= input("Do you want to exit (yes/no): ").upper == "NO"

print("********** Thanks For Using Our Calculator ***********")


    


    