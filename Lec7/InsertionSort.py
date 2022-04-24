def insert(arr,i):
    t = arr[i]
    # flag = True
    for i in range(i-1,-2,-1):
        if arr[i] > t:
            arr[i+1] = arr[i]
        else:
            # arr[i+1] = t
            # flag = False
            break
    arr[i+1] = t

def insertionSort(arr):
    for i in range(1,len(arr)):
        insert(arr,i)
    

l = [1,2,4,5,0,1,2, 3, 4, 6]
insertionSort(l)
print(l)