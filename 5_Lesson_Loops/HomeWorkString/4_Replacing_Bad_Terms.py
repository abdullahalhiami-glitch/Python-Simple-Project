'''
Docstring for 5_Lesson_Loops.HomeWorkString.4_Replacing_Bad_Terms
'''
#     str.replace(old, new[, count])
#     Returns a copy with all occurrences of old replaced by new. If count given,
#     only the first 'count' occurrences are replaced.

#Input Bad Words
comment = input("Enter a comment: ")
bad_words = ["bad", "stupid", "shit", "fuck", "bitch"]

#checking bad words
for word in bad_words:
    if word in comment:
        comment = comment.replace(word, '*' * len(word))
print("Clean comment (sol1):", comment)
