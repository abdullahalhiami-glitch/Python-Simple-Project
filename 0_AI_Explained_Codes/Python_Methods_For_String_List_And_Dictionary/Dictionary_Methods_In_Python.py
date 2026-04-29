"""
================================================================================
   COMPREHENSIVE DEMONSTRATION OF ALL PYTHON DICTIONARY METHODS & FUNCTIONS
================================================================================
This script covers:
  - All instance methods of the `dict` class:
      clear, copy, fromkeys, get, items, keys, pop, popitem, setdefault, update, values
  - Built-in functions/statements that operate on dictionaries:
      len(), in / not in, del, dict() constructor
  - Dictionary indexing and assignment

Every section is self-contained and heavily commented.
Run the script to see the output produced by each operation.
"""

# ----------------------------------------------------------------------
# 1. CREATING A DICTIONARY (constructor, literals, fromkeys)
# ----------------------------------------------------------------------

# Using a literal
d = {'apple': 5, 'banana': 2, 'cherry': 8}
print("Original dictionary:", d)
# Output: {'apple': 5, 'banana': 2, 'cherry': 8}

# Using the dict() constructor with keyword arguments
d2 = dict(apple=5, banana=2, cherry=8)
print("From dict(**kwargs):", d2)   # same as above

# Using dict() with an iterable of key-value pairs
d3 = dict([('apple', 5), ('banana', 2), ('cherry', 8)])
print("From list of tuples:", d3)

# Using dict() with a mapping (another dictionary)
d4 = dict(d)
print("From another dict:", d4)


########################################################################
#        INSTANCE METHODS OF THE DICT CLASS
########################################################################

# ----------------------------------------------------------------------
# 2. dict.clear() – Remove all items from the dictionary.
# ----------------------------------------------------------------------
print("\n--- clear() ---")
d_clear = {'x': 10, 'y': 20, 'z': 30}
print("Before clear:", d_clear)     # {'x': 10, 'y': 20, 'z': 30}
d_clear.clear()                     # Removes everything, modifies in place
print("After clear:", d_clear)      # {}
# Note: clear() returns None.


# ----------------------------------------------------------------------
# 3. dict.copy() – Return a shallow copy of the dictionary.
# ----------------------------------------------------------------------
print("\n--- copy() ---")
original = {'a': [1, 2], 'b': 3}
shallow = original.copy()           # new dict, same objects inside
print("Original:", original)
print("Shallow copy:", shallow)
# Prove it's a different container, but nested mutable objects are shared
shallow['a'].append(99)
print("After modifying list inside shallow copy:")
print("Original:", original)        # original['a'] also changed -> [1, 2, 99]
print("Shallow copy:", shallow)     # same list object
# A deep copy (from copy module) would be needed to avoid this.


# ----------------------------------------------------------------------
# 4. dict.fromkeys(iterable, value=None) – CLASS METHOD.
#    Creates a new dictionary with keys from iterable and values set to value.
# ----------------------------------------------------------------------
print("\n--- fromkeys() ---")
keys = ['name', 'age', 'city']
# Default value is None
d_default = dict.fromkeys(keys)
print("Default None:", d_default)   # {'name': None, 'age': None, 'city': None}

# With a specific value
d_value = dict.fromkeys(keys, 0)
print("With value 0:", d_value)     # {'name': 0, 'age': 0, 'city': 0}

# IMPORTANT: If value is mutable, all keys point to the *same* object!
d_mutable = dict.fromkeys(['a', 'b'], [])
print("Before mutation:", d_mutable) # {'a': [], 'b': []}
d_mutable['a'].append(1)
print("After d_mutable['a'].append(1):", d_mutable)  # {'a': [1], 'b': [1]}  (same list)


# ----------------------------------------------------------------------
# 5. dict.get(key, default=None) – Return the value for key if key exists,
#    else return default (None by default). Does NOT raise KeyError.
# ----------------------------------------------------------------------
print("\n--- get() ---")
d_get = {'apple': 5, 'banana': 2}
print("d_get:", d_get)
# Existing key
print("get('apple'):", d_get.get('apple'))          # 5
# Non-existing key without default -> None
print("get('orange'):", d_get.get('orange'))        # None
# Non-existing key with custom default
print("get('orange', 0):", d_get.get('orange', 0))  # 0
# Dictionary remains unchanged
print("After get calls:", d_get)


# ----------------------------------------------------------------------
# 6. dict.items() – Return a dynamic view of the dictionary’s (key, value) pairs.
# ----------------------------------------------------------------------
print("\n--- items() ---")
d_items = {'x': 1, 'y': 2}
items_view = d_items.items()
print("Items view:", items_view)  # dict_items([('x', 1), ('y', 2)])
# Views reflect changes in the dictionary
d_items['z'] = 3
print("After adding 'z':", items_view)  # now includes ('z', 3)
# Typical usage: iteration
for k, v in d_items.items():
    print(f"  {k} -> {v}")


# ----------------------------------------------------------------------
# 7. dict.keys() – Return a dynamic view of the dictionary’s keys.
# ----------------------------------------------------------------------
print("\n--- keys() ---")
d_keys = {'a': 1, 'b': 2}
keys_view = d_keys.keys()
print("Keys view:", keys_view)     # dict_keys(['a', 'b'])
d_keys['c'] = 3
print("After adding 'c':", keys_view)  # dict_keys(['a', 'b', 'c'])
# Membership test works on views
print("'a' in keys_view:", 'a' in keys_view)  # True


# ----------------------------------------------------------------------
# 8. dict.values() – Return a dynamic view of the dictionary’s values.
# ----------------------------------------------------------------------
print("\n--- values() ---")
d_vals = {'a': 1, 'b': 2, 'c': 1}
vals_view = d_vals.values()
print("Values view:", vals_view)   # dict_values([1, 2, 1])
d_vals['a'] = 100
print("After modifying 'a':", vals_view)  # dict_values([100, 2, 1])


# ----------------------------------------------------------------------
# 9. dict.pop(key, default) – Remove the key and return its value.
#    If key is not found, return default if given, otherwise raise KeyError.
# ----------------------------------------------------------------------
print("\n--- pop() ---")
d_pop = {'x': 10, 'y': 20, 'z': 30}
# Pop an existing key
val = d_pop.pop('y')
print("Popped 'y':", val)          # 20
print("After pop:", d_pop)         # {'x': 10, 'z': 30}
# Pop with a default for a missing key
val2 = d_pop.pop('w', 'not found')
print("Popped 'w' with default:", val2)  # 'not found'
# Without default, missing key raises KeyError
# d_pop.pop('w')  # Uncommenting this would raise KeyError


# ----------------------------------------------------------------------
# 10. dict.popitem() – Remove and return the last inserted (key, value) pair
#     as a tuple. Raises KeyError if the dictionary is empty.
#     (Since Python 3.7+, dictionaries preserve insertion order.)
# ----------------------------------------------------------------------
print("\n--- popitem() ---")
d_popitem = {'first': 1, 'second': 2, 'last': 3}
print("Before popitem:", d_popitem)
item = d_popitem.popitem()
print("Popped item:", item)        # ('last', 3)  – the last inserted
print("After popitem:", d_popitem) # {'first': 1, 'second': 2}
# Repeat until empty
while d_popitem:
    print("Popping:", d_popitem.popitem())
# Now d_popitem is empty; next call would raise KeyError
# d_popitem.popitem()   # --> KeyError: 'popitem(): dictionary is empty'


# ----------------------------------------------------------------------
# 11. dict.setdefault(key, default=None) – If key is in the dictionary,
#     return its value. If not, insert key with a value of default and
#     return default. This is useful for initialising missing keys.
# ----------------------------------------------------------------------
print("\n--- setdefault() ---")
d_sd = {'a': 1, 'b': 2}
# Existing key: returns its value, no modification
print("setdefault('a', 99):", d_sd.setdefault('a', 99))  # 1
print("After:", d_sd)                                     # unchanged
# Missing key: inserts key with default and returns default
print("setdefault('c', 99):", d_sd.setdefault('c', 99))  # 99
print("After:", d_sd)                                    # {'a': 1, 'b': 2, 'c': 99}
# Without default, it inserts None
d_sd.setdefault('d')
print("After setdefault('d'):", d_sd)                    # 'd': None


# ----------------------------------------------------------------------
# 12. dict.update([other]) – Update the dictionary with key/value pairs from
#     another dictionary, an iterable of key-value pairs, or keyword arguments.
#     Existing keys are overwritten.
# ----------------------------------------------------------------------
print("\n--- update() ---")
d_up = {'one': 1, 'two': 2}
# Update with another dictionary
d_up.update({'three': 3, 'four': 4})
print("After update with dict:", d_up)   # {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# Update with an iterable of (key, value) pairs
d_up.update([('five', 5), ('two', 22)])  # 'two' is overwritten
print("After update with list of tuples:", d_up)  # 'two' becomes 22
# Update with keyword arguments
d_up.update(six=6, seven=7, one=11)
print("After update with **kwargs:", d_up)        # 'one' becomes 11, etc.
# update() modifies the dictionary in place and returns None


########################################################################
#     BUILT-IN FUNCTIONS / OPERATORS THAT WORK WITH DICTIONARIES
########################################################################

# ----------------------------------------------------------------------
# 13. len(dictionary) – Return the number of items (key-value pairs).
# ----------------------------------------------------------------------
print("\n--- len() ---")
d_len = {'a': 1, 'b': 2, 'c': 3}
print("Length:", len(d_len))           # 3
d_len.clear()
print("Length after clear:", len(d_len))  # 0


# ----------------------------------------------------------------------
# 14. in / not in – Membership tests on keys (NOT values).
# ----------------------------------------------------------------------
print("\n--- in / not in ---")
d_mem = {'apple': 1, 'banana': 2}
print("'apple' in d_mem:", 'apple' in d_mem)    # True
print("'orange' in d_mem:", 'orange' in d_mem)  # False
print("'banana' not in d_mem:", 'banana' not in d_mem) # False
# Note: membership checks keys only, never values directly.
# For values use: 2 in d_mem.values()


# ----------------------------------------------------------------------
# 15. del statement – Delete a specific key. Raises KeyError if missing.
# ----------------------------------------------------------------------
print("\n--- del ---")
d_del = {'x': 10, 'y': 20, 'z': 30}
print("Before del:", d_del)
del d_del['y']
print("After del 'y':", d_del)         # {'x': 10, 'z': 30}
# Attempting to delete a non-existent key raises KeyError:
# del d_del['missing']   # KeyError: 'missing'


# ----------------------------------------------------------------------
# 16. Dictionary indexing: d[key] – Get value, or raise KeyError if missing.
# ----------------------------------------------------------------------
print("\n--- d[key] (get item) ---")
d_index = {'a': 100, 'b': 200}
print("d_index['a']:", d_index['a'])   # 100
# print(d_index['c'])                  # would raise KeyError


# ----------------------------------------------------------------------
# 17. Assignment d[key] = value – Set/update a key-value pair.
# ----------------------------------------------------------------------
print("\n--- d[key] = value (set item) ---")
d_assign = {}
d_assign['new'] = 'hello'
d_assign['a'] = 1
print("After assignments:", d_assign)  # {'new': 'hello', 'a': 1}
d_assign['a'] = 999                    # overwrite
print("After overwrite:", d_assign)    # {'new': 'hello', 'a': 999}


# ----------------------------------------------------------------------
# 18. (Bonus) sorted(dict) – Returns a sorted list of the dictionary’s keys.
# ----------------------------------------------------------------------
print("\n--- sorted() ---")
d_sort = {'banana': 2, 'apple': 5, 'cherry': 8}
sorted_keys = sorted(d_sort)
print("Sorted keys:", sorted_keys)     # ['apple', 'banana', 'cherry']