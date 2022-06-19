# l3 = []
def merge(l1,l2):
    # global l3
    l3 = []
    i = 0
    j = 0
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l3.append(l1[i])
            i += 1
        else:
            l3.append(l2[j])
            j += 1

    # while i < len(l1):
    #     l3.append(l1[i])
    #     i+=1
    
    # while j < len(l2):
    #     l3.append(l2[j])
    #     j+=1 

    l3 += l1[i:]
    l3 += l2[j:]
    
    return l3

def mergeSort(l,si,ei):
    if si == ei:
        return [l[si]]
    else:
        mid = (si+ei)//2
        left = mergeSort(l,si,mid)
        right = mergeSort(l,mid+1,ei)
        return merge(left,right)

# l1 = [1,3,4,8,10]
# l2 = [2,5,7,9,12,13]
# print(merge(l1,l2))
# print(merge(l1,l2))
l = [2,5,1,7,4,3]
print(mergeSort(l,0,len(l)-1))