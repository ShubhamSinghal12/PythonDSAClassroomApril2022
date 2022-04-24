
def reverse(arr,si,ei):
    # si = 0
    # ei = len(arr)-1
    while si < ei:
        t = arr[si]
        arr[si] = arr[ei]
        arr[ei] = t

        si += 1
        ei -= 1

l = [1,2,3,4,5,6]
# l = l[::-1]
l.reverse()
# reverse(l,2,len(l)-2)
print(l)