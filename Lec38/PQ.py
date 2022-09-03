from queue import PriorityQueue

pq = PriorityQueue()
pq.put((-1,100))
pq.put((-2,200))
pq.put((-3,10))
# pq.put(30)
# pq.put(80)
# pq.put(50)

while not pq.empty():
    p = pq.get()
    print(p)