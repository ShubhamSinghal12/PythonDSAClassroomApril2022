from collections import deque

l = [2,-1,-7,8,-15,30,24,6]

def printFN(l,k):
    dq = deque()
    for i in range(k):
        if l[i] < 0:
            dq.append(i)
    # print(dq)
    if len(dq) == 0:
        print(0,end = " ")
    else:
        print(l[dq[0]],end= " ")
    
    for i in range(k,len(l)):
        if l[i] < 0:
            dq.append(i)
        if len(dq)!=0 and dq[0] <= i-k:
            dq.popleft()
        # print(dq)
        if len(dq) == 0:
            print(0,end = " ")
        else:
            print(l[dq[0]],end= " ")

printFN(l,3)
print()

