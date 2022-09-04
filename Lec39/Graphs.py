from collections import deque


class MyGraph:
    def __init__(self,nv = 0):
        self.gp = {}
        for i in range(nv):
            self.gp[i+1] = {}
    
    def addVertex(self,v):
        self.gp[v] = {}

    def containsEdge(self,u,v):
        return v in self.gp[u]

    def countVertex(self):
        return len(self.gp)
    
    def addEdge(self,u,v,ew=1):
        self.gp[u][v] = ew
        self.gp[v][u] = ew
    
    def removeEdge(self,u,v):
        if self.containsEdge(u,v):
            self.gp[u].pop(v)
            self.gp[v].pop(u)
    
    def countEdges(self):
        s = 0
        for v in self.gp:
            s += len(self.gp[v])
        
        return s//2
    
    def display(self):
        for i in self.gp:
            print(i,self.gp[i])
    
    def removeVertex(self,u):
        for v in self.gp[u]:
            self.gp[v].pop(u)

        self.gp.pop(u)
    
    def hasPath(self,u,v):
        return self.__hp(u,v,set())

    def __hp(self,u,v,visited:"set"):
        if u == v:
            return True
        else:
            visited.add(u)
            f = False
            for nbrs in self.gp[u]:
                if nbrs not in visited:
                    f = f or self.__hp(nbrs,v,visited)
            return f
    
    def printAllPath(self,u,v):
        self.__pap(u,v,set(),"")

    def __pap(self,u,v,visited:"set",ans):
        if u == v:
            print(ans+str(v))
        else:
            visited.add(u)
            for nbrs in self.gp[u]:
                if nbrs not in visited:
                    self.__pap(nbrs,v,visited,ans +"{} - ".format(u))
            visited.remove(u)
    
    def hasPathBFS(self,u,v):
        qt = deque()
        qt.append(u)
        visited = set()
        while len(qt) != 0:
            t = qt.popleft()
            if t in visited:
                continue
            if t == v:
                return True
            
            visited.add(t)
            for nbrs in self.gp[t]:
                if nbrs not in visited:
                    qt.append(nbrs)
        return False

    def BFST(self):
        qt = deque()
        visited = set()
        for u in self.gp:
            if u in visited:
                continue
            qt.append(u)
            while len(qt) != 0:
                t = qt.popleft()
                if t in visited:
                    continue
                
                visited.add(t)
                print(t,end=" ")
                for nbrs in self.gp[t]:
                    if nbrs not in visited:
                        qt.append(nbrs)
        print()
    
    def isCycle(self):
        qt = deque()
        visited = set()
        for u in self.gp:
            if u in visited:
                continue
            qt.append(u)
            while len(qt) != 0:
                t = qt.popleft()
                if t in visited:
                    return True
                
                visited.add(t)
                for nbrs in self.gp[t]:
                    if nbrs not in visited:
                        qt.append(nbrs)
        return False
    
    def noOfConnectedComponents(self):
        qt = deque()
        visited = set()
        nc = 0
        for u in self.gp:
            if u in visited:
                continue
            qt.append(u)
            nc += 1
            while len(qt) != 0:
                t = qt.popleft()
                if t in visited:
                    continue
                
                visited.add(t)
                for nbrs in self.gp[t]:
                    if nbrs not in visited:
                        qt.append(nbrs)
        return nc
    
    def isTree(self):
        return self.isCycle() == False and self.noOfConnectedComponents() == 1
    
    def isConnected(self):
        return self.noOfConnectedComponents() == 1
        

gr = MyGraph(7)
gr.addEdge(1,2,10)
gr.addEdge(2,3,20)
# gr.addEdge(3,4,30)
gr.addEdge(1,4,50)
gr.addEdge(4,5,60)
gr.addEdge(5,6,90)
gr.addEdge(5,7,7)
# gr.addEdge(6,7,5)
gr.addVertex(8)
# gr.addEdge(7,8,100)
# gr.removeVertex(4)
gr.display()
# print(gr.hasPathBFS(1,8))
# gr.printAllPath(1,6)
print(gr.noOfConnectedComponents())
