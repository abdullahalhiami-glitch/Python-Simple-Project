import random 
import string

# def generate_password(length):
#     if length < 8:
#         print("Password should be at least 8 characters long.")
#         return None
    
#     # Define the character sets
#     uppercase_letters = string.ascii_uppercase
#     lowercase_letters = string.ascii_lowercase
#     digits = string.digits
#     punctuation = string.punctuation
    
#     # Ensure the password includes at least one character from each set
#     password = [
#         random.choice(uppercase_letters),
#         random.choice(lowercase_letters),
#         random.choice(digits),
#         random.choice(punctuation)
#     ]
    
#     # Fill the remaining length with a mix of all character sets
#     all_characters = uppercase_letters + lowercase_letters + digits + punctuation
#     password += random.choices(all_characters, k=length - 4)
    
#     # Shuffle the password list to avoid predictable patterns
#     random.shuffle(password)
    
#     # Join the list into a string and return it
#     return ''.join(password)
# # Get the desired password length from the user
# try:
#     password_length = int(input("Enter the desired password length (at least 8 characters): "))
#     generated_password = generate_password(password_length)
#     if generated_password:
#         print(f"Generated Password: {generated_password}")
# except ValueError:
#     print("Please enter a valid integer for the password length.")

# #_____________________________________________________
# legth = int(input("Enter the desired password length (at least 8 characters): "))
# lowercase = string.ascii_lowercase
# uppercase = string.ascii_uppercase
# numbers = string.digits
# symbols = string.punctuation

# all_characters = lowercase + uppercase + numbers + symbols
# temp = random.sample(all_characters, legth)
# password = "".join(temp)
# print(f"Generated Password: {password}")

length = int(input("Enter the desired password length (at least 8 characters): "))
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

upperLetters = random.choice(uppercase)
lowerLetters = random.choice(lowercase)
numbers = random.choices(digits, k= 2)
symbols = random.choices(punctuation, k= 2)
joined = upperLetters + lowerLetters + ''.join(numbers) + ''.join(symbols)
password = ''.join(random.sample(joined, len(joined)))
print(f"Generated Password: {password}")

