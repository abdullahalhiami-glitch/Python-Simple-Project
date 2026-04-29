'''
Docstring for 5_Lesson_Loops.Another_HomeWork.9_Words_Counter
'''

#input Paragraph
paragraph = input("Enter Your Paragraph here: ")

paragraphSplit = paragraph.split()
wordsCount = len(paragraphSplit)

print(f"The Words Count Is {wordsCount}.")