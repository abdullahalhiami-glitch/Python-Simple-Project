# =============================================================================
# PYTHON LIST METHODS - COMPLETE GUIDE WITH EXAMPLES
# =============================================================================
# Lists are mutable sequences. All methods below modify the list in place
# except for copy() and count() which return new values/lists.
# =============================================================================

# ---------- 1. append(x) ----------
# Adds a single element x to the end of the list.
# Returns: None (modifies list in place).
# Time complexity: O(1) amortized.
print("=" * 50)
print("1. append(x) - Add element to end")
my_list = [1, 2, 3]
my_list.append(4)
print(f"After append(4): {my_list}")  # [1, 2, 3, 4]
# Append any object: list, tuple, dict, etc.
my_list.append([5, 6])
print(f"Append list [5,6]: {my_list}")  # [1, 2, 3, 4, [5, 6]]

# ---------- 2. clear() ----------
# Removes all elements from the list.
# Returns: None.
# Time complexity: O(n) because it removes each reference.
print("\n" + "=" * 50)
print("2. clear() - Remove all elements")
my_list = [1, 2, 3, 4]
my_list.clear()
print(f"After clear(): {my_list}")  # []

# ---------- 3. copy() ----------
# Returns a shallow copy of the list.
# Returns: New list object.
# Time complexity: O(n).
print("\n" + "=" * 50)
print("3. copy() - Shallow copy")
original = [1, 2, [3, 4]]
copied = original.copy()
print(f"Original: {original}")
print(f"Copied:   {copied}")
# Modifying the copy does NOT affect original (for top-level elements)
copied[0] = 99
print(f"After modifying copy[0]=99 -> original[0] still {original[0]}")
# BUT for nested mutable objects (like inner list), changes reflect in both
copied[2][0] = 999  # changes the inner list
print(f"After modifying copied's inner list: original = {original}")  # inner changed!

# ---------- 4. count(x) ----------
# Returns the number of occurrences of x in the list.
# Returns: Integer count.
# Time complexity: O(n).
print("\n" + "=" * 50)
print("4. count(x) - Count occurrences")
my_list = [1, 2, 2, 3, 2, 4, 2]
cnt = my_list.count(2)
print(f"List: {my_list}")
print(f"Count of 2: {cnt}")  # 4
cnt_99 = my_list.count(99)
print(f"Count of 99 (non-existent): {cnt_99}")  # 0

# ---------- 5. extend(iterable) ----------
# Appends all elements from the iterable (list, tuple, string, etc.) to the end.
# Returns: None.
# Time complexity: O(k) where k = length of iterable.
print("\n" + "=" * 50)
print("5. extend(iterable) - Add multiple elements")
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])  # extend with list
print(f"Extend with [4,5,6]: {my_list}")  # [1,2,3,4,5,6]
my_list.extend((7, 8))     # extend with tuple
print(f"Extend with (7,8): {my_list}")    # [1,2,3,4,5,6,7,8]
my_list.extend("abc")      # extend with string (each char becomes element)
print(f"Extend with 'abc': {my_list}")    # [1,2,3,4,5,6,7,8,'a','b','c']
# Note: extend() is different from append() – append adds the iterable as one object.

# ---------- 6. index(x[, start[, end]]) ----------
# Returns the first index of x (search from start to end-1).
# Raises ValueError if x not found.
# Returns: Integer index.
# Time complexity: O(n) worst-case.
print("\n" + "=" * 50)
print("6. index(x[, start[, end]]) - Find first occurrence")
my_list = [10, 20, 30, 20, 40]
idx = my_list.index(20)          # finds first 20
print(f"First 20 at index: {idx}")   # 1
idx = my_list.index(20, 2)       # search from index 2 onward
print(f"20 after index 2 at: {idx}") # 3 (second occurrence)
# idx = my_list.index(20, 2, 4)  # search indices 2 to 3 only -> would raise ValueError
# To avoid error, check with 'in' first: if 99 in my_list: my_list.index(99)

