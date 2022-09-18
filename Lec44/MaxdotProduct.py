def maxDotProduct(s,t,i,j):
    if i == len(s) or j == len(t):
        return -10**9
    else:
        cur = s[i]*t[j] + max(maxDotProduct(s,t,i+1,j+1),0)
        f = maxDotProduct(s,t,i+1,j)
        s = maxDotProduct(s,t,i,j+1)

        return max(cur,f,s)

s = [2,1,-2,5]
t = [3,0,-6]
print(maxDotProduct(s,t,0,0))