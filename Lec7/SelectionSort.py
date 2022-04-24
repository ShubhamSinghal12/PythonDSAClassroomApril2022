def minS(arr,i):
    m = i
    for k in range(i+1,len(arr)):
        if arr[m] > arr[k]:
            m = k
    return m

def SelectionSort(arr):
    for i in range(len(arr)-1):
        m = minS(arr,i)
        t = arr[i]
        arr[i] = arr[m]
        arr[m] = t

l = [5,1,4,2,3]
SelectionSort(l)
print(l)

