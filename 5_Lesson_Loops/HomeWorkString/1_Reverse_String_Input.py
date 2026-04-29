'''
Docstring for 5_Lesson_Loops.HomeWorkString.1_Reverse_String_Input
Reverse String Input, the user input anything and the program reverse it

'''

# user input
userStringInput = input("Please enter your string here\n let it be anything:")
StringLength = len(userStringInput)

reversedString = ""
# First way, reversing and printing user input

for stringIndex in userStringInput:
    reversedString = stringIndex + reversedString
print(f"Reversed String is: {reversedString}")

#Second way, reversing and printing user input
# userStringReversed = userStringInput[0]
# for i in range(StringLength-1, 0, -1):
#     print(userStringInput[i])
# print(userStringReversed)

# Third way, another method is
# print(userStringInput[::-1])

