def binarySearch(arr,ele):
    si = 0
    ei = len(arr)-1

    while si <= ei:
        mid = (si+ei)//2
        if arr[mid] > ele:
            ei = mid-1
        elif arr[mid] < ele:
            si = mid + 1
        else:
            return mid
    
    return -1

l = [i+1 for i in range(16)]
print(binarySearch(l,50))