class MyStack:
    
    def __init__(self,size = 10):
        self.l = [0 for i in range(size)]
        self.top = -1
    
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == len(self.l)-1
    

    def size(self):
        return self.top+1
    
    def push(self,ele):
        if self.isFull():
            raise Exception("Stack Overflow")
        else:
            self.top += 1
            self.l[self.top] = ele
    def pop(self):
        if self.isEmpty():
            raise Exception("Stack UnderFlow")
        else:
            v = self.l[self.top]
            self.top -= 1
            return v
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack UnderFlow")
        else:
            return self.l[self.top]
    
    def display(self):
        
        for i in range(self.top,-1,-1):
            print(self.l[i],end= " ")
        print()

st = MyStack(5)
for i in range(1,6):
    st.push(i)
    st.display()

print(st.pop())
print(st.pop())
print(st.peek())
st.display()
st.push(10)
st.push(20)
st.display()