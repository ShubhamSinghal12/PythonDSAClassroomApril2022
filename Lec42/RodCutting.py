def MaxP(length,price,n):
    if n == 0:
        return 0
    else:
        m = 0
        for i in range(len(length)):
            if length[i] <= n:
                m = max(m,MaxP(length,price,n-length[i])+price[i])
        return m

def MaxPBU(length,price,n):
    dp = [0 for i in range(n+1)]
    
    for j in range(n+1):
        m = 0
        for i in range(len(length)):
            if length[i] <= j:
                m = max(m,dp[j-length[i]]+price[i])
        dp[j] = m
    
    print(dp)
    return dp[-1]


length = [1,2,3,4,5,6,7,8]
price = [1,  5,   8,   9,  10, 17,  17,  20]
# print(MaxP(length,price,10))
print(MaxPBU(length,price,10))