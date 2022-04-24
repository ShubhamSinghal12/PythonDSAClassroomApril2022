def lowerBound(arr,ele):
    si = 0
    ei = len(arr)-1
    ans = -1

    while si <= ei:
        mid = (si+ei)//2
        if arr[mid] > ele:
            ei = mid-1
        elif arr[mid] < ele:
            si = mid + 1
        else:
            ans = mid
            ei = mid-1
    
    return ans


def upperBound(arr,ele):
    si = 0
    ei = len(arr)-1
    ans = -1

    while si <= ei:
        mid = (si+ei)//2
        if arr[mid] > ele:
            ei = mid-1
        elif arr[mid] < ele:
            si = mid + 1
        else:
            ans = mid
            si = mid+1
    
    return ans
l = [1,1,1,1,2,2,2,2,3,4,5,6,6,7,7,7,8,8,9,9,9]
print(upperBound(l,2))