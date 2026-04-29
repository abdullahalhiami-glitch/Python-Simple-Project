# =============================================================================
# 15 Python Programs: Two Solutions Each
# All comments and variable names are in English.
# =============================================================================

# -----------------------------------------------------------------------------
# 1. Reverse Text Manually
#    Description: Ask for a text, create a new empty string, loop through 
#    characters of the original one by one to reverse it, then print the result.
#    Concepts: for loop, string concatenation.
# -----------------------------------------------------------------------------

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


# -----------------------------------------------------------------------------
# 4. Bad Words Filter
#    Description: Ask for a comment. If it contains specific bad words
#    (e.g., "سيء" or "غبي" – here we use "bad" and "stupid" in English),
#    replace them with stars and print the clean comment.
#    Concepts: replace() function.
# -----------------------------------------------------------------------------

# --- Solution 1: replace each word one by one ---
comment = input("Enter a comment: ")
bad_words = ["bad", "stupid"]  # using English examples to match the requirement

for word in bad_words:
    if word in comment:
        comment = comment.replace(word, '*' * len(word))
print("Clean comment (sol1):", comment)

# --- Solution 2: use a dictionary to map words to stars ---
comment = input("Enter a comment: ")
replacements = {"bad": "***", "stupid": "******"}  # length of stars matches word length
for word, stars in replacements.items():
    comment = comment.replace(word, stars)
print("Clean comment (sol2):", comment)


# -----------------------------------------------------------------------------
# 5. Toggle Case (Alternating Case)
#    Description: Ask for a text. Loop through its characters. If a character 
#    is lowercase, turn it uppercase; if uppercase, turn it lowercase.
#    (Challenge: do not use the built-in swapcase() function.)
#    Concepts: for loop, if...elif, isupper(), islower(), upper(), lower().
# -----------------------------------------------------------------------------

# --- Solution 1: build a new string character by character ---
text = input("Enter a text: ")
toggled = ""
for char in text:
    if char.isupper():
        toggled += char.lower()
    elif char.islower():
        toggled += char.upper()
    else:
        toggled += char   # keep other characters unchanged
print("Toggled text (sol1):", toggled)

# --- Solution 2: use a helper function with map() ---
def toggle_char(ch):
    if ch.isupper():
        return ch.lower()
    elif ch.islower():
        return ch.upper()
    return ch

text = input("Enter a text: ")
toggled = ''.join(map(toggle_char, text))
print("Toggled text (sol2):", toggled)


# -----------------------------------------------------------------------------
# 6. Extra Space Cleaner
#    Description: Ask for a sentence full of random extra spaces (at the 
#    beginning, end, and between words). Clean it so that only one space 
#    remains between each word.
#    Concepts: strip(), split(), join().
# -----------------------------------------------------------------------------

# --- Solution 1: strip then split then join ---
sentence = input("Enter a messy sentence: ")
trimmed = sentence.strip()        # remove leading/trailing spaces
words = trimmed.split()           # split at any whitespace, ignoring multiple spaces
clean = ' '.join(words)           # join with a single space
print("Cleaned sentence (sol1):", clean)

# --- Solution 2: split alone (no explicit strip needed) ---
sentence = input("Enter a messy sentence: ")
# split() already ignores leading/trailing whitespace and splits on any whitespace
words = sentence.split()
clean = ' '.join(words)
print("Cleaned sentence (sol2):", clean)


# -----------------------------------------------------------------------------
# 7. Palindrome Checker
#    Description: Ask for a word and check if it reads the same backwards.
#    Print "Palindrome" or "Not a palindrome".
#    Concepts: if...else, reversing text, string comparison ==.
# -----------------------------------------------------------------------------

# --- Solution 1: manual reversal with a loop ---
word = input("Enter a word: ")
reversed = ""
for char in word:
    reversed = char + reversed
if word == reversed:
    print("Palindrome")
else:
    print("Not a palindrome")

