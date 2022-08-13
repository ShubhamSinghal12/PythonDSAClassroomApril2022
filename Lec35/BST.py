class BST:
    class Node:
        def __init__(self,val = 0,left = None,right = None):
            self.data = val
            self.left = left
            self.right = right
    def __init__(self):
        self.root = None
    
    def createTree(self,inorder):
        self.root = self.__ct(inorder,0,len(inorder)-1)

    def __ct(self,inorder,inlo,inhi):
        if inlo > inhi:
            return None
        else:
            mid = (inlo+inhi)//2
            r = self.Node(inorder[mid])
            r.left = self.__ct(inorder,inlo,mid-1)
            r.right = self.__ct(inorder,mid+1,inhi)

            return r

    def display(self):
        self.__disp(self.root)

    def __disp(self,cur):
        if cur == None:
            return
        else:
            st = ""
            if cur.left:
                st += str(cur.left.data)
            st += " --> "+str(cur.data)+" <-- "
            if cur.right:
                st += str(cur.right.data)
            
            print(st)
            self.__disp(cur.left)
            self.__disp(cur.right)
    
    def search(self,ele):
        return self.__sch(self.root,ele)
    def __sch(self,cur,ele):
        if cur == None:
            return False
        else:
            if cur.data == ele:
                return True
            elif cur.data > ele:
                return self.__sch(cur.left,ele)
            else:
                return self.__sch(cur.right,ele)
    
    def add1(self,ele):
        if self.root == None:
            self.root = self.Node(ele)
        else:
            self.__add1(self.root,ele)
    
    def __add1(self,cur,ele):
        if cur.data > ele:
            if cur.left == None:
                cur.left = self.Node(ele)
            else:
                self.__add1(cur.left,ele)
        else:
            if cur.right == None:
                cur.right = self.Node(ele)
            else:
                self.__add1(cur.right,ele)
    
    def add2(self,ele):
        self.root = self.__add2(self.root,ele)
    def __add2(self,cur,ele):
        if cur == None:
            return self.Node(ele)
        else:
            if cur.data > ele:
                cur.left = self.__add2(cur.left,ele)
            else:
                cur.right = self.__add2(cur.right,ele)
            
            return cur
    
    
    def delNode(self,ele):
        self.root = self.__del(self.root,ele)

    def __del(self,cur,ele):
        if cur == None:
            return None
        else:
            if cur.data > ele:
                cur.left = self.__del(cur.left,ele)
            elif cur.data < ele:
                cur.right = self.__del(cur.right,ele)
            else:
                if cur.left == None and cur.right == None:
                    return None
                elif cur.left == None:
                    return cur.right
                elif cur.right == None:
                    return cur.left
                else:
                    t = cur.left
                    while t.right != None:
                        t = t.right
                    cur.data = t.data
                    cur.left = self.__del(cur.left,t.data)
            return cur

    def ht(self):
        return self.__ht(self.root)

    def __ht(self,cur):
        if cur == None:
            return -1
        else:
            lht = self.__ht(cur.left)
            rht = self.__ht(cur.right)

            return max(lht,rht)+1
    
    def decorder(self):
        self.__dec(self.root)
        print()
    
    def __dec(self,cur):
        if cur == None:
            return
        else:
            self.__dec(cur.right)
            print(cur.data,end = " ")
            self.__dec(cur.left)

    def rws(self):
        self.__rws(self.root,0)
        print()
    
    def __rws(self,cur,sum):
        if cur == None:
            return sum
        else:
            sum = self.__rws(cur.right,sum)
            
            t = cur.data
            cur.data = sum
            sum += t

            sum = self.__rws(cur.left,sum)
            return sum

ino = [10,20,30,40,50,60,70]
bst = BST()
bst.createTree(ino)
bst.rws()
bst.display()
# bst.add2(15)
# bst.add2(45)
# bst.display()
# bst.delNode(20)
# print("------------------------------")
# bst.display()
# bst.decorder()
# print(bst.search(300))
# print(bst.ht())

