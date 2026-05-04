'''
Docstring for 3_Lesson_Operators.HomeWork_Python.7_Guessing_Game
This is a guessing game you pick a number from 1 to 100 
'''
# used the random library to generate random numbers
import random 

#then we generated random numbers
number = random.randint(1,100)

#then asked the user for a number that the user have guessed
guessNumbwer = input("Guess a number between 1 to 100\nAnd the Enter the numer here: ")
guessNumbwer = int(guessNumbwer)

#then check if the number is equl or not
if guessNumbwer == number:
    print("Congrates, You won.")
else:
    print(f"Sorry, the Number you guessed is wrong\n The number is {number}")