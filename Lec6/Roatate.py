
def rotate1(arr):

    t = arr[-1]
    for i in range(len(arr)-2,-1,-1):
        arr[i+1] = arr[i]
    
    arr[0] = t


def rotatek(arr,k):
    k = k%len(arr)
    print(k)
    for i in range(k):
        rotate1(arr)


def reverse(arr,si,ei):
    # si = 0
    # ei = len(arr)-1
    while si < ei:
        t = arr[si]
        arr[si] = arr[ei]
        arr[ei] = t

        si += 1
        ei -= 1

def ro(arr,k):
    k = k%len(arr)
    reverse(arr,0,len(arr)-1)
    reverse(arr,0,k-1)
    reverse(arr,k,len(arr)-1)


l = [1,2,3,4,5]
ro(l,3)
print(l)
