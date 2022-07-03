class X:
    def __init__(self):
        print("Entering X")
        # super().__init__()
        print("Exiting X")
    
    def hello(self):
        print("X says Hello")
class A(X):
    def __init__(self):
        print("Entering A")
        super().__init__()
        print("Exiting A")
    
    def hello(self):
        print("A says Hello")

class B(X):
    def __init__(self):
        print("Entering B")
        super().__init__()
        print("Exiting B")
    
    def hello(self,a=10,b=0):
        print("B says Hello")

class C(A,B):
    def __init__(self):
        print("Entering C")
        # B.__init__(self)
        # A.__init__(self)
        super().__init__()
        # super(A,self).__init__()
        print("Exiting C")
    
    def hello(self):
        print("C says Hello")


c = C()
c.hello()
print(help(c))