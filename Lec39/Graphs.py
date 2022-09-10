from collections import deque
from queue import PriorityQueue


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
        # self.gp[v][u] = ew
    
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
        
    def getAllConnectedComponents(self):
        qt = deque()
        visited = set()
        acp = []
        for u in self.gp:
            if u in visited:
                continue
            cp = []
            qt.append(u)
            while len(qt) != 0:
                t = qt.popleft()
                if t in visited:
                    continue
                
                visited.add(t)
                cp.append(t)
                for nbrs in self.gp[t]:
                    if nbrs not in visited:
                        qt.append(nbrs)
            acp.append(cp)
        return acp
    

    def DFST(self):
        qt = []
        visited = set()
        for u in self.gp:
            if u in visited:
                continue
            qt.append(u)
            while len(qt) != 0:
                t = qt.pop()
                if t in visited:
                    continue
                
                visited.add(t)
                print(t,end=" ")
                for nbrs in self.gp[t]:
                    if nbrs not in visited:
                        qt.append(nbrs)
        print()
    
    class EdgePair:
        def __init__(self,u,via,cost):
            self.u = u
            self.via = via
            self.cost = cost
        
        def __str__(self):
            return "{} via {} @ {}".format(self.u,self.via,self.cost)
        
        def __lt__(self,oth):
            return self.cost < oth.cost
    def prims(self):
        qt = PriorityQueue()
        visited = set()
        qt.put(self.EdgePair(3,0,0))
        while not qt.empty():
            t = qt.get()
            if t.u in visited:
                continue
            
            visited.add(t.u)
            print(t)
            for nbrs in self.gp[t.u]:
                if nbrs not in visited:
                    qt.put(self.EdgePair(nbrs,t.u,self.gp[t.u][nbrs]))
    
    def dijakstra(self,u):
        qt = PriorityQueue()
        visited = set()
        qt.put(self.EdgePair(u,"",0))
        while not qt.empty():
            t = qt.get()
            if t.u in visited:
                continue
            
            visited.add(t.u)
            print(t)
            for nbrs in self.gp[t.u]:
                if nbrs not in visited:
                    epu = nbrs
                    epVia = t.via+" "+str(t.u)
                    epCost = t.cost+self.gp[t.u][nbrs]
                    qt.put(self.EdgePair(epu,epVia,epCost))
    
    def getAllEdgePair(self):
        ep = []
        for u in self.gp:
            for v in self.gp[u]:
                ep.append(self.EdgePair(u,v,self.gp[u][v]))
        return ep

    def bellmonFord(self,u):
        edges = self.getAllEdgePair()
        dist = {}
        for v in self.gp:
            dist[v] = 10**10

        dist[u] = 0

        for i in range(len(self.gp)):
            for e in edges:
                if dist[e.via] > dist[e.u]+e.cost:
                    if i == len(self.gp)-1:
                        print("Negative Weight Cycle")
                        return
                    dist[e.via] = dist[e.u]+e.cost
            for i in dist:
                print(i,":",dist[i])
            print("------------------------")





# gr = MyGraph(7)
# gr.addEdge(1,2,10)
# gr.addEdge(2,3,20)
# gr.addEdge(3,4,30)
# gr.addEdge(1,4,50)
# gr.addEdge(4,5,60)
# gr.addEdge(5,6,90)
# gr.addEdge(5,7,7)
# gr.addEdge(6,7,5)
# gr.addVertex(8)
# gr.addEdge(7,8,100)
# gr.removeVertex(4)
# gr.display()
# print(gr.hasPathBFS(1,8))
# gr.printAllPath(1,6)
# print(gr.getAllConnectedComponents())
# gr.dijakstra(1)

gr = MyGraph(5)
gr.addEdge(1,2,8)
gr.addEdge(1,3,4)
gr.addEdge(1,4,5)
gr.addEdge(3,4,-3)
gr.addEdge(4,5,4)
gr.addEdge(2,5,-1)
gr.addEdge(5,2,-2)

gr.display()
gr.bellmonFord(1)