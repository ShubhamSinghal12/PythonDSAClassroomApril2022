class MyQueue:
    def __init__(self,cap = 10):
        self.l = [0 for i in range(cap)]
        self.front = 0
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == len(self.l)
    
    def Qsize(self):
        return self.size
    
    def enqueue(self,ele):
        if self.isFull():
            raise Exception("Queue Overflow")
        else:
            self.l[(self.front+self.size)%len(self.l)] = ele
            self.size += 1
    
    def dequeue(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")
        else:
            v = self.l[self.front]
            self.front = (self.front+1)%len(self.l)
            self.size -= 1
            return v
    
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue Underflow")
        else:
            v = self.l[self.front]
            return v
    
    def display(self):
        for i in range(self.front,self.front+self.size,1):
            print(self.l[i%len(self.l)],end = " ")
        print()

qt = MyQueue(5)
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

