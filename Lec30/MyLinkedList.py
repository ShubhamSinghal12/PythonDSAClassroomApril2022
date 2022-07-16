class MyLinkedList:
    class Node:
        def __init__(self,val = 0,next = None):
            self.data = val
            self.next = next
    
    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        tmp = self.head
        cnt = 0
        while tmp!= None:
            cnt += 1
            tmp = tmp.next
        return cnt

    def addFirst(self,ele):
        n = self.Node(ele,self.head)
        self.head = n

    def display(self):
        tmp = self.head
        while tmp!= None:
            print(tmp.data,end= " ")
            tmp = tmp.next
        print()
    def addLast(self,ele):
        if self.isEmpty():
            self.addFirst(ele)
            return
        
        n = self.Node(ele)
        
        tmp = self.head
        while tmp.next!=None:
            tmp = tmp.next
        
        tmp.next = n
    

    def addAt(self,ele,idx):
        if idx<0 or idx >self.size():
            return
        elif idx == 0:
                self.addFirst(ele)
                return
        else:
            tmp = self.__gAt(idx-1)
            n = self.Node(ele,tmp.next)
            tmp.next = n

    
    def getFirst(self):
        if self.isEmpty():
            return None

        return self.head.data
    
    def __gAt(self,idx):
        i = 0
        temp = self.head
        while temp != None and i < idx:
            temp = temp.next
            i += 1
        return temp
    
    def getAt(self,idx):
        if idx < 0 or idx >= self.size():
            return None
        else:
            return self.__gAt(idx).data
    
    def getLast(self):
        return self.__gAt(self.size()-1).data
    
    def removeFirst(self):
        if self.isEmpty():
            return None
        
        tmp = self.head
        self.head = self.head.next
        return tmp.data
    
    def removeLast(self):
        if self.isEmpty():
            return None
        elif self.head.next == None:
            return self.removeFirst()
        else:
            tmp = self.__gAt(self.size()-2)
            dt = tmp.next.data
            tmp.next = None
            return dt
    
    def removeAt(self,idx):
        if idx < 0 or idx >= self.size():
            return None
        if idx == 0:
            return self.removeFirst()
        
        tmp = self.__gAt(idx-1)
        dt = tmp.next.data
        tmp.next = tmp.next.next
        return dt
    
    def reverse(self):
        cur = self.head
        prev = None
        while cur != None:
            ahead = cur.next
            cur.next = prev
            prev = cur
            cur = ahead
        self.head = prev
    
    def reverseR(self):
        self.__rR(self.head,None)

    def __rR(self,cur,prev):
        if cur == None:
            self.head = prev
        else:
            self.__rR(cur.next,cur)
            cur.next = prev
    
    def reverseR2(self):
        tmp = self.head
        self.__rR2(self.head)
        tmp.next = None

    def __rR2(self,prev):
        if prev.next == None:
            self.head = prev
        else:
            self.__rR2(prev.next)
            prev.next.next = prev

ll = MyLinkedList()
# ll.addLast(5)
ll.addLast(4)
ll.addLast(3)
ll.addLast(2)
ll.addLast(1)
ll.addAt(5,2)
# print(ll.getLast())
# print(ll.getFirst())
# print(ll.getAt(2))
ll.display()
ll.reverseR2()
ll.display()
# print(ll.size())
