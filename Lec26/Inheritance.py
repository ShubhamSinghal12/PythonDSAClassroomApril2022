class Parent:
    def __init__(self,name="",age=0):
        self.__name = name
        self._age = age
    
    def intro(self):
        print("Hi My name is "+self.__name+" and my age is: "+str(self._age))

class Child(Parent):
    def __init__(self,name = "",age = 0):
        self.rollNo = 100
        # super().__init__(name,age)
        Parent.__init__(self,name,age)
    def wave(self):
        print(self._Parent__name)
        print(self._age)

if __name__ == "__main__":
    c = Child("Ram",20)
    # print(dir(c))
    # print(c._Parent__name)
    # print(c.__name)
    # print(c._age)
    c.intro()
    # c.wave()
    # print(help(c))
