
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
    
    def kreverse(self,k=3):
        self.head = self.__kr(self.head,k)

    def __kr(self,cur,k):
        if cur == None:
            return None
        else:
            temp = cur
            s = k
            while temp != None and s >= 1:
                temp = temp.next
                s -= 1
            
            prev = self.__kr(temp,k)

            while cur!=temp:
                ahead = cur.next
                cur.next = prev
                prev = cur
                cur = ahead
            
            return prev
    
    def midNode(self):
        return self.__mid().data
    
    def __mid(self):
        slow = self.head
        fast = self.head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def merge(self,l2):
        l3 = MyLinkedList()
        i = self.head
        j = l2.head
        while i!= None and j!= None:
            if i.data > j.data:
                l3.addLast(j.data)
                j = j.next
            else:
                l3.addLast(i.data)
                i = i.next
        while i != None:
            l3.addLast(i.data)
            i = i.next
        while j!= None:
            l3.addLast(j.data)
            j = j.next
        
        return l3

    def mergeSort(self):
        l3 = self.__mergerSortHelper()
        self.head = l3.head

    def __mergerSortHelper(self):
        if self.head.next == None:
            # l3 = MyLinkedList()
            # l3.head = self.head
            return self
        else:
            midNode = self.__mid()
            # l1 = MyLinkedList()
            l2 = MyLinkedList()
            # l1.head = self.head
            l2.head = midNode.next
            midNode.next = None

            left = self.__mergerSortHelper()
            right = l2.__mergerSortHelper()

            return left.merge(right)
    
    def DummyListForIntersection(self):

        n1= self.Node(1)
        n2= self.Node(2)
        n3= self.Node(3)
        n4= self.Node(4)
        n5= self.Node(5)
        n6= self.Node(6)
        n7= self.Node(7)
        n8= self.Node(8)
        n9= self.Node(9)
        n10= self.Node(10)
        n11= self.Node(11)
        n12= self.Node(12)
        n13= self.Node(13)


        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n9
        n9.next = n10
        n10.next = None
        n11.next = n12
        n12.next = n13
        n13.next = n7
        self.Intersection(n1,n11)

    def Intersection(self,head1,head2):
        t1 = head1
        t2 = head2

        while t1 != t2:
            if t1 == None:
                t1 = head2
            if t2 == None:
                t2 = head1

            t1 = t1.next
            t2 = t2.next
        
        print("Intersection",t1.data)


    def dummyListForCycle(self):
        n1= self.Node(1)
        n2= self.Node(2)
        n3= self.Node(3)
        n4= self.Node(4)
        n5= self.Node(5)
        n6= self.Node(6)
        n7= self.Node(7)
        n8= self.Node(8)

        n1.next = n2
        n2.next = n3
        n3.next = n4
        n4.next = n5
        n5.next = n6
        n6.next = n7
        n7.next = n8
        n8.next = n3

        self.head = n1
    
    def cycleDetectionRemoval(self):
        slow = self.head
        fast = self.head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                # print("Cycle")
                t1 = self.head
                t2 = slow
                while t1.next != t2.next:
                    t1 = t1.next
                    t2 = t2.next
                t2.next = None
                print("Cycle Removed")
                break
        else:
            print("No Cycle")
    
    def fold(self):
        l2 = MyLinkedList()
        mid = self.__mid()
        l2.head = mid.next
        mid.next = None
        l2.reverse()

        t1= self.head
        t2 = l2.head

        cur = self.Node(0)
        h = cur

        while t1 != None or t2 != None:
            if t1 != None:
                cur.next = t1
                cur = cur.next
                t1 = t1.next
            if t2 != None:
                cur.next = t2
                cur = cur.next
                t2 = t2.next
        
        self.head = h.next



ll = MyLinkedList()
for i in range(1,8):
    ll.addLast(i)
ll.display()
ll.fold()
ll.display()
# ll.dummyListForCycle()
# ll.display()
# ll.cycleDetectionRemoval()
# ll.display()
# ll2 = MyLinkedList()
# for i in range(1,6):
#     ll.addLast(i+1)
#     ll.addFirst(2*i+3)

# # l3 = ll.merge(ll2)
# ll.display()
# ll.mergeSort()
# ll.display()
# ll.display()
# ll.kreverse(5)
# ll.display()


# ll.addLast(5)
# ll.addLast(4)
# ll.addLast(3)
# ll.addLast(2)
# ll.addLast(1)
# ll.addAt(5,2)
# print(ll.getLast())
# print(ll.getFirst())
# print(ll.getAt(2))
# ll.display()
# ll.reverseR2()
# ll.display()
# print(ll.size())
