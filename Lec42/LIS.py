def LIS(ls,i):
    m = 0
    for j in range(i+1,len(ls)):
        if ls[j] > ls[i]:
            m = max(m,LIS(ls,j))
    return m+1

def LISTD(ls,i,dp):
    if dp[i] != 0:
        return dp[i]
    m = 0
    for j in range(i,len(ls)):
        if ls[j] > ls[i]:
            m = max(m,LISTD(ls,j,dp))
    dp[i] = m+1
    return dp[i]

def LISBU(ls):
    # ls.insert(0,-100000)
    dp = [0 for i in range(len(ls))]
    for i in range(len(ls)-1,-1,-1):
        m = 0
        for j in range(i+1,len(ls)):
            if ls[j] > ls[i]:
                m = max(m,dp[j])
        dp[i] = m+1
    
    # return dp[0]-1
    return max(dp)




ls = [10,9,2,5,3,7,101,18]
dp = [0 for i in range(len(ls))]
m = 0
# for i in range(len(ls)):
#     m = max(m,LISTD(ls,i,dp))

# print(max(dp),dp)
print(LISBU(ls))