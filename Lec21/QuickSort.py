def partition(l,si,ei):
    j = si
    for i in range(si,ei+1):
        if l[i] <= l[ei]:
            t = l[i]
            l[i] = l[j]
            l[j] = t

            j+=1

    # l[j],l[ei] = l[ei],l[j]
    return j-1

def quicksort(l,si,ei):
    if si >= ei:
        return
    else:
        p = partition(l,si,ei)
        quicksort(l,si,p-1)
        quicksort(l,p+1,ei)

l = [2,5,1,7,3,8,6,4]
quicksort(l,0,len(l)-1)
print(l)