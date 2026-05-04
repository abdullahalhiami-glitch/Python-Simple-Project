'''
Docstring for 3_Lesson_Operators.HomeWork_Python.7_Guessing_Game
This is a guessing game you pick a number from 1 to 100 
'''
# used the random library to generate random numbers
import random 

value1 = random.random() # this will generate a random number between 0 and 1
value2 = random.uniform(1, 100) # this will generate a random number between 1 and 100
roll_dice = random.randint(1, 6) # this will generate a random integer between 1 and 6

print(f"Random number between 0 and 1: {value1}")
print(f"Random number between 1 and 100: {value2}")
print(f"Random number between 1 and 100: {value2:.2f}") # this will print the number with 2 decimal places
print(f"Rolling a dice: {roll_dice}")

greetings = ['Hello', 'Hi', 'Hey', 'Welcome', 'Good day', 'Howdy', 'Greetings', 'Salutations', 'Hola', 'Bonjour', 'Ciao', 'Namaste', 'Salaam', 'Shalom', 'Konnichiwa', 'Annyeonghaseyo', 'Guten Tag', 'Olá', 'Zdravstvuyte', 'Merhaba', 'Sawubona', 'Sannu', 'Aloha', 'Yassas', 'Szia', 'Tere', 'Sveiki', 'Bula', 'Mingalaba', 'Kia ora', 'Salam', 'As-salamu alaykum', 'Nǐ hǎo', 'Dzień dobry', 'Jambo', 'Sain baina uu', 'Marhaba', 'Shikamoo', 'Hey']

random_greeting = random.choice(greetings) # this will randomly select a greeting from the list
print(f'Random Greeting: {random_greeting}, Abdullah.')

colors = ['Red', 'Green', 'Blue', 'Yellow', 'Purple', 'Orange', 'Pink', 'Brown', 'Black', 'White', 'Gray', 'Cyan', 'Magenta', 'Lime', 'Maroon', 'Navy', 'Olive', 'Teal', 'Violet', 'Indigo']

color_result = random.sample(colors, 3) # this will randomly select 3 colors from the list
color_result2 = random.choices(colors ,k=5) # this will randomly select 10 colors from the list
color_result3 = random.choices(colors, weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] ,k=5) # this will randomly select 10 colors from the list
print(f'Randomly selected colors: {color_result}')
print(f'Randomly selected colors (with replacement): {color_result2}')
print(f'Randomly selected colors (with weights): {color_result3}')

deck = list(range(1, 53)) # this will create a list of numbers from 1 to 52 representing a deck of cards
random.shuffle(deck) # this will shuffle the deck of cards
print(f'Shuffled deck of cards: {deck}')

grab_deck = random.sample(deck, 5) # this will randomly select 5 unique cards from the deck
print(f'Randomly selected cards: {grab_deck}')

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