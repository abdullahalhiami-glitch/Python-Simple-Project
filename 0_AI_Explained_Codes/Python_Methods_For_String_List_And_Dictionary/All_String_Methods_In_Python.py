#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COMPREHENSIVE GUIDE TO PYTHON STRING FUNCTIONS (METHODS)
========================================================
This script demonstrates every built-in string method available in Python 3.x.
Additionally, it shows len(), str(), and the 'in' operator, which are often used
with strings.

All string methods are non-destructive because strings are immutable -
they return a new string or a value without modifying the original.
"""

# =============================================================================
# 1. str.capitalize()
#    Returns a copy of the string with its first character uppercase and the
#    rest lowercase. Non-alphabetic first character leaves the rest unchanged.
# =============================================================================
print("\n--- str.capitalize() ---")
s = "hello WORLD"
result = s.capitalize()
print(f"Original: '{s}' -> Capitalized: '{result}'")  # 'Hello world'
# Note: The rest of the string is forced to lowercase, not just first letter.

# =============================================================================
# 2. str.casefold()
#    Aggressive lowercase for case-insensitive matching. More powerful than
#    lower() for certain Unicode characters (e.g., German 'ß' becomes 'ss').
# =============================================================================
print("\n--- str.casefold() ---")
s = "Straße"
result = s.casefold()
print(f"Original: '{s}' -> casefold: '{result}'")      # 'strasse'
print(f"Compare with lower(): '{s.lower()}'")          # 'straße'

# =============================================================================
# 3. str.center(width[, fillchar])
#    Returns centered string padded with fillchar (default space).
#    If width <= len(s) -> returns original string.
# =============================================================================
print("\n--- str.center() ---")
s = "Python"
result = s.center(12, '-')
print(f"Original: '{s}' -> center(12, '-'): '{result}'")  # '---Python---'
result2 = s.center(3)                                      # width smaller
print(f"center(3): '{result2}'")                           # 'Python'

# =============================================================================
# 4. str.count(sub[, start[, end]])
#    Returns number of non-overlapping occurrences of substring 'sub' in the
#    slice s[start:end]. start and end are optional (default whole string).
# =============================================================================
print("\n--- str.count() ---")
s = "ababcab"
count = s.count("ab")
print(f"'{s}'.count('ab') -> {count}")          # 3
count2 = s.count("ab", 2)                       # from index 2 to end
print(f"count('ab', 2) -> {count2}")            # 1 (only last 'ab' at index 4)

# =============================================================================
# 5. str.encode(encoding='utf-8', errors='strict')
#    Returns a bytes representation of the string. 'errors' can be 'ignore',
#    'replace', etc.
# =============================================================================
print("\n--- str.encode() ---")
s = "café"
encoded = s.encode('utf-8')
print(f"'{s}' encoded to bytes: {encoded}")     # b'caf\xc3\xa9'

# =============================================================================
# 6. str.endswith(suffix[, start[, end]])
#    Returns True if the string ends with the specified suffix (can be a tuple
#    of suffixes). start/end limit the check to a slice.
# =============================================================================
print("\n--- str.endswith() ---")
s = "hello.py"
print(f"'{s}'.endswith('.py') -> {s.endswith('.py')}")          # True
print(f"endswith(('.txt', '.py')) -> {s.endswith(('.txt','.py'))}") # True
print(f"endswith('.py', 0, 5) -> {s.endswith('.py', 0, 5)}")    # False (slice 'hello')

# =============================================================================
# 7. str.expandtabs(tabsize=8)
#    Replaces tab characters (\t) with spaces. Each tab is replaced with enough
#    spaces to reach the next tabstop (multiples of tabsize).
# =============================================================================
print("\n--- str.expandtabs() ---")
s = "a\tb\tc"
print(f"Original: '{s}'")
print(f"expandtabs(4): '{s.expandtabs(4)}'")    # 'a   b   c' (1 space + 3, then 2+2)

# =============================================================================
# 8. str.find(sub[, start[, end]])
#    Returns the lowest index where sub is found, or -1 if not found.
#    Use rfind() for highest index. start/end are slice limits.
# =============================================================================
print("\n--- str.find() ---")
s = "hello world"
pos = s.find("world")
print(f"'{s}'.find('world') -> {pos}")          # 6
pos2 = s.find("xyz")
print(f"find('xyz') -> {pos2}")                 # -1

# =============================================================================
# 9. str.format(*args, **kwargs)
#    Performs string formatting using placeholders {}.
#    Very powerful, supports positional, keyword, and index-based arguments.
# =============================================================================
print("\n--- str.format() ---")
name = "Alice"
age = 30
s = "Name: {}, Age: {}".format(name, age)
print(s)                                        # 'Name: Alice, Age: 30'
s2 = "Name: {n}, Age: {a}".format(n=name, a=age)
print(s2)                                       # 'Name: Alice, Age: 30'

# =============================================================================
# 10. str.format_map(mapping)
#     Similar to format() but takes a dictionary (or mapping) directly.
# =============================================================================
print("\n--- str.format_map() ---")
data = {'name': 'Bob', 'age': 25}
s = "User: {name}, Age: {age}".format_map(data)
print(s)                                        # 'User: Bob, Age: 25'

# =============================================================================
# 11. str.index(sub[, start[, end]])
#     Like find(), but raises ValueError if sub is not found.
# =============================================================================
print("\n--- str.index() ---")
s = "hello world"
try:
    pos = s.index("world")
    print(f"index('world') -> {pos}")           # 6
    pos2 = s.index("xyz")
except ValueError as e:
    print(f"index('xyz') raises: {e}")

# =============================================================================
# 12. str.isalnum()
#     Returns True if all characters are alphanumeric (a-z, A-Z, 0-9) and at
#     least one character. False otherwise (spaces, punctuation return False).
# =============================================================================
print("\n--- str.isalnum() ---")
print(f"'abc123'.isalnum() -> {'abc123'.isalnum()}")      # True
print(f"'abc 123'.isalnum() -> {'abc 123'.isalnum()}")    # False (space)

# =============================================================================
# 13. str.isalpha()
#     True if all characters are alphabetic and at least one character.
# =============================================================================
print("\n--- str.isalpha() ---")
print(f"'Hello'.isalpha() -> {'Hello'.isalpha()}")        # True
print(f"'Hello123'.isalpha() -> {'Hello123'.isalpha()}")  # False

# =============================================================================
# 14. str.isascii()
#     True if the string is empty or all characters are ASCII (code point <128).
#     Python 3.7+.
# =============================================================================
print("\n--- str.isascii() ---")
print(f"'abc'.isascii() -> {'abc'.isascii()}")            # True
print(f"'café'.isascii() -> {'café'.isascii()}")          # False (é not ASCII)

# =============================================================================
# 15. str.isdecimal()
#     True if all characters are decimal digits (0-9) and at least one char.
#     Superscripts, fractions, Roman numerals return False.
# =============================================================================
print("\n--- str.isdecimal() ---")
print(f"'123'.isdecimal() -> {'123'.isdecimal()}")        # True
print(f"'½'.isdecimal() -> {'½'.isdecimal()}")            # False (fraction)

# =============================================================================
# 16. str.isdigit()
#     True if all characters are digits (0-9, plus superscripts, subscripts,
#     fractions like ½, etc.). Broader than isdecimal().
# =============================================================================
print("\n--- str.isdigit() ---")
print(f"'123'.isdigit() -> {'123'.isdigit()}")            # True
print(f"'½'.isdigit() -> {'½'.isdigit()}")                # True (vs isdecimal false)

# =============================================================================
# 17. str.isidentifier()
#     True if the string is a valid Python identifier (starts with letter/_,
#     followed by letters/digits/_).
# =============================================================================
print("\n--- str.isidentifier() ---")
print(f"'_var1'.isidentifier() -> {'_var1'.isidentifier()}")  # True
print(f"'1var'.isidentifier() -> {'1var'.isidentifier()}")    # False

# =============================================================================
# 18. str.islower()
#     True if at least one cased character and all cased chars are lowercase.
#     Non-cased chars (digits, punctuation) are ignored.
# =============================================================================
print("\n--- str.islower() ---")
print(f"'hello123'.islower() -> {'hello123'.islower()}")    # True
print(f"'Hello'.islower() -> {'Hello'.islower()}")          # False

# =============================================================================
# 19. str.isnumeric()
#     True if all characters are numeric (digits, fractions, Roman numerals,
#     Chinese numbers, etc.). Broader than isdigit().
# =============================================================================
print("\n--- str.isnumeric() ---")
print(f"'123'.isnumeric() -> {'123'.isnumeric()}")          # True
print(f"'½'.isnumeric() -> {'½'.isnumeric()}")              # True
print(f"'一二三'.isnumeric() -> {'一二三'.isnumeric()}")      # True (Chinese numerals)

# =============================================================================
# 20. str.isprintable()
#     True if all characters are printable (including space, not control chars
#     like \n, \t, \r). Empty string is printable.
# =============================================================================
print("\n--- str.isprintable() ---")
print(f"'Hello\\n'.isprintable() -> {'Hello\n'.isprintable()}")  # False (\n not printable)
print(f"'Hello '".isprintable(), f"-> {'Hello '.isprintable()}")  # True

# =============================================================================
# 21. str.isspace()
#     True if there is at least one character and all characters are whitespace
#     (space, tab, newline, carriage return, etc.).
# =============================================================================
print("\n--- str.isspace() ---")
print(f"'   \\t\\n'.isspace() -> {'   \t\n'.isspace()}")     # True
print(f"'   a '.isspace() -> {'   a '.isspace()}")           # False

# =============================================================================
# 22. str.istitle()
#     True if the string is titlecased: each word starts with uppercase,
#     remaining letters are lowercase. Non-letter characters separate words.
# =============================================================================
print("\n--- str.istitle() ---")
print(f"'Hello World'.istitle() -> {'Hello World'.istitle()}")  # True
print(f"'Hello world'.istitle() -> {'Hello world'.istitle()}")  # False ('world' w lowercase)

# =============================================================================
# 23. str.isupper()
#     True if at least one cased character and all cased chars are uppercase.
# =============================================================================
print("\n--- str.isupper() ---")
print(f"'HELLO123'.isupper() -> {'HELLO123'.isupper()}")    # True
print(f"'Hello'.isupper() -> {'Hello'.isupper()}")          # False

# =============================================================================
# 24. str.join(iterable)
#     Returns a string formed by concatenating the elements of an iterable,
#     using the string as a separator. Elements must be strings.
# =============================================================================
print("\n--- str.join() ---")
words = ["Python", "is", "fun"]
separator = " "
result = separator.join(words)
print(f"'{separator}'.join({words}) -> '{result}'")        # 'Python is fun'
result2 = ", ".join(["apple", "banana"])
print(result2)                                             # 'apple, banana'

# =============================================================================
# 25. str.ljust(width[, fillchar])
#     Left-justifies the string, padding with fillchar (default space) to given width.
# =============================================================================
print("\n--- str.ljust() ---")
s = "Python"
result = s.ljust(10, '*')
print(f"'{s}'.ljust(10,'*') -> '{result}'")                # 'Python****'

# =============================================================================
# 26. str.lower()
#     Returns a copy with all cased characters converted to lowercase.
# =============================================================================
print("\n--- str.lower() ---")
s = "HELLO World"
print(f"'{s}'.lower() -> '{s.lower()}'")                  # 'hello world'

# =============================================================================
# 27. str.lstrip([chars])
#     Removes leading characters (whitespace by default). If chars given,
#     removes any combination of those characters.
# =============================================================================
print("\n--- str.lstrip() ---")
s = "   hello   "
print(f"'{s}'.lstrip() -> '{s.lstrip()}'")                # 'hello   '
s2 = "www.example.com"
print(f"'{s2}'.lstrip('w.') -> '{s2.lstrip('w.')}'")      # 'example.com'

# =============================================================================
# 28. static str.maketrans(x[, y[, z]])
#     Returns a translation table usable with translate(). Can be used with
#     one dict, or two equal-length strings (x -> y), or optionally a third
#     string of chars to delete.
# =============================================================================
print("\n--- str.maketrans() ---")
# Example: replace 'a' with '1', 'b' with '2', and delete 'c'
trans_table = str.maketrans("ab", "12", "c")
s = "abcab"
result = s.translate(trans_table)
print(f"translate('{s}') -> '{result}'")                  # '1212' (c removed)

# =============================================================================
# 29. str.partition(sep)
#     Splits the string at the first occurrence of sep. Returns a 3-tuple:
#     (head, sep, tail). If sep not found, returns (original, "", "").
# =============================================================================
print("\n--- str.partition() ---")
s = "hello-world-example"
result = s.partition("-")
print(f"'{s}'.partition('-') -> {result}")                # ('hello', '-', 'world-example')
result2 = s.partition("+")
print(f"partition('+') -> {result2}")                     # ('hello-world-example', '', '')

# =============================================================================
# 30. str.removeprefix(prefix)  (Python 3.9+)
#     If the string starts with prefix, returns the string without that prefix.
#     Otherwise returns the original string.
# =============================================================================
print("\n--- str.removeprefix() ---")
s = "TestString"
print(f"'{s}'.removeprefix('Test') -> '{s.removeprefix('Test')}'")  # 'String'
print(f"removeprefix('X') -> '{s.removeprefix('X')}'")              # 'TestString'

# =============================================================================
# 31. str.removesuffix(suffix)  (Python 3.9+)
#     If the string ends with suffix, returns the string without that suffix.
#     Otherwise returns the original.
# =============================================================================
print("\n--- str.removesuffix() ---")
s = "hello.py"
print(f"'{s}'.removesuffix('.py') -> '{s.removesuffix('.py')}'")    # 'hello'
print(f"removesuffix('.txt') -> '{s.removesuffix('.txt')}'")        # 'hello.py'

# =============================================================================
# 32. str.replace(old, new[, count])
#     Returns a copy with all occurrences of old replaced by new. If count given,
#     only the first 'count' occurrences are replaced.
# =============================================================================
print("\n--- str.replace() ---")
s = "one two three two"
result = s.replace("two", "four")
print(f"'{s}'.replace('two','four') -> '{result}'")        # 'one four three four'
result2 = s.replace("two", "four", 1)
print(f"replace with count=1 -> '{result2}'")              # 'one four three two'

# =============================================================================
# 33. str.rfind(sub[, start[, end]])
#     Highest index where sub is found, or -1 if not found.
# =============================================================================
print("\n--- str.rfind() ---")
s = "hello world hello"
pos = s.rfind("hello")
print(f"rfind('hello') -> {pos}")          # 12 (last occurrence)
pos2 = s.rfind("xyz")
print(f"rfind('xyz') -> {pos2}")           # -1

# =============================================================================
# 34. str.rindex(sub[, start[, end]])
#     Like rfind(), but raises ValueError if sub is not found.
# =============================================================================
print("\n--- str.rindex() ---")
s = "hello world hello"
try:
    pos = s.rindex("hello")
    print(f"rindex('hello') -> {pos}")     # 12
    pos2 = s.rindex("xyz")
except ValueError as e:
    print(f"rindex('xyz') raises: {e}")

# =============================================================================
# 35. str.rjust(width[, fillchar])
#     Right-justifies the string, padding on the left with fillchar.
# =============================================================================
print("\n--- str.rjust() ---")
s = "Python"
result = s.rjust(10, '*')
print(f"'{s}'.rjust(10,'*') -> '{result}'")                # '****Python'

# =============================================================================
# 36. str.rpartition(sep)
#     Splits at the last occurrence of sep. Returns 3-tuple (head, sep, tail).
#     If sep not found, returns ('', '', original).
# =============================================================================
print("\n--- str.rpartition() ---")
s = "hello-world-example"
result = s.rpartition("-")
print(f"'{s}'.rpartition('-') -> {result}")                # ('hello-world', '-', 'example')
result2 = s.rpartition("+")
print(f"rpartition('+') -> {result2}")                     # ('', '', 'hello-world-example')

# =============================================================================
# 37. str.rsplit(sep=None, maxsplit=-1)
#     Splits from the right. If sep not given, splits on whitespace. maxsplit
#     limits number of splits (from right).
# =============================================================================
print("\n--- str.rsplit() ---")
s = "a b c d"
result = s.rsplit(maxsplit=2)
print(f"rsplit(maxsplit=2) -> {result}")                  # ['a', 'b', 'c d']? Wait careful:
# Actually rsplit(' ', maxsplit=2) -> ['a', 'b', 'c d']? Let's test: default sep any whitespace
print(f"Actual: '{s}'.rsplit(None, 2) -> {s.rsplit(None, 2)}")  # ['a', 'b', 'c d']? On 3.10: ['a', 'b', 'c d']
# Better use explicit:
result = s.rsplit(' ', 2)
print(f"rsplit(' ',2) -> {result}")                       # ['a', 'b', 'c d']

# =============================================================================
# 38. str.rstrip([chars])
#     Removes trailing characters (whitespace by default). If chars given,
#     removes any combination of those characters from the end.
# =============================================================================
print("\n--- str.rstrip() ---")
s = "   hello   "
print(f"'{s}'.rstrip() -> '{s.rstrip()}'")                # '   hello'
s2 = "example.com///"
print(f"'{s2}'.rstrip('/') -> '{s2.rstrip('/')}'")        # 'example.com'

# =============================================================================
# 39. str.split(sep=None, maxsplit=-1)
#     Splits the string into a list of substrings. If sep specified, splits on
#     that exact separator. If sep is None (default), splits on any whitespace.
#     maxsplit limits number of splits from left.
# =============================================================================
print("\n--- str.split() ---")
s = "one two three"
result = s.split()
print(f"split() -> {result}")               # ['one', 'two', 'three']
result2 = s.split(' ', 1)
print(f"split(' ',1) -> {result2}")         # ['one', 'two three']

# =============================================================================
# 40. str.splitlines([keepends])
#     Splits at line boundaries (\n, \r\n, \r, etc.). Returns list of lines.
#     If keepends=True, line breaks are kept.
# =============================================================================
print("\n--- str.splitlines() ---")
s = "line1\nline2\r\nline3"
result = s.splitlines()
print(f"splitlines() -> {result}")          # ['line1', 'line2', 'line3']
result2 = s.splitlines(keepends=True)
print(f"splitlines(keepends=True) -> {result2}")  # ['line1\n', 'line2\r\n', 'line3']

# =============================================================================
# 41. str.startswith(prefix[, start[, end]])
#     True if string starts with prefix (can be tuple). start/end slice limits.
# =============================================================================
print("\n--- str.startswith() ---")
s = "hello.py"
print(f"'{s}'.startswith('hel') -> {s.startswith('hel')}")          # True
print(f"startswith(('.py','.txt')) -> {s.startswith(('.py','.txt'))}") # False

# =============================================================================
# 42. str.strip([chars])
#     Removes leading and trailing characters (whitespace default). chars is a
#     set of characters to remove.
# =============================================================================
print("\n--- str.strip() ---")
s = "   hello   "
print(f"'{s}'.strip() -> '{s.strip()}'")          # 'hello'
s2 = "www.example.com"
print(f"'{s2}'.strip('w.mc') -> '{s2.strip('w.mc')}'")  # 'example' (removes w, ., m, c from ends)

# =============================================================================
# 43. str.swapcase()
#     Returns a copy with uppercase characters converted to lowercase and vice
#     versa. Not locale-aware; e.g., 'ß' (sharp s) becomes 'SS' or stays?
#     In Python, 'ß'.swapcase() -> 'ß' (unchanged) because no uppercase mapping.
# =============================================================================
print("\n--- str.swapcase() ---")
s = "Hello World"
print(f"'{s}'.swapcase() -> '{s.swapcase()}'")    # 'hELLO wORLD'

# =============================================================================
# 44. str.title()
#     Returns a titlecased version: first letter of each word uppercase, rest
#     lowercase. Words are separated by any non-letter character.
# =============================================================================
print("\n--- str.title() ---")
s = "hello world! python"
print(f"'{s}'.title() -> '{s.title()}'")          # 'Hello World! Python'
# Note: apostrophes can cause odd results: "they're" -> "They'Re"

# =============================================================================
# 45. str.translate(table)
#     Uses a translation table (from maketrans) to replace/delete characters.
# =============================================================================
print("\n--- str.translate() ---")
trans = str.maketrans({'a': '1', 'b': '2', 'c': None})  # None means delete
s = "abcab"
result = s.translate(trans)
print(f"translate('{s}') -> '{result}'")                # '1212'

# =============================================================================
# 46. str.upper()
#     Returns a copy with all cased characters converted to uppercase.
# =============================================================================
print("\n--- str.upper() ---")
s = "Hello World"
print(f"'{s}'.upper() -> '{s.upper()}'")               # 'HELLO WORLD'

# =============================================================================
# 47. str.zfill(width)
#     Pads the string on the left with zeros to reach the given width. Handles
#     sign (+/-) by placing zeros after the sign. If width <= len(s), returns s.
# =============================================================================
print("\n--- str.zfill() ---")
s = "42"
print(f"'{s}'.zfill(5) -> '{s.zfill(5)}'")            # '00042'
s2 = "-42"
print(f"'-42'.zfill(5) -> '{s2.zfill(5)}'")           # '-0042' (zeros after sign)

# =============================================================================
# ADDITIONAL BUILT-IN FUNCTIONS FREQUENTLY USED WITH STRINGS
# =============================================================================
print("\n--- Additional built-in functions: len(), str(), 'in' ---")

# len() - returns number of characters (Unicode code points)
s = "Python"
print(f"len('{s}') -> {len(s)}")                       # 6

# str() - converts any object to its string representation
num = 123
print(f"str({num}) -> '{str(num)}'")                   # '123'

# 'in' operator - checks for substring membership
print(f"'Py' in 'Python' -> {'Py' in 'Python'}")       # True

# =============================================================================
# END OF DEMONSTRATION
# =============================================================================
print("\nAll string methods and related functions have been demonstrated.")