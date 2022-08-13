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
    
    def pir(self,a,b):
        self.__in(self.root,a,b)
        print()
    
    def __in(self,cur,a,b):
        if cur == None:
            return
        else:
            if cur.data >= a:
                self.__in(cur.left,a,b)
            if a <= cur.data <= b:
                print(cur.data,end = " ")
            if cur.data <= b:
                self.__in(cur.right,a,b) 
    
    def isBSTrange(self):
        return self.__isBSTr(self.root,-10**4,10**4)
    
    def __isBSTr(self,cur,a,b):
        if cur == None:
            return True
        else:
            if a > cur.data or b < cur.data:
                return False
            else:
                return self.__isBSTr(cur.left,a,cur.data) and self.__isBSTr(cur.right,cur.data,b)

    def maximum(self):
        return self.__max(self.root)

    def __max(self,cur):
        if cur == None:
            return -10**7
        else:
            lmax = self.__max(cur.left)
            rmax = self.__max(cur.right)

            return max(lmax,rmax,cur.data)

    def minimum(self):
        return self.__min(self.root)

    def __min(self,cur):
        if cur == None:
            return 10**7
        else:
            lmin = self.__min(cur.left)
            rmin = self.__min(cur.right)

            return min(lmin,rmin,cur.data)
    
    def isBST1(self):
        return self.__isBST1(self.root)
    
    def __isBST1(self,cur):
        if cur == None:
            return True
        else:
            curBST = False
            if cur.data >= self.__max(cur.left) and cur.data <= self.__min(cur.right):
                curBST = True
            
            return curBST and self.__isBST1(cur.left) and self.__isBST1(cur.right)
    
    def isBST2(self):
        return self.__isBST2(self.root)[0]
    
    def __isBST2(self,cur):
        if cur == None:
            return True,-10**4,10**4
        else:
            lisBst,lmax,lmin = self.__isBST2(cur.left)
            risBst,rmax,rmin = self.__isBST2(cur.right)
            curBST = False
            if cur.data >= lmax and cur.data <= rmin:
                curBST = True
            
            return curBST and lisBst and risBst, max(lmax,rmax,cur.data), min(lmin,rmin,cur.data)

    def maxBST(self):
        return self.__disp(self.__maxBST(self.root)[3])
    
    def __maxBST(self,cur):
        if cur == None:
            return True,-10**4,10**4,None,0,0
        else:
            lisBst,lmax,lmin, lmaxBSTroot, lsize, lmaxBSTsize = self.__maxBST(cur.left)
            risBst,rmax,rmin, rmaxBSTroot, rsize, rmaxBSTsize = self.__maxBST(cur.right)
            
            cisBst = False
            if cur.data >= lmax and cur.data <= rmin:
                cisBst = True
            
            cisBst = cisBst and lisBst and risBst
            cmax = max(lmax,rmax,cur.data)
            cmin = min(lmin,rmin,cur.data)
            csize = lsize + rsize + 1

            if cisBst:
                cmaxBSTroot = cur
                cmaxBSTsize = csize
            else:
                cmaxBSTroot = lmaxBSTroot if lmaxBSTsize >= rmaxBSTsize else rmaxBSTroot
                cmaxBSTsize = lmaxBSTsize if lmaxBSTsize >= rmaxBSTsize else rmaxBSTsize
            
            return cisBst,cmax,cmin, cmaxBSTroot, csize, cmaxBSTsize



ino = [10,20,30,40,500,60,70]
bst = BST()
bst.createTree(ino)
# bst.display()
bst.maxBST()
# bst.rws()
# bst.display()
# bst.pir(30,50)
# bst.add2(15)
# bst.add2(45)
# bst.display()
# bst.delNode(20)
# print("------------------------------")
# bst.display()
# bst.decorder()
# print(bst.search(300))
# print(bst.ht())

