from DynamicQueue import DynamicQueue

class StackUsingQueue:
    
    def __init__(self,size = 10):
        self.qt = DynamicQueue()
    
    def isEmpty(self):
        return self.qt.isEmpty() 

    def size(self):
        return self.qt.Qsize()
    
    def push(self,ele):
        self.qt.enqueue(ele)

    def pop(self):
        # nqt = DynamicQueue()
        i = self.qt.Qsize()
        while i > 1:
            self.qt.enqueue(self.qt.dequeue())
            i -= 1
        
        t = self.qt.dequeue()
        # self.qt = nqt
        return t
    
    def peek(self):
         # nqt = DynamicQueue()
        i = self.qt.Qsize()
        while i > 1:
            self.qt.enqueue(self.qt.dequeue())
            i -= 1
        
        t = self.qt.dequeue()
        self.qt.enqueue(t)
        # self.qt = nqt
        return t
    
    def display(self):
        self.ar(self.qt)
        self.qt.display()
        self.ar(self.qt)
    
    def ar(self,qt:"DynamicQueue"):
        if qt.isEmpty():
            return
        else:
            n = qt.dequeue()
            self.ar(qt)
            qt.enqueue(n)

st = StackUsingQueue()
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