class MyHeap:
    def __init__(self):
        self.heap = []

    def display(self):
        print(self.heap)
    
    def size(self):
        return len(self.heap)
    
    def add(self,ele):
        self.heap.append(ele)
        self.upheapify(len(self.heap)-1)

    def upheapify(self,ci):
        # if ci == 0:
        #     return 
        # else:
            pi = (ci-1)//2
            if pi >= 0 and self.heap[ci] < self.heap[pi]:
                self.heap[ci],self.heap[pi] = self.heap[pi], self.heap[ci]
                self.upheapify(pi)
    
    def getmin(self):
        return self.heap[0]

    def downheapify(self,pi):
        lc = 2*pi+1
        rc = 2*pi+2

        max3 = pi
        if lc < len(self.heap) and self.heap[lc] < self.heap[max3]:
            max3 = lc
        if rc < len(self.heap) and self.heap[rc] < self.heap[max3]:
            max3 = rc

        if max3 != pi:
            self.heap[max3],self.heap[pi] = self.heap[pi], self.heap[max3]
            self.downheapify(max3)
        
    def remove(self):
        self.heap[0],self.heap[-1] = self.heap[-1], self.heap[0]
        t = self.heap.pop()
        self.downheapify(0)
        return t

hp = MyHeap()
hp.add(100)
hp.add(10)
hp.add(40)
hp.add(50)
hp.add(20)
hp.add(80)
hp.display()
hp.remove()
hp.display()
