class BinaryTree:
    class Node:
        def __init__(self,val = 0,left = None,right = None):
            self.data = val
            self.left = left
            self.right = right
    def __init__(self):
        self.root = None
    def createTree2(self):
        n1 = self.Node(10)
        n2 = self.Node(20)
        n3 = self.Node(30)
        n4 = self.Node(40)
        n5 = self.Node(50)
        n6 = self.Node(60)
        n7 = self.Node(70)
        n8 = self.Node(80)

        self.root = n1
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n5.left = n8
        n3.left = n6
        n6.right = n7
    
    def createTree(self):
        self.root = self.__ct(None,True)

    def __ct(self,parent,ilor):
        if parent == None:
            print("Enter data for root Node: ")
        elif ilor:
            print("Enter the data for left child of {}".format(parent.data))
        else:
            print("Enter the data for right child of {}".format(parent.data))
        
        dt = int(input())
        n = self.Node(dt)
        print("Is There a left Child of {} ?".format(dt))
        flag = int(input())
        if flag == 1:
            n.left = self.__ct(n,True)
        
        print("Is There a right Child of {} ?".format(dt))
        flag = int(input())
        if flag == 1:
            n.right = self.__ct(n,False)
        
        return n
    
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
    
    def maximum(self):
        return self.__max(self.root)

    def __max(self,cur):
        if cur == None:
            return -10**7
        else:
            lmax = self.__max(cur.left)
            rmax = self.__max(cur.right)

            return max(lmax,rmax,cur.data)
    def size(self):
        return self.__size(self.root)

    def __size(self,cur):
        if cur == None:
            return 0
        else:
            ls = self.__size(cur.left)
            rs = self.__size(cur.right)

            return ls+rs+1
    
    def ht(self):
        return self.__ht(self.root)

    def __ht(self,cur):
        if cur == None:
            return -1
        else:
            lht = self.__ht(cur.left)
            rht = self.__ht(cur.right)

            return max(lht,rht)+1
    
    def search(self,val):
        return self.__search(self.root,val)

    def __search(self,cur,val):
        if cur == None:
            return False
        else:
            return cur.data == val or self.__search(cur.left,val) or self.__search(cur.right,val)
    
    def preorder(self):
        self.__pre(self.root)
        print()
    
    def __pre(self,cur):
        if cur == None:
            return
        else:
            print(cur.data,end = " ")
            self.__pre(cur.left)
            self.__pre(cur.right)
    
    def inorder(self):
        self.__in(self.root)
        print()
    
    def __in(self,cur):
        if cur == None:
            return
        else:
            self.__in(cur.left)
            print(cur.data,end = " ")
            self.__in(cur.right)
    
    def postorder(self):
        self.__post(self.root)
        print()
    
    def __post(self,cur):
        if cur == None:
            return
        else:
            self.__post(cur.left)
            self.__post(cur.right)
            print(cur.data,end = " ")
    
    def printAtLevel(self,lvl):
        self.__pal(self.root,0,lvl)
        print()

    def __pal(self,cur,clvl,lvl):
        if cur == None:
            return 
        elif lvl == clvl:
            print(cur.data,end= " ")
            return
        else:
            self.__pal(cur.left,clvl+1,lvl)
            self.__pal(cur.right,clvl+1,lvl)
        

bt = BinaryTree()
bt.createTree2()
# bt.display()
# print(bt.maximum())
# print(bt.size())
# print(bt.search(400))

# print("Preorder: ",end= " ")
# bt.preorder()
# print()
# print("inorder: ",end= " ")
# bt.inorder()
# print()
# print("Postorder: ",end= " ")
# bt.postorder()
# print()

bt.printAtLevel(2)
    

