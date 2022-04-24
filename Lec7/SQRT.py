def sqrt(n):
    si = 1
    ei = n
    ans = 0
    while si <= ei:
        mid = (si+ei)//2
        if mid*mid > n:
            ei = mid-1
        else:
            ans = mid
            si = mid+1
    
    return ans

print(sqrt(125))