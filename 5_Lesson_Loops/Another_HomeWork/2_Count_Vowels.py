'''
Docstring for 5_Lesson_Loops.Another_HomeWork.2_Count_Vowels
'''

# -----------------------------------------------------------------------------
# 2. Count Vowels
#    Description: Ask for a sentence, count the vowels (a,e,i,o,u) init,
#    print the final count.
#    Concepts: for loop, if condition, in operator.
# -----------------------------------------------------------------------------

# --- Solution 1: use a list of vowels and 'in' ---
sentence = input("Enter a sentence: ").lower()
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print("Vowel count (sol1):", count)

# --- Solution 2: check each vowel with 'or' ---
sentence = input("Enter a sentence: ").lower()
count = 0
for char in sentence:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        count += 1
print("Vowel count (sol2):", count)