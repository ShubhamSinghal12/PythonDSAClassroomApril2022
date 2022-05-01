def isItPossible(stalls,c,minD):
    noc = 1
    place = stalls[0]
    for i in range(1,len(stalls)):
        if place+minD <= stalls[i]:
            noc += 1
            place = stalls[i]
    
    if noc < c:
        return False
    else:
        return True

def LSAG(stalls,c):
    for i in range(1,stalls[-1]):
        if not isItPossible(stalls,c,i):
            break
    print(i-1)

def BSAG(stalls,c):
    si = 1
    ei = stalls[-1]
    ans = 0
    while si <= ei:
        mid = (si+ei)//2
        if isItPossible(stalls,c,mid):
            ans = mid
            si = mid+1
        else:
            ei = mid-1
    
    print(ans)


stalls = [1,2,4,8,9]
c = 4
# print(isItPossible(stalls,c,4))
BSAG(stalls,c)

