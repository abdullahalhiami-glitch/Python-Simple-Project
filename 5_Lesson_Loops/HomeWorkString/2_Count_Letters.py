''' 4. str.count(sub[, start[, end]])
    Returns number of non-overlapping occurrences of substring 'sub' in the
    slice s[start:end]. start and end are optional (default whole string).
'''
#user input sentence
sentence = input("Please, enter your sentence here:")

vowels = "aeiuoAEIUO"
vowelsCount = 0
#Calculate all vowels
for letter in sentence:
    if letter in vowels:
        vowelsCount += 1
#output All vowels in the sentence
print(f"Vowels Count is {vowelsCount}")




vowel_a_A_count = 0
vowel_e_E_count = 0
vowel_u_U_count = 0
vowel_i_I_count = 0
vowel_o_O_count = 0
const_letters = 0
total_count = 0
for letter in sentence:
    if letter == "a" or letter == "A":
        vowel_a_A_count += 1
        total_count += 1
    elif letter == "e" or letter == "E":
        vowel_e_E_count += 1
        total_count += 1
    elif letter == "u" or letter == "U":
        vowel_u_U_count += 1
        total_count += 1
    elif letter == "i" or letter == "I":
        vowel_i_I_count += 1
        total_count += 1
    elif letter == "o" or letter == "O":
        vowel_o_O_count += 1
        total_count += 1
    else:
        const_letters += 1
        total_count += 1

print(f"Vowel a A count is {vowel_a_A_count}")
print(f"Vowel e E count is {vowel_e_E_count}")
print(f"Vowel u U count is {vowel_u_U_count}")
print(f"Vowel i I count is {vowel_i_I_count}")
print(f"Vowel o O count is {vowel_o_O_count}")
print(f"Constant Letters count is {const_letters}")
print(f"Total Letters count is {total_count}")



