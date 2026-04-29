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