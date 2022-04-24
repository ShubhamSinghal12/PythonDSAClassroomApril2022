l = [1,2,3,4,5,6]

def search(arr,ele):
    for i in range(len(arr)):
        if arr[i] == ele:
            return i
    
    return -1

print(search(l,10))
print(30 in l)


def maxi(arr):
    max = arr[0]
    for i in arr:
        if max < i:
            max = i
    
    return max

l = [10,50,30,4,100,-1]
print(maxi(l))
print(max(l))
print(max(14,2,3,12))
