'''
Docstring for 5_Lesson_Loops.Another_HomeWork.1_Reversed_String
'''

# --- Solution 1: iterate indices from the end to the beginning ---
text = input("Enter a text: ")
reversed_text = ""
for i in range(len(text)-1, -1, -1):
    reversed_text += text[i]
print("Reversed text (sol1):", reversed_text)

# --- Solution 2: prepend each character to the growing string ---
text = input("Enter a text: ")
reversed_text = ""
for char in text:
    reversed_text = char + reversed_text
print("Reversed text (sol2):", reversed_text)