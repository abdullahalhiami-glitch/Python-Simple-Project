'''
Docstring for 5_Lesson_Loops.HomeWorkString.8_Star_Trigalar
'''

NumOfRows = int(input("Enter The Number of rows: "))
ChoosedCharacter = input("Enter Any character to draw the trignagle : ")

#printing Triangle
for i in range(1,NumOfRows+1):
    for j in range(NumOfRows - i):
        print(" ",end="")
    for k in range(i):
        print(ChoosedCharacter,end="")
    print()

#printing X Pattern 
for i in range(NumOfRows):
    for j in range(NumOfRows):
        if i == j or j == NumOfRows - 1 - i:
            print(ChoosedCharacter, end="")
        else:
            print(" ", end="")
    print()

#printing Triangle
for i in range(1,NumOfRows+1):
    for j in range(NumOfRows - i -1):
        print(" ",end="")
    for k in range(2 * i + 1):
        print(ChoosedCharacter,end="")
    print()
    
# --- Solution 2: string multiplication for spaces and stars ---
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)


# -- Solution 1: nested loops for spaces and stars ---
# rows = int(input("Enter number of rows: "))
# for i in range(1, rows + 1):
#     # print spaces
#     for j in range(rows - i):
#         print(" ", end="")
#     # print stars
#     for k in range(i):
#         print("*", end="")
#     print()   # new line