class A:
    def __init__(self,val=10,y = 0):
        self.x = val
        self.y = y
    
    def __add__(self,ob):
        return A(self.x + ob.x, self.y+ob.y)
    
    def __str__(self):
        return "x = "+str(self.x)+" , y = "+str(self.y)
    
a = A(10,-10)
b = A(20,-20)
c = a+b
# print(a)
print(c,type(c))