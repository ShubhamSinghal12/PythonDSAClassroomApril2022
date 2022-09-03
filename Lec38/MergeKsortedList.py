from queue import PriorityQueue

#(Value,ListNo,Index) --> Tuple to be inserted in PQ
l = [[1,4,5],[1,3,4],[2,6]]

ans = []
pq = PriorityQueue()

for i in range(len(l)):
    pq.put((l[i][0],i,0))

while not pq.empty():
    value,listNo,index = pq.get()
    ans.append(value)
    if index+1 < len(l[listNo]):
        pq.put((l[listNo][index+1],listNo,index+1))

print(ans)
