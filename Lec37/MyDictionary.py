class myDict:
    th = 2
    class Node:
        def __init__(self,key = None,value = None,next = None):
            self.key = key
            self.value = value
            self.next = next
    def __init__(self,size = 4):
        self.buckets = [None for i in range(size)]
        self.size = 0
    
    def hashFn(self,key):
        hv = hash(key)
        return hv%len(self.buckets)
    
    def put(self,key,value):
        idx = self.hashFn(key)
        tmp = self.buckets[idx]
        while tmp != None:
            if tmp.key == key:
                tmp.value = value
                return
            else:
                tmp = tmp.next
        
        n = self.Node(key,value,self.buckets[idx])
        self.buckets[idx] = n

        self.size += 1

        lf = self.size/len(self.buckets)
        if lf > myDict.th:
            self.rehash()
    
    def rehash(self):
        nb = [None for i in range(len(self.buckets)*2)]
        ob = self.buckets

        self.buckets = nb
        
        for head in ob:
            while head != None:
                self.put(head.key,head.value)
                head = head.next
            
    def get(self,key,default=None):
        idx = self.hashFn(key)
        tmp = self.buckets[idx]
        while tmp != None:
            if tmp.key == key:
                return tmp.value
            else:
                tmp = tmp.next
        return default
    
    def remove(self,key):
        idx = self.hashFn(key)
        tmp = self.buckets[idx]
        prev = tmp
        while tmp != None:
            if tmp.key == key:
                break
            else:
                prev = tmp
                tmp = tmp.next

        if tmp == None:
            return None
        if prev == tmp:
            self.buckets[idx] = self.buckets[idx].next
        else:
            prev.next = tmp.next
        
        return tmp.value

    def __str__(self) -> str:
        st = "{ "
        for head in self.buckets:
            while head != None:
                st += str(head.key)+" : "+str(head.value)+" , "
                head = head.next
        st += " }"
        return st
    
d1 = myDict()
d1.put("ram",10)
d1.put("rama",100)
d1.put("sita",20)
d1.put("ram",50)
print(d1)
d1.remove("ram")
print(d1)
