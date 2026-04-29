# =============================================================================
# PYTHON BUILT-IN FUNCTIONS THAT WORK WITH LISTS
# =============================================================================
# These functions take a list (or any iterable) as argument.
# They return new values or iterators; they never modify the original list
# (except for `list()` which creates a new list from another iterable).
# =============================================================================

# ---------- 1. len(list) ----------
# Returns the number of elements in the list (length).
# Time complexity: O(1) – length is stored internally.
print("=" * 60)
print("1. len(list) – Number of elements")
my_list = [10, 20, 30, 40]
length = len(my_list)
print(f"List: {my_list}")
print(f"Length: {length}\n")  # 4
# Works on empty list:
empty = []
print(f"Length of empty list: {len(empty)}\n")  # 0

# ---------- 2. max(list) / min(list) ----------
# Returns the largest / smallest element in the list.
# Raises ValueError if list is empty.
# Can accept a `key` function (like sort).
print("=" * 60)
print("2. max(list), min(list) – Largest / smallest element")
numbers = [5, 2, 8, 1, 9]
print(f"Numbers: {numbers}")
print(f"Maximum: {max(numbers)}")   # 9
print(f"Minimum: {min(numbers)}")   # 1

# With strings (lexicographic order)
words = ["apple", "Banana", "cherry"]
print(f"Words: {words}")
print(f"Max (case-sensitive): {max(words)}")     # 'cherry' because 'c' > 'B' as ASCII
print(f"Max (case-insensitive): {max(words, key=str.lower)}")  # 'cherry' (because lowercased 'c' > 'a' > 'b')

# With key function (e.g., by length)
print(f"Longest word: {max(words, key=len)}")    # 'Banana' (length 6)

# ---------- 3. sum(list, start=0) ----------
# Returns the total of all elements (must be numeric).
# Optional `start` value is added to the total.
# Raises TypeError if list contains non‑numeric values.
print("=" * 60)
print("3. sum(list) – Sum of numeric elements")
nums = [1, 2, 3, 4]
total = sum(nums)
print(f"List: {nums}, sum = {total}")          # 10
total_start10 = sum(nums, 10)
print(f"Sum with start=10: {total_start10}")   # 20
# sum(["a", "b"]) would raise TypeError – use ''.join() for strings

# ---------- 4. sorted(list, key=None, reverse=False) ----------
# Returns a NEW sorted list from the original (original unchanged).
# Parameters same as list.sort().
print("=" * 60)
print("4. sorted(list) – New sorted list, original unchanged")
original = [3, 1, 4, 1, 5]
sorted_asc = sorted(original)
sorted_desc = sorted(original, reverse=True)
print(f"Original: {original}")
print(f"Sorted ascending: {sorted_asc}")   # [1,1,3,4,5]
print(f"Sorted descending: {sorted_desc}") # [5,4,3,1,1]
print(f"Original still: {original}")       # unchanged

# With key function:
words = ["cat", "elephant", "bird"]
sorted_by_len = sorted(words, key=len)
print(f"Sorted by length: {sorted_by_len}")  # ['cat', 'bird', 'elephant']

# ---------- 5. reversed(list) ----------
# Returns an iterator that yields elements in reverse order.
# To get a list, wrap with list().
# Original list unchanged.
print("=" * 60)
print("5. reversed(list) – Reverse iterator")
original = [1, 2, 3, 4]
rev_iter = reversed(original)
print(f"Reversed iterator: {rev_iter} (not a list)")
rev_list = list(rev_iter)
print(f"As list: {rev_list}")           # [4,3,2,1]
print(f"Original unchanged: {original}")

# You can iterate directly:
for item in reversed(original):
    print(f"Loop reversed: {item}")

# ---------- 6. all(list) ----------
# Returns True if ALL elements in the list are truthy.
# Returns True for empty list.
print("=" * 60)
print("6. all(list) – Check if all elements are truthy")
list1 = [True, 1, "hello", [1,2]]
list2 = [True, 0, "hello"]   # 0 is falsy
list3 = []                   # empty list
print(f"all({list1}) = {all(list1)}")  # True
print(f"all({list2}) = {all(list2)}")  # False
print(f"all({list3}) = {all(list3)}")  # True (vacuously true)

# ---------- 7. any(list) ----------
# Returns True if AT LEAST ONE element is truthy.
# Returns False for empty list.
print("=" * 60)
print("7. any(list) – Check if any element is truthy")
list1 = [0, False, "", []]       # all falsy
list2 = [0, False, "hello", []]  # one truthy
print(f"any({list1}) = {any(list1)}")  # False
print(f"any({list2}) = {any(list2)}")  # True