# --- Solution 2: slicing to reverse ---
word = input("Enter a word: ")
if word == word[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


# -----------------------------------------------------------------------------
# 8. Star Pyramid
#    Description: Ask for the number of rows, then print a pyramid of stars
#    that grows with each row.
#    Concepts: nested for loops, print() with end control.
# -----------------------------------------------------------------------------

# --- Solution 1: nested loops for spaces and stars ---
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    # print spaces
    for j in range(rows - i):
        print(" ", end="")
    # print stars
    for k in range(i):
        print("*", end="")
    print()   # new line

# --- Solution 2: string multiplication for spaces and stars ---
rows = int(input("Enter number of rows: "))
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)


# -----------------------------------------------------------------------------
# 9. Word Counter
#    Description: Ask for a full paragraph, count the number of words and print it.
#    Concepts: split(), len().
# -----------------------------------------------------------------------------

# --- Solution 1: split and len ---
paragraph = input("Enter a paragraph: ")
word_list = paragraph.split()
print("Word count (sol1):", len(word_list))

# --- Solution 2: manual counting by detecting word boundaries ---
paragraph = input("Enter a paragraph: ")
count = 0
in_word = False
for ch in paragraph:
    if ch != ' ' and not in_word:
        count += 1
        in_word = True
    elif ch == ' ':
        in_word = False
print("Word count (sol2):", count)


# -----------------------------------------------------------------------------
# 10. Letter Search Engine
#     Description: Ask for a text, then ask for a single letter to search for.
#     Print all the indices where that letter appears.
#     Concepts: for loop with range(len()) or enumerate(), if condition.
# -----------------------------------------------------------------------------

# --- Solution 1: range(len()) ---
text = input("Enter a text: ")
letter = input("Enter a letter to search for: ")
positions = []
for i in range(len(text)):
    if text[i] == letter:
        positions.append(i)
if positions:
    print("Letter found at indices:", positions)
else:
    print("Letter not found.")

# --- Solution 2: enumerate() ---
text = input("Enter a text: ")
letter = input("Enter a letter to search for: ")
positions = []
for idx, ch in enumerate(text):
    if ch == letter:
        positions.append(idx)
if positions:
    print("Letter found at indices:", positions)
else:
    print("Letter not found.")


# -----------------------------------------------------------------------------
# 11. Digit Hunter (Extract and sum digits)
#     Description: Ask for a text containing mixed letters and digits. Extract
#     only the digits, convert them to integers, sum them, and print the sum.
#     Concepts: for loop, isdigit(), int().
# -----------------------------------------------------------------------------

# --- Solution 1: loop and accumulate ---
text = input("Enter a text with letters and digits: ")
total = 0
for ch in text:
    if ch.isdigit():
        total += int(ch)
print("Sum of digits (sol1):", total)

# --- Solution 2: filter and sum with generator ---
text = input("Enter a text with letters and digits: ")
digits = filter(str.isdigit, text)
total = sum(int(d) for d in digits)
print("Sum of digits (sol2):", total)


# -----------------------------------------------------------------------------
# 12. Echo Letters (Double Repetition)
#     Description: Ask for a word, create a new text where each character of
#     the original is repeated twice (e.g., "Python" -> "PPyytthhoonn").
#     Concepts: for loop, string multiplication * and concatenation +.
# -----------------------------------------------------------------------------

# --- Solution 1: build string with += and * ---
word = input("Enter a word: ")
echo = ""
for ch in word:
    echo += ch * 2
print("Echo word (sol1):", echo)

# --- Solution 2: join with generator expression ---
word = input("Enter a word: ")
echo = ''.join(ch * 2 for ch in word)
print("Echo word (sol2):", echo)


# -----------------------------------------------------------------------------
# 13. Duplicate Letter Filter
#     Description: Ask for a text, print it after removing any duplicate
#     letters (keep only the first occurrence).
#     Concepts: for loop, not in operator to check new string.
# -----------------------------------------------------------------------------

# --- Solution 1: build new string and check 'not in' ---
text = input("Enter a text: ")
unique = ""
for ch in text:
    if ch not in unique:
        unique += ch
print("Without duplicates (sol1):", unique)

# --- Solution 2: use dict.fromkeys() preserving order (Python 3.7+) ---
text = input("Enter a text: ")
unique = ''.join(dict.fromkeys(text))
print("Without duplicates (sol2):", unique)


