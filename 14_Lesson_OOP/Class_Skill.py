'''
Docstring for 14_Lesson_OOP.Class_Skill
'''

# class Skill:
#     def __init__(self):
#         self.Skills = ['Html', 'Css', 'C++']
#     # def __str__(self):
#     #     return f'Skills: {self.Skills}'
#     def __len__(self):
#         return len(self.Skills)

class Skill:
    def __init__(self):
        self.Skills = ['Html', 'Css', 'C++']
    #without this function the object will only print the location of the memory that it has, but with it it will show the value of the object
    # def __str__(self):
    #     return f'Skills: {self.Skills}'
    def __str__(self):
        return f'Skills: {self.Skills}'
    def __len__(self):
        return len(self.Skills)
    

profile = Skill()

print(profile)
profile.Skills.append("Python")
print(profile)
print(len(profile))