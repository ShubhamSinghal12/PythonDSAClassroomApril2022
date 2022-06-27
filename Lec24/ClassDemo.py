class Person:

    country = "USA"

    def __init__(self,name="",age=0):
        self.name = name
        self.age = age
    
    def saysHi(self):
        # print(self)
        print("Says Hi! My name is " + self.name+" and my age is : "+str(self.age))

Person.country = "Russia"
p = Person("Rahul",20)
p.country = "India"
print(p.country)
# p.name = "Rahul"
# p.name = "Ram"
# print(p)
# p.saysHi()
print(Person.country)

p2 = Person("Divyanshu",25)
print(p2.country)
# p2.name = "Divyanshu"
# p2.saysHi()
# print(p2.age)

def test1(p1,p2):
    t = p1
    p1 = p2
    p2 = t

def test2(s1,s2):
    s2 = Person("",10)
    t = s1.age
    s1.age = s2.age
    s2.age = t

    s1 = Person("",10)
    t = s1.name
    s1.name = s2.name
    s2.name = t


def test3(s1,age,name,myage,myname):
    s1.age = 0
    s1.name = ""
    age = 0
    name = ""
    myage = 0
    myname = ""

# myage = 100
# myname = "Sh"
# test3(p,p2.age,p2.name,myage,myname)
# print(p.name+" "+str(p.age))
# print(p2.name+" "+str(p2.age))
# print(myname+" "+str(myage))


# print(p.name+" "+str(p.age))
# print(p2.name+" "+str(p2.age))

# test2(p,p2)

# print(p.name+" "+str(p.age))
# print(p2.name+" "+str(p2.age))

