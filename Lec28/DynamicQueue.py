from MyQueue import MyQueue

class DynamicQueue(MyQueue):
    def enqueue(self, ele):
        if self.isFull():
            nl = [0]*(2*len(self.l))
            j = 0
            for i in range(self.front,self.front+self.size,1):
                nl[j] = self.l[i%len(self.l)]
                j += 1
            self.l = nl

        super().enqueue(ele)

if __name__ == "__main__":
    qt = DynamicQueue(5)
    for i in range(1,15):
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