# -----------------------------------------------------------------------------
# 14. Comprehensive Text Analyzer
#     Description: Ask for a long sentence, print a report containing:
#     number of uppercase letters, lowercase letters, digits, and spaces.
#     Concepts: for loop, isupper(), islower(), isdigit(), isspace().
# -----------------------------------------------------------------------------

# --- Solution 1: separate counters and a single loop ---
sentence = input("Enter a long sentence: ")
upper_count = 0
lower_count = 0
digit_count = 0
space_count = 0

for ch in sentence:
    if ch.isupper():
        upper_count += 1
    elif ch.islower():
        lower_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch.isspace():
        space_count += 1

print(f"Uppercase: {upper_count}, Lowercase: {lower_count}, Digits: {digit_count}, Spaces: {space_count}")

# --- Solution 2: use sum with generator expressions ---
sentence = input("Enter a long sentence: ")
upper_count = sum(1 for ch in sentence if ch.isupper())
lower_count = sum(1 for ch in sentence if ch.islower())
digit_count = sum(1 for ch in sentence if ch.isdigit())
space_count = sum(1 for ch in sentence if ch.isspace())
print(f"Uppercase: {upper_count}, Lowercase: {lower_count}, Digits: {digit_count}, Spaces: {space_count}")


# -----------------------------------------------------------------------------
# 15. Mini Project: Smart Cashier System & Invoice Generation
#     Description: Simulate a supermarket checkout. Welcome the user, then
#     enter a while loop asking for product name and price. Add price to a
#     running total and build a text invoice using += and \n. Stop when
#     the user types "done". Then apply 15% tax, subtract a discount if
#     the subtotal is large, and print the final formatted invoice.
#     Concepts: while loop, string concatenation, if...else, arithmetic.
# -----------------------------------------------------------------------------

# --- Solution 1: build invoice as a single string incrementally ---
print("Welcome to Smart Cashier System")
print("Enter product name (or 'done' to finish):")

subtotal = 0.0
invoice = ""

while True:
    product = input("Product name: ")
    if product.lower() == 'done':
        break
    price = float(input("Price: "))
    subtotal += price
    # Add a formatted line for this product
    invoice += f"{product:<15} ${price:>8.2f}\n"

# Tax and discount
tax = subtotal * 0.15
discount = 0.0
if subtotal > 1000:
    discount = subtotal * 0.10   # 10% discount on large purchases

final_total = subtotal + tax - discount

# Append summary lines to the invoice
invoice += "-" * 30 + "\n"
invoice += f"Subtotal:          ${subtotal:>8.2f}\n"
invoice += f"Tax (15%):         ${tax:>8.2f}\n"
if discount > 0:
    invoice += f"Discount (10%):   -${discount:>8.2f}\n"
invoice += f"Total:             ${final_total:>8.2f}\n"

print("\n===== FINAL INVOICE =====")
print(invoice)

# --- Solution 2: store products in a list, build invoice at the end ---
print("\n--- Alternative Implementation ---")
print("Welcome to Smart Cashier System")
print("Enter product name (or 'done' to finish):")

products = []   # list of tuples (name, price)
subtotal = 0.0

while True:
    name = input("Product name: ")
    if name.lower() == 'done':
        break
    price = float(input("Price: "))
    products.append((name, price))
    subtotal += price

tax = subtotal * 0.15
discount = subtotal * 0.10 if subtotal > 1000 else 0.0
final_total = subtotal + tax - discount

invoice_lines = []
for name, price in products:
    invoice_lines.append(f"{name:<15} ${price:>8.2f}")
invoice_lines.append("-" * 30)
invoice_lines.append(f"Subtotal:          ${subtotal:>8.2f}")
invoice_lines.append(f"Tax (15%):         ${tax:>8.2f}")
if discount:
    invoice_lines.append(f"Discount (10%):   -${discount:>8.2f}")
invoice_lines.append(f"Total:             ${final_total:>8.2f}")

print("\n===== FINAL INVOICE =====")
print("\n".join(invoice_lines))