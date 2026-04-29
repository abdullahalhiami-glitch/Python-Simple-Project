'''
Docstring for 0_AI_Explained_Codes.Python_Methods_For_String_List_And_Dictionary.List_Comerheriosn
'''

odd_number = [1,3,5,7,9,11,13]
list_number = [1,2,3,4,5,6,7,8,9,10,11,12,13]
even_number = []
#simples way
for number in odd_number:
    even_number.append(number+1)
print(even_number)

#comperhaisive list
even_number = [number+1 for number in odd_number]
print(even_number)

#comperhaisive list with conditions
even_number = [number for number in list_number if number%2==0]
print(even_number)
#
odd2_number = [number for number in list_number if number%2==1]
print(odd2_number)
#



