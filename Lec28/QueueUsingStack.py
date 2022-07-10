from DynamicStack import DynamicStack

class QueueUsingStack:
    def __init__(self,cap = 10):
        self.st = DynamicStack()
    
    def isEmpty(self):
        return self.st.isEmpty()
    
    def Qsize(self):
        return self.st.size()
    
    def enqueue(self,ele):
        self.pushFirst(self.st,ele)

    def pushFirst(self,st,ele):
        if st.isEmpty():
            st.push(ele)
        else:
            n = st.pop()
            self.pushFirst(st,ele)
            st.push(n)
    
    def dequeue(self):
        return self.st.pop()
    
    def peek(self):
        return self.st.peek()
    
    def display(self):
        self.st.display()

qt = QueueUsingStack(5)
for i in range(1,6):
    qt.enqueue(i)
    qt.display()

print(qt.dequeue())
print(qt.dequeue())
qt.display()
print(qt.peek())
qt.display()

qt.enqueue(10)
qt.enqueue(20)
qt.display()

