class Child:
    def __init__(self):
        self.__age = 0
    def set_age(self,age):
        if age < 18 and age > 0 and age < 100:
            self.__age = age
            print("Child age set successfully")
        else:
            print("Invaid Age")
    def get_age(self):
        return self.__age
    


Child1 = Child()
Child1.set_age(17)
Child2 = Child()
Child2.set_age(19)