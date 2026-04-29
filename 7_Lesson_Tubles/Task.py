'''
Docstring for 7_Lesson_Tubles.Task
'''

sentence = input("Enter your sentence here: ").lower()

sentenceLength = len(sentence)
vowels = ['a','e','u','i','o']
newLength = 1
if sentenceLength < 5:
    print('Sentence is too short')
else:
    for letter in sentence:
        if letter.isnumeric():
            newLength +=5
        elif letter in vowels:
        # elif letter == 'a' or letter == 'e' or letter == 'u' or letter == 'i' or letter == 'o':
            newLength += 3
        elif letter == " " or letter.isspace:
            newLength -= 1
        else:
            newLength += 1
print(f"The Power of your words is {newLength}")
        