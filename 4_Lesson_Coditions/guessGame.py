'''
Docstring for 3_Lesson_Operators.HomeWork_Python.7_Guessing_Game
This is a guessing game you pick a number from 1 to 100 
'''
# used the random library to generate random numbers
import random 

#then we generated random numbers
number = random.randint(1,10)
numberExit = 5
while numberExit > 0:
    #then asked the user for a number that the user have guessed
    guessNumbwer = input("Guess a number between 1 to 10\nAnd the Enter the numer here: ")
    guessNumbwer = int(guessNumbwer)
    #then check if the number is equl or not
    if guessNumbwer == number:
        print("Congrates, You won.")
        break
    else:
        if guessNumbwer > number:
            print(f"Sorry, the Number you guessed is wrong")
            print("Your number is greater than the guessed number")
            print(f"Attempts Left {numberExit}")
            print('------------------------------------------------')
            numberExit -= 1
        else:
            print(f"Sorry, the Number you guessed is wrong")
            print("Your number is lower than the guessed number")
            print(f"Attempts Left {numberExit}")
            print('------------------------------------------------')
            numberExit -= 1
    if numberExit == 0:
        print("------------ Your five attempts have finished. --------------")

# #then asked the user for a number that the user have guessed
# guessNumbwer = input("Guess a number between 1 to 100\nAnd the Enter the numer here: ")
# guessNumbwer = int(guessNumbwer)

# #then check if the number is equl or not
# if guessNumbwer == number:
#     print("Congrates, You won.")
# else:
#     print(f"Sorry, the Number you guessed is wrong\n The number is {number}")