# ---------- 8. list(iterable) ----------
# Constructor: creates a new list from any iterable (string, tuple, set, dict keys, range, etc.)
print("=" * 60)
print("8. list(iterable) – Create a list from an iterable")
from_str = list("abc")          # string -> ['a','b','c']
from_tuple = list((1,2,3))      # tuple -> [1,2,3]
from_range = list(range(5))     # range -> [0,1,2,3,4]
from_dict = list({"a":1, "b":2}) # dict keys -> ['a','b']
print(f"From string 'abc': {from_str}")
print(f"From tuple (1,2,3): {from_tuple}")
print(f"From range(5): {from_range}")
print(f"From dict keys: {from_dict}")

# ---------- 9. enumerate(list, start=0) ----------
# Returns an iterator of (index, element) pairs.
# Very useful in loops.
print("=" * 60)
print("9. enumerate(list) – Get index‑element pairs")
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(f"Index {idx}: {fruit}")
# With custom start:
for idx, fruit in enumerate(fruits, start=1):
    print(f"Position {idx}: {fruit}")

# ---------- 10. zip(list1, list2, ...) ----------
# Aggregates elements from multiple lists into tuples.
# Stops at the shortest list.
print("=" * 60)
print("10. zip(list1, list2, ...) – Pair elements from multiple lists")
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
zipped = list(zip(names, scores))
print(f"Zipped: {zipped}")  # [('Alice',85), ('Bob',92), ('Charlie',78)]

# Unzipping:
names2, scores2 = zip(*zipped)
print(f"Unzipped names: {names2}")
print(f"Unzipped scores: {scores2}")

# ---------- 11. map(function, list) ----------
# Applies function to every element, returns an iterator (lazy).
# To get list, wrap with list().
print("=" * 60)
print("11. map(function, list) – Apply function to each element")
def square(x):
    return x * x
numbers = [1, 2, 3, 4]
squared_iter = map(square, numbers)
squared_list = list(squared_iter)
print(f"Original: {numbers}")
print(f"Squared: {squared_list}")  # [1,4,9,16]

# With lambda:
cubed = list(map(lambda x: x**3, numbers))
print(f"Cubed: {cubed}")           # [1,8,27,64]

# ---------- 12. filter(function, list) ----------
# Returns iterator with elements where function returns True.
print("=" * 60)
print("12. filter(function, list) – Keep elements that satisfy condition")
def is_even(x):
    return x % 2 == 0
numbers = [1,2,3,4,5,6]
even_iter = filter(is_even, numbers)
even_list = list(even_iter)
print(f"Original: {numbers}")
print(f"Even numbers: {even_list}")  # [2,4,6]

# With lambda:
odd_list = list(filter(lambda x: x % 2 == 1, numbers))
print(f"Odd numbers: {odd_list}")    # [1,3,5]

# ---------- 13. reduce(function, list) – (from functools) ----------
# Not a built‑in (needs import), but extremely common with lists.
# Applies function cumulatively to reduce list to a single value.
from functools import reduce
print("=" * 60)
print("13. reduce(function, list) – Cumulative reduction (from functools)")
numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
print(f"Product of {numbers} = {product}")  # 24
# With initializer:
sum_with_start = reduce(lambda a, b: a + b, numbers, 10)
print(f"Sum starting from 10: {sum_with_start}")  # 20

# ---------- 14. any other? 'slice' is not a function, but a built-in class ----------
# slice(start, stop, step) can be used to extract portions, but it's rarely called directly.
print("=" * 60)
print("14. slice() – Create slice object (used in list indexing)")
numbers = [0,1,2,3,4,5]
s = slice(2, 5)      # equivalent to [2:5]
print(f"numbers[{s}] = {numbers[s]}")  # [2,3,4]
# Also: slice(1,6,2) -> [1:6:2]

# =============================================================================
# SUMMARY OF BUILT-IN FUNCTIONS FOR LISTS:
# - len(), max(), min(), sum()   →  scalar results
# - sorted(), reversed()         →  new sorted/reversed iterable/list
# - all(), any()                 →  boolean checks
# - list()                       →  constructor from any iterable
# - enumerate()                  →  index‑value pairs
# - zip()                        →  parallel pairing of lists
# - map()                        →  transform each element
# - filter()                     →  keep elements passing test
# - reduce() (from functools)    →  cumulative reduction
# - slice()                      →  create slice objects
# 
# IMPORTANT: None of these modify the original list (except list() which creates a new one).
# For in‑place modification, use list methods like .sort(), .reverse(), .append() etc.
# =============================================================================