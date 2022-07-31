from collections import deque
#https://leetcode.com/problems/binary-tree-maximum-path-sum/
#https://leetcode.com/problems/path-sum/

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
        n9 = self.Node(90)

        self.root = n1
        n1.left = n2
        n1.right = n3
        n2.left = n4
        n2.right = n5
        n5.left = n8
        n3.left = n6
        n7.right = n9
        n6.right = n7

    def createTreeUsingPreIn(self,pre,ino):
        self.root = self.__ct(pre,ino,0,len(pre)-1,0,len(ino)-1)

    def __ct(self,pre,ino,plo,phi,inlo,inhi):
        if inlo >inhi:
            return None
        else:
            r = self.Node(pre[plo])
            i = self.__search(ino,inlo,inhi,pre[plo])

            r.left = self.__ct(pre,ino,plo+1,plo+i-inlo,inlo,i-1)
            r.right = self.__ct(pre,ino,plo+i-inlo+1,phi,i+1,inhi)

            return r
            
    def __search(self,ino,inlo,inhi,dt):
        i = inlo
        while i <= inhi:
            if ino[i] == dt:
                return i
            i += 1
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
    
    def ht(self):
        return self.__ht(self.root)

    def __ht(self,cur):
        if cur == None:
            return -1
        else:
            lht = self.__ht(cur.left)
            rht = self.__ht(cur.right)

            return max(lht,rht)+1
    
    def isBal(self):
        return self.__isBal(self.root)

    def __isBal(self,cur):
        if cur == None:
            return True
        else:
            lbal = self.__isBal(cur.left)
            rbal = self.__isBal(cur.right)

            curBal = abs(self.__ht(cur.left)-self.__ht(cur.right)) <= 1
            
            return lbal and rbal and curBal
    
    def isBal2(self):
        return self.__isBal2(self.root)[0]

    def __isBal2(self,cur):
        if cur == None:
            return True,-1
        else:
            lbal,lht = self.__isBal2(cur.left)
            rbal,rht = self.__isBal2(cur.right)

            curBal = abs(lht-rht) <= 1
            
            return lbal and rbal and curBal, max(lht,rht)+1
    
    def dia(self):
        return self.__dia(self.root)

    def __dia(self,cur):
        if cur == None:
            return 0
        else:
            ldia = self.__dia(cur.left)
            rdia = self.__dia(cur.right)

            curdia = self.__ht(cur.left) + self.__ht(cur.right) + 2
            
            return max(ldia,rdia,curdia)
    
    def dia2(self):
        return self.__dia2(self.root)[0]

    def __dia2(self,cur):
        if cur == None:
            return -1,-1
        else:
            ldia,lht = self.__dia2(cur.left)
            rdia,rht = self.__dia2(cur.right)

            curdia = lht+rht+2
            
            return max(ldia,rdia,curdia), max(lht,rht)+1
    
    def leftView(self):
        qt = deque()
        temp = deque()
        qt.append(self.root)
        print(self.root.data,end= " ")
        while qt:
            r = qt.popleft()
            # print(r.data,end= " ")
            if r.left:
                temp.append(r.left)
            if r.right:
                temp.append(r.right)
            if not qt:
                if temp:
                    print(temp[0].data,end = " ")
                qt = temp
                temp = deque()
        print()
    
    def rightView(self):
        qt = deque()
        temp = deque()
        qt.append(self.root)
        print(self.root.data,end= " ")
        while qt:
            r = qt.popleft()
            # print(r.data,end= " ")
            if r.left:
                temp.append(r.left)
            if r.right:
                temp.append(r.right)
            if not qt:
                if temp:
                    print(temp[-1].data,end = " ")
                qt = temp
                temp = deque()
        print()

    def lv(self):
        self.__lv(self.root,0,0)
        print()

    def __lv(self,cur,lvl,mlvl):
        if cur == None:
            return mlvl
        else:
            if lvl == mlvl:
                print(cur.data,end=" ")
                mlvl += 1
            
            mlvl = self.__lv(cur.left,lvl+1,mlvl)
            mlvl = self.__lv(cur.right,lvl+1,mlvl)
            return mlvl
    
    def rv(self):
        self.__rv(self.root,0,0)
        print()
    def __rv(self,cur,lvl,mlvl):
        if cur == None:
            return mlvl
        else:
            if lvl == mlvl:
                print(cur.data,end=" ")
                mlvl += 1
            
            mlvl = self.__lv(cur.right,lvl+1,mlvl)
            mlvl = self.__lv(cur.left,lvl+1,mlvl)
            return mlvl


pre = [10,20,40,50,80,30,60,70]
ino = [40,20,80,50,10,60,70,30]

bt = BinaryTree()
bt.createTree2()
# bt.display()
# print(bt.dia2())
bt.rv()
