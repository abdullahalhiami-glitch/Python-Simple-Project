'''
Docstring for 5_Lesson_Loops.HomeWorkString.6_Cleaning_Whitespaces
'''

#Asking the user to input a full sentence to clear up the unwanted or unnecessary white spaces
whiteSpaceSentence = input("Enter a sentence full with white spaces\n\t to clear it up\n\t\t Please, enter your sentence here: ")

clearedWhiteSpace = whiteSpaceSentence.strip()
spiltSentence = clearedWhiteSpace.split()
clearedSentence = ' '.join(spiltSentence)
print(clearedSentence)

# --- Solution 2: split alone (no explicit strip needed) ---
sentence = input("Enter a messy sentence: ")
# split() already ignores leading/trailing whitespace and splits on any whitespace
words = sentence.split()
clean = ' '.join(words)
print("Cleaned sentence (sol2):", clean)