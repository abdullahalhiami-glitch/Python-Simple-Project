programmingLanguages = ["Python", "Java", "C++", "JavaScript", "Ruby"]
# Print the list of programming languages

print("Programming Languages:", programmingLanguages)   

programmingLanguages.append("Go")  # Adding a new programming 
programmingLanguages[3] = "TypeScript"  # Updating JavaScript to TypeScript
programmingLanguages.remove("C++")  # Removing C++ from the list

programmingLanguages[2] = "C#"  # Updating Java to C#
programmingLanguages.insert(1, "Swift")  # Inserting Swift at index 1
print("Programming Languages:", programmingLanguages)   

programmingLanguages[::3] = ["Kotlin", "Rust"]  # Replacing every third element with Kotlin and Rust
print("Programming Languages:", programmingLanguages)

programmingLanguages[1:4] = ["PHP", "Scala"]  # Replacing elements from index 1 to 3 with PHP and Scala
print("Programming Languages:", programmingLanguages)   

programmingLanguages[0:2] = []  # Removing the first two elements
print("Programming Languages:", programmingLanguages)   
programmingLanguages.append("Dart")  # Adding Dart to the end of the list
print("Programming Languages:", programmingLanguages)

programmingLanguage = ["Python", "Java", "C++", "JavaScript", "Ruby"]

pro = programmingLanguages + programmingLanguage  # Concatenating the two lists
print("Concatenated List:", pro)

pro += ["Swift", "Go"]  # Adding more languages to the concatenated list
print("Updated Concatenated List:", pro)
print("Updated Concatenated List:", pro*2)  # Repeating the concatenated list twice
print(pro[2:])
print(pro[:5])#indexing
print(pro[::3])#three steps slice
#delete item from list
del pro[1:3]
del pro[:5]

for lang in programmingLanguages:
    print(lang)

for lang in range(0,len(programmingLanguages)):
    print(programmingLanguages[lang])

print("While printing: ")
i = 0

while i <= len(programmingLanguages)-1:
    print(programmingLanguages[i])
    i += 1


print("2d matrix: ")
studentInfo = [
    ['ID', 'Name', 'Age', 'GPA'],
    ['1', 'Abdullah', 32, 90.4],
    ['2', 'Ali', 22, 78.82],
    ['3', 'Mohammed', 18, 89.2]
]

studentInfo.append(['4', 'Malek', 15, 89.2 ])
studentInfo.insert(2,['4', 'Malek', 15, 89.2 ])
studentInfo.extend(['4', 'Malek', 15, 89.2 ])
studentInfo.remove('Malek')
studentInfo.pop(2)
studentInfo.reverse()
studentInfo.copy()
studentInfo.count()
studentInfo.clear()


for i in range(0,len(studentInfo)):
    print(studentInfo[i])
# for i in range(0,len(studentInfo)):
#     print(studentInfo[i][1:3])