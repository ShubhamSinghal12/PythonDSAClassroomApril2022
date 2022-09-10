def HR(cost,i):
    if i >= len(cost):
        return 0
    else:
        return max(cost[i]+HR(cost,i+2),HR(cost,i+1))

def HRBU(cost):
    dp = [0 for i in range(len(cost)+2)]

    for i in range(len(cost)-1,-1,-1):
        dp[i] = max(dp[i+1],dp[i+2]+cost[i])
    
    return dp[0]


