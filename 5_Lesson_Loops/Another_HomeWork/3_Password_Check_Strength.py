'''
Docstring for 5_Lesson_Loops.Another_HomeWork.3_Password_Check_Strength
'''

# -----------------------------------------------------------------------------
# 3. Password Strength Checker
#    Description: Ask for a new password and check 3 conditions: length > 8,
#    contains at least one digit, contains at least one uppercase letter.
#    Print "Strong password" or "Weak password".
#    Concepts: len(), for loop, isupper(), isdigit().
# -----------------------------------------------------------------------------

# --- Solution 1: boolean flags set inside a single loop ---
password = input("Enter a new password: ")
length_ok = len(password) > 8
has_digit = False
has_upper = False

for char in password:
    if char.isdigit():
        has_digit = True
    if char.isupper():
        has_upper = True

if length_ok and has_digit and has_upper:
    print("Strong password")
else:
    print("Weak password")

# --- Solution 2: using any() with generator expressions ---
password = input("Enter a new password: ")
length_ok = len(password) > 8
has_digit = any(ch.isdigit() for ch in password)
has_upper = any(ch.isupper() for ch in password)

if length_ok and has_digit and has_upper:
    print("Strong password")
else:
    print("Weak password")