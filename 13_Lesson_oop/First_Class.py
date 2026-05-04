class Human:
    def __init__(self,firstName,lastName,age):
        self.f = firstName
        self.l = lastName
        self.a = age
        print("Human")
    def printName(self):
        print("Hello, person")
    def printInfo(self):
        print(f'you name is {self.f} {self.l} and your age is {self.a}')

human = Human("Abdullah", "Al-Hiami",23)
human2 = Human("Mohammed", "Samlan", 56)
human3 = Human("Ahmed","Al-Hiami",21)

human.printName()
human.printInfo()
human2.printInfo()
human3.printInfo()
human2.printName()