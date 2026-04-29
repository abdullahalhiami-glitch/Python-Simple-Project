'''
Docstring for 5_Lesson_Loops.HomeWorkString.5_CaseLetter_Switching
'''

#input the sentence
sentence = input("Enter your sentence here:")
swapCase = ""

#truning the uppercase letters to lowercase and the opsite
for letter in sentence:
    if letter.isupper():
        swapCase += letter.lower()
    elif letter.islower():
        swapCase += letter.upper()
    else:
        swapCase += letter
print(f"Sentence after swaping lower and upper case letters\n{swapCase}")



# text = input("Enter a text: ")
# toggled = ""
# for char in text:
#     if char.isupper():
#         toggled += char.lower()
#     elif char.islower():
#         toggled += char.upper()
#     else:
#         toggled += char   # keep other characters unchanged
# print("Toggled text (sol1):", toggled)