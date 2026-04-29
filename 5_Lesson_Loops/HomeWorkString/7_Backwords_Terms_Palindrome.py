'''
Docstring for 5_Lesson_Loops.HomeWorkString.7_Backwords_Terms_Palindrome
'''
print("---------------- A program that checks if the word Palindrome or Not ---------------")
palindromeWord = input("\tEnter the word here: ").lower()

#reversed Word or sentence
reversed = "".lower()
for letter in palindromeWord:
    reversed = letter + reversed
# print(f"Reversed : {reversed}")

#check if the reversed word is equal the same word the user enter
if reversed == palindromeWord:
    print("Your Word Matches Its Backwords Its Reversed Word.")
    print(f"Your Word is : {palindromeWord} and its reversed is : {reversed}.")
else:
    print("Your Word Doesn't Match its reversed.")

