'''
Docstring for 8_Lesson_Dictionaries.Practice_Dictionaries.4_Analyis_The_Count_Of_Each_Letter_In_A_Sentence
'''
#input your sentence here
sentence = list(input("Enter your sentence here: "))
# sentence = input("Enter your sentence here: ").split()
# mylist = " To myself, sorry for all the pain that you don't deserve "
joined_sentence = "".join(sentence)
print(sentence)


dic = {}
# or you can use split to make the keys the words
for letter in sentence:
    if letter not in dic.keys():
        dic[letter]=1
    else:
        dic[letter]+=1    
print(f"------------ Your sentence is {joined_sentence}. --------------------")       
for key,value in dic.items():
    print(f"The letter is {key} || and its count is {value}.")






# dic = {}
# # or you can use split to make the keys the words
# for i in mylist:
#     if i not in dic.keys():
#         dic[i]=1
#     else:
#         dic[i]+=1    
# print(dic)       