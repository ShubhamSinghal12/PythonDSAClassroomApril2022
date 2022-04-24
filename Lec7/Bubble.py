def bubbleSort(arr):
    for i in range(len(arr)-1):
        swap = 0
        for j in range(len(arr)-1-i):
            if arr[j] > arr[j+1]:
                swap += 1
                t = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = t
        
        if swap == 0:
            print(i)
            return

l = [5,1,4,2,3,6,7,8,9]
bubbleSort(l)
print(l)