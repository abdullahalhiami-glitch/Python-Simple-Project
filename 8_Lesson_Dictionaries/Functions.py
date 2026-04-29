# def add_contact(contacts, name, phone):
#     gicontacts[name] = phone
#     print(f"Contact {name} added successfully.")
  
def hello(name):
    print(f"Hello {name.capitalize()}!")

# hello("Abdullah")# this is a function call
# hello("Abdullah")
# hello("Abdullah")
# hello("Abdullah")
# hello("Abdullah")
# hello("Abdullah")
# hello("Abdullah")

# def hello():
#     print("Hello World!")

# def CheckVowelsInName():
#     name = input("Enter a name: ").lower()
#     vowels = ('a', 'e', 'i', 'o', 'u')
#     count = 0
#     for char in name:
#         if char in vowels:
#             count += 1
#     hello(name)
#     print(f"The name {name} has {count} vowels.")
# CheckVowelsInName()

def CheckVowelsInName():
    name = input("Enter a name: ").lower()
    vowels = ('a', 'e', 'i', 'o', 'u')
    count = 0
    for char in name:
        if char in vowels:
            count += 1
        else:
            print(f"The name {name} does not have any vowels.")
            break
    hello(name)
    print(f"Your name {name} has {count} vowels.")
CheckVowelsInName()

def say_hello(name):
    print(f"Hello {name}!")


def sayHello(name,gender="male"):
    if gender == "male":
        print(f"Hello Mr. {name}!")
    elif gender == "female":
        print(f"Hello Ms. {name}!")
    else:
        print(f"Hello {name}!")