l = [1,2,3,4,5,6,7,8,9,10]

def BS(l,si,ei,ele):
    if si > ei:
        return -1
    else:
        mid = (si+ei)//2
        if ele == l[mid]:
            return mid
        elif ele > l[mid]:
            return BS(l,mid+1,ei,ele)
        else:
            return BS(l,si,mid-1,ele)

print(BS(l,0,len(l)-1,8))