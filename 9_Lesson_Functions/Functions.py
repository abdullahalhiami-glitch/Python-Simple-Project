# def sayHello(name='Unknown'):
#     if name=='Unknown':
#         print("Unkown person!.")
#     else:
#         print(f'Hello {name}.')


# def sayHello(name='Unknown',age =18):
#     if name=='Unknown':
#         print("Unkown person!.")
#     else:
#         print(f'Hello {name}.')

# def sayHello(name,age =18):
#     if name=='Unknown':
#         print("Unkown person!.")
#     else:
#         print(f'Hello {name} and your age is {age}')


# def power(sup,sub):
#     return sup**sub

# number1 = int(input("Enter the first number: "))
# number2 = int(input("Enter the second number: "))

# power_result = power(number1,number2)
# print(f'The power of the two numbers is {power_result}')

def multi(*numbers):
    result = 1
    result2 = 1
    for i in range(0,len(numbers)):
        result *= numbers[i]
    for number in numbers:
        result2 *= number
    return result,result2

result,result2 = multi(45,8,9,65,66,22,88,8)
print(f'The result 1: {result}')
print(f'The result 2: {result2}')

def student_info(name,age,**kwargs):
    print(f'Name: {name}')
    print(f'Age: {age}')
    for key,value in kwargs.items():
        print(f'{key}: {value}')
student_info('John',25,grade='A',school='ABC School',hobby='Football')