# ---------- 7. insert(i, x) ----------
# Inserts element x at index i (shifts elements to the right).
# If i is negative, it counts from the end (like -1 is last position, but inserts before that element).
# If i >= len(list), inserts at end. If i <= -len(list)-1, inserts at beginning.
# Returns: None.
# Time complexity: O(n) because elements after i are shifted.
print("\n" + "=" * 50)
print("7. insert(i, x) - Insert at position")
my_list = [1, 2, 3, 4]
my_list.insert(2, 99)            # insert 99 at index 2 (between 2 and 3)
print(f"Insert 99 at index 2: {my_list}")  # [1, 2, 99, 3, 4]
my_list.insert(-1, 777)          # insert 777 before last element (index -1)
print(f"Insert 777 before last: {my_list}") # [1,2,99,3,777,4]
my_list.insert(100, 888)         # index > length -> inserts at end
print(f"Insert at huge index: {my_list}")   # [... ,888]
my_list.insert(-100, 111)        # very negative -> inserts at beginning
print(f"Insert at very negative: {my_list}") # [111, ...]

# ---------- 8. pop([i]) ----------
# Removes and returns the element at index i. If i not given, removes and returns last element.
# Raises IndexError if list empty or i out of range.
# Returns: The popped element.
# Time complexity: O(1) for last element, O(n) for arbitrary index (shifting).
print("\n" + "=" * 50)
print("8. pop([i]) - Remove and return element")
my_list = [10, 20, 30, 40, 50]
last = my_list.pop()             # pop last
print(f"Popped last: {last}, list now: {my_list}")  # popped 50, list [10,20,30,40]
second = my_list.pop(1)          # pop element at index 1 (20)
print(f"Popped index 1: {second}, list now: {my_list}") # [10,30,40]
# Trying pop() on empty list: uncomment to see IndexError
# empty = []; empty.pop()

# ---------- 9. remove(x) ----------
# Removes the first occurrence of x from the list.
# Raises ValueError if x not found.
# Returns: None.
# Time complexity: O(n) (search + shift).
print("\n" + "=" * 50)
print("9. remove(x) - Remove first occurrence")
my_list = [1, 2, 3, 2, 4]
my_list.remove(2)                # removes first 2
print(f"After remove(2): {my_list}")  # [1,3,2,4]
# Attempt to remove non-existent: my_list.remove(99) -> ValueError
# Safe way: if 99 in my_list: my_list.remove(99)

# ---------- 10. reverse() ----------
# Reverses the list in place (does not create a new list).
# Returns: None.
# Time complexity: O(n).
print("\n" + "=" * 50)
print("10. reverse() - Reverse in place")
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(f"After reverse(): {my_list}")  # [5,4,3,2,1]
# To get a reversed copy without modifying original: new_list = my_list[::-1]

# ---------- 11. sort(key=None, reverse=False) ----------
# Sorts the list in place (ascending by default).
# Parameters:
#   key: function that extracts a comparison key from each element (e.g., key=len, key=str.lower)
#   reverse: if True, sorts descending.
# Returns: None.
# Time complexity: O(n log n) (Timsort).
print("\n" + "=" * 50)
print("11. sort(key=None, reverse=False) - Sort in place")
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(f"Sort ascending: {my_list}")      # [1,1,3,4,5,9]
my_list.sort(reverse=True)
print(f"Sort descending: {my_list}")     # [9,5,4,3,1,1]

# Sorting with key function
words = ["apple", "Banana", "cherry", "date"]
words.sort(key=str.lower)                # case-insensitive sort
print(f"Sort case-insensitive: {words}") # ['apple','Banana','cherry','date']
words.sort(key=len)                      # sort by string length
print(f"Sort by length: {words}")        # ['date','apple','Banana','cherry']

# Sorting a list of tuples by second element
pairs = [(1, 'b'), (2, 'a'), (3, 'c')]
pairs.sort(key=lambda x: x[1])           # sort by second element
print(f"Sort by second element: {pairs}") # [(2,'a'),(1,'b'),(3,'c')]

# =============================================================================
# ADDITIONAL NOTES:
# - Lists also support operators like + (concatenation) and * (replication), but these are not methods.
# - Methods like .append(), .extend(), .insert(), .remove(), .pop(), .reverse(), .sort() modify in place.
# - .copy() creates a shallow copy; for deep copy use copy.deepcopy() from module copy.
# - For sorting without modifying original: use sorted(list, ...)
# - For reversing without modifying: use reversed(list) or slicing list[::-1]
# =============================================================================