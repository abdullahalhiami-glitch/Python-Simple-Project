#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
COMPREHENSIVE GUIDE TO ALL PYTHON DICTIONARY FUNCTIONS (METHODS)
================================================================
This script demonstrates every built-in method available for dictionary objects in Python.
Each method is explained in detail with its own example, including parameters, return values,
side effects, and edge cases.

Dictionary basics:
- Dictionaries are unordered (but insertion ordered since Python 3.7), mutable, key-value stores.
- Keys must be hashable (immutable types like strings, numbers, tuples).
- Values can be any type.
- Methods shown: clear, copy, fromkeys, get, items, keys, values, pop, popitem, setdefault, update.
- Also includes built-in functions len(), 'in' operator, and dict() constructor for context.
"""

print("=== PYTHON DICTIONARY FUNCTIONS (METHODS) DEMONSTRATION ===\n")

# ----------------------------------------------------------------------
# 1. dict.clear()
# ----------------------------------------------------------------------
print("1. clear() - Removes all items from the dictionary.")
print("-" * 50)
# Create a sample dictionary
sample_dict = {"a": 1, "b": 2, "c": 3}
print(f"Original dict: {sample_dict}")
# clear() removes all key-value pairs, mutating the dictionary in place
sample_dict.clear()
print(f"After clear(): {sample_dict}")  # Output: {}
# Note: clear() returns None. It modifies the original dict; no new dict is created.
print()

# ----------------------------------------------------------------------
# 2. dict.copy()
# ----------------------------------------------------------------------
print("2. copy() - Returns a shallow copy of the dictionary.")
print("-" * 50)
original = {"x": [1, 2], "y": 3}
print(f"Original: {original}")
# copy() creates a new dictionary with the same key-value references (shallow)
copied = original.copy()
print(f"Shallow copy: {copied}")
# Modifying the copied dict at top level does not affect original
copied["y"] = 99
print(f"After modifying copied['y']=99 -> copied: {copied}, original: {original}")
# But modifying a mutable value inside the copy affects original (shallow copy behavior)
copied["x"].append(99)
print(f"After appending to copied['x'] -> copied: {copied}, original: {original}")
# To avoid this, use deepcopy from copy module if needed.
print()

# ----------------------------------------------------------------------
# 3. dict.fromkeys(iterable, [value])   (class method)
# ----------------------------------------------------------------------
print("3. fromkeys(iterable, value=None) - Class method to create new dict from keys.")
print("-" * 50)
# Creates a new dictionary with keys from the iterable and all values set to the given value.
keys = ["name", "age", "city"]
# Using default value None
d1 = dict.fromkeys(keys)
print(f"dict.fromkeys({keys}) -> {d1}")  # Values are None
# With custom default value
d2 = dict.fromkeys(keys, "unknown")
print(f"dict.fromkeys({keys}, 'unknown') -> {d2}")
# Works with any iterable (tuple, set, range)
d3 = dict.fromkeys(range(3), 0)
print(f"dict.fromkeys(range(3), 0) -> {d3}")
# Important: The value is shared for all keys; if mutable, changes affect all keys.
d4 = dict.fromkeys(["a", "b"], [])
d4["a"].append(1)
print(f"Shared mutable value: dict.fromkeys(['a','b'], []) -> after appending to 'a' -> {d4}")
print()

# ----------------------------------------------------------------------
# 4. dict.get(key, [default])
# ----------------------------------------------------------------------
print("4. get(key, default=None) - Returns value for key if exists, else default.")
print("-" * 50)
inventory = {"apples": 5, "bananas": 3}
print(f"Dict: {inventory}")
# Normal access: inventory["oranges"] would raise KeyError, but get() avoids that
oranges = inventory.get("oranges")
print(f"get('oranges') -> {oranges}")  # None (default not provided => None)
oranges_default = inventory.get("oranges", 0)
print(f"get('oranges', 0) -> {oranges_default}")  # 0
existing = inventory.get("apples", 0)
print(f"get('apples', 0) -> {existing}")  # 5 (key exists, default ignored)
# get() does NOT modify the dictionary.
print(f"Dict unchanged: {inventory}")
print()

# ----------------------------------------------------------------------
# 5. dict.items()
# ----------------------------------------------------------------------
print("5. items() - Returns a view of dictionary's (key, value) pairs.")
print("-" * 50)
person = {"name": "Alice", "job": "Engineer"}
print(f"Dict: {person}")
# items() returns a dict_items view object (dynamic, reflects changes)
items_view = person.items()
print(f"items_view = person.items() -> {items_view}")
# Convert to list or iterate
print("Iterating over items:")
for k, v in items_view:
    print(f"  {k} -> {v}")
# The view reflects dictionary changes dynamically
person["age"] = 30
print(f"After adding 'age': items_view = {items_view}")
# Useful for membership test: ('name','Alice') in items_view -> True
print(f"('name','Alice') in items_view? {('name','Alice') in items_view}")
print()

# ----------------------------------------------------------------------
# 6. dict.keys()
# ----------------------------------------------------------------------
print("6. keys() - Returns a view of dictionary's keys.")
print("-" * 50)
country_capitals = {"France": "Paris", "Japan": "Tokyo"}
print(f"Dict: {country_capitals}")
keys_view = country_capitals.keys()
print(f"keys_view = {keys_view}")  # dict_keys(['France', 'Japan'])
# Supports set-like operations (union, intersection, etc.) because keys are unique and hashable
print(f"Set of keys: {set(keys_view)}")
# Dynamic: adding new key updates the view
country_capitals["Brazil"] = "Brasilia"
print(f"After adding Brazil: keys_view = {keys_view}")
# Membership test is efficient
print(f"'Japan' in keys_view? {'Japan' in keys_view}")
print()

# ----------------------------------------------------------------------
# 7. dict.values()
# ----------------------------------------------------------------------
print("7. values() - Returns a view of dictionary's values.")
print("-" * 50)
scores = {"math": 90, "science": 85}
print(f"Dict: {scores}")
values_view = scores.values()
print(f"values_view = {values_view}")  # dict_values([90, 85])
# Note: values may contain duplicates, so view does not support set operations
# Dynamic: modifying dict updates the view
scores["art"] = 95
print(f"After adding art: values_view = {values_view}")
# Useful for iteration or aggregation
print(f"Average score: {sum(scores.values()) / len(scores)}")
print()

# ----------------------------------------------------------------------
# 8. dict.pop(key, [default])
# ----------------------------------------------------------------------
print("8. pop(key, default) - Removes specified key and returns its value.")
print("-" * 50)
cart = {"apple": 2, "banana": 3, "orange": 1}
print(f"Original dict: {cart}")
# pop removes the key and returns the value
removed_value = cart.pop("banana")
print(f"pop('banana') -> {removed_value}")
print(f"Dict after pop: {cart}")
# If key not found and default provided, returns default (no error)
default_pop = cart.pop("grape", "not found")
print(f"pop('grape', 'not found') -> {default_pop}")
# If key not found and no default, raises KeyError
try:
    cart.pop("nonexistent")
except KeyError as e:
    print(f"pop('nonexistent') raises KeyError: {e}")
print()

# ----------------------------------------------------------------------
# 9. dict.popitem()
# ----------------------------------------------------------------------
print("9. popitem() - Removes and returns a (key, value) pair (LIFO order).")
print("-" * 50)
# Since Python 3.7, dictionaries maintain insertion order, and popitem() removes the last inserted item (LIFO).
ordered_dict = {"first": 1, "second": 2, "third": 3}
print(f"Original dict: {ordered_dict}")
# popitem removes the last inserted item
item = ordered_dict.popitem()
print(f"popitem() returns: {item}")
print(f"Dict after popitem: {ordered_dict}")
item2 = ordered_dict.popitem()
print(f"Second popitem() returns: {item2}")
print(f"Dict after second popitem: {ordered_dict}")
# On empty dict, popitem() raises KeyError
try:
    {}.popitem()
except KeyError as e:
    print(f"popitem() on empty dict raises KeyError: {e}")
print()

# ----------------------------------------------------------------------
# 10. dict.setdefault(key, [default])
# ----------------------------------------------------------------------
print("10. setdefault(key, default=None) - Returns value if key exists, else inserts key with default.")
print("-" * 50)
config = {"host": "localhost", "port": 8080}
print(f"Original dict: {config}")
# Existing key: returns its value and does nothing else
port_val = config.setdefault("port", 9999)
print(f"setdefault('port', 9999) -> {port_val} (existing value)")
print(f"Dict unchanged: {config}")
# Non-existing key: inserts key with default value and returns that default
timeout_val = config.setdefault("timeout", 60)
print(f"setdefault('timeout', 60) -> {timeout_val} (inserted and returned)")
print(f"Dict after setdefault: {config}")
# If default not provided, inserts with None
new_key_val = config.setdefault("protocol")
print(f"setdefault('protocol') -> {new_key_val} (inserts None)")
print(f"Dict now: {config}")
# Very useful for counting or grouping patterns (e.g., building lists in dict)
word_counts = {}
for word in ["apple", "banana", "apple"]:
    word_counts.setdefault(word, 0)
    word_counts[word] += 1
print(f"Word counts using setdefault: {word_counts}")
print()

# ----------------------------------------------------------------------
# 11. dict.update([other])
# ----------------------------------------------------------------------
print("11. update([other]) - Updates dictionary with key-value pairs from other.")
print("-" * 50)
# update can accept another dict, an iterable of pairs, or keyword arguments.
d = {"a": 1, "b": 2}
print(f"Start dict: {d}")
# Update with another dict
d.update({"b": 3, "c": 4})
print(f"After update with dict: {d}")  # {'a':1, 'b':3, 'c':4}
# Update with iterable of (key,value) pairs
d.update([("d", 5), ("e", 6)])
print(f"After update with list of tuples: {d}")
# Update with keyword arguments
d.update(f=7, g=8)
print(f"After update with kwargs: {d}")
# Existing keys are overwritten, new keys added. Returns None.
# Additional: update can also accept a mapping or any object with keys() method.
print()

# ----------------------------------------------------------------------
# Additional useful built-in functions for dictionaries
# ----------------------------------------------------------------------
print("=== ADDITIONAL BUILT-IN FUNCTIONS & OPERATORS ===")
print("-" * 50)

# len(dict) - returns number of items
print("len() - Number of key-value pairs:")
d_len = {"x": 10, "y": 20, "z": 30}
print(f"len({d_len}) = {len(d_len)}")

# 'in' operator - check if key exists (uses __contains__)
print("\n'in' operator - Check key presence:")
print(f"'x' in {d_len}? {'x' in d_len}")
print(f"'w' in {d_len}? {'w' in d_len}")

# dict() constructor - creates dict from various inputs
print("\ndict() constructor - Create dictionaries:")
# From keyword args
d1 = dict(red=1, green=2, blue=3)
print(f"dict(red=1, green=2, blue=3) -> {d1}")
# From iterable of pairs
d2 = dict([("one", 1), ("two", 2)])
print(f"dict([('one',1), ('two',2)]) -> {d2}")
# From mapping (another dict)
d3 = dict(d1)
print(f"dict(d1) -> {d3}")

# Dictionary comprehension (not a method but essential)
print("\nDictionary comprehension:")
squares = {x: x**2 for x in range(5)}
print(f"{{x: x**2 for x in range(5)}} -> {squares}")

# ----------------------------------------------------------------------
# Summary of all methods with their complexity and behavior
# ----------------------------------------------------------------------
print("\n=== SUMMARY OF DICTIONARY METHODS ===")
summary = """
Method          | Description                                      | Returns          | Modifies?
----------------|--------------------------------------------------|------------------|-----------
clear()         | Removes all items                               | None             | Yes
copy()          | Shallow copy                                    | New dict         | No
fromkeys()      | Creates new dict from keys                      | New dict         | No (classmethod)
get()           | Returns value or default                        | Value or default | No
items()         | Returns view of (key, value) pairs              | dict_items view  | No
keys()          | Returns view of keys                            | dict_keys view   | No
values()        | Returns view of values                          | dict_values view | No
pop()           | Removes key and returns value                   | Removed value    | Yes
popitem()       | Removes and returns last inserted pair          | (key, value)     | Yes
setdefault()    | Inserts/returns value for key                   | Value            | Yes (if missing)
update()        | Merges another mapping into dict                | None             | Yes
"""
print(summary)

print("End of demonstration.